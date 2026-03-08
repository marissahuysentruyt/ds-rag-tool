"""
Unit tests for the LocalFileLoader
"""

import pytest

from pathlib import Path
from ds_compare.loaders import LoaderConfig
from ds_compare.models import Document
from ds_compare.loaders.local_loader import LocalFileLoader
from ds_compare.models.documents import DSInfo

TEST_DOCS_PATH = Path(__file__).parent / "test_docs"

@pytest.fixture
def loader():
    mock_config = LoaderConfig(
        base_source=str(TEST_DOCS_PATH),
        file_extensions=[".md"],
        recursive=True,
        design_system=DSInfo(name="Test System")
    )

    return LocalFileLoader(mock_config)

def test_loads_documents(loader):
    documents = loader.load()

    assert len(documents) == 4
    assert all(isinstance(doc, Document) for doc in documents)
    assert all("filename" in doc.metadata for doc in documents)
    assert all("extension" in doc.metadata for doc in documents)
    assert all("design_system" in doc.metadata for doc in documents)

def test_filters_docs_by_extension():
    mock_config = LoaderConfig(
        base_source=str(TEST_DOCS_PATH),
        file_extensions=[".txt"],
        recursive=True,
        design_system=DSInfo(name="Test System")
    )

    loader = LocalFileLoader(mock_config)
    documents = loader.load()
    
    assert len(documents) == 0

def test_load_single_doc(loader):
    document = loader.load_single_doc(str(TEST_DOCS_PATH/"modal.md"))

    assert document
    assert isinstance(document, Document)
    assert document.metadata["filename"] == "modal.md"
    assert document.metadata["extension"] == ".md"
    assert "Stack modals on top of each other" in document.content

def test_raises_error_if_file_not_found(loader): 
    with pytest.raises(FileNotFoundError):
        loader.load_single_doc(str(TEST_DOCS_PATH/"popover.md",))

def test_supported_source_directory(loader):
    isSupported = loader.supports_source(str(TEST_DOCS_PATH/"button.md"))
    isUnsupported = loader.supports_source(str(TEST_DOCS_PATH/"popover.txt"))
    isSupportedDirectory = loader.supports_source(str(TEST_DOCS_PATH))
    isUnsupportedUrl = loader.supports_source("www.mrbigshot.com")

    assert isSupported
    assert not isUnsupported
    assert isSupportedDirectory
    assert not isUnsupportedUrl

def test_not_recursive(): 
    mock_config = LoaderConfig(
        base_source=str(TEST_DOCS_PATH),
        file_extensions=[".md"],
        recursive=False,
        design_system=DSInfo(name="Test System")
    )

    loader = LocalFileLoader(mock_config)
    documents = loader.load()

    assert len(documents) == 3