"""
Unit tests for document loader and loader config.
"""

import pytest

from ds_compare.loaders import LoaderConfig, DocumentLoader
from ds_compare.models.documents import DSInfo, Document

def test_loader_config_creation():
    """Test that LoaderConfig can be instantiated with valid data."""
    mock_design_system = DSInfo(name="Chauncey", url="www.misterbigshot.com")
    mock_config = LoaderConfig(
        base_source="/documents",
        file_extensions=[".md", ".mdx"],
        recursive=True,
        design_system=mock_design_system
    )

    assert(mock_config.base_source)=="/documents"
    assert(mock_config.file_extensions)==[".md", ".mdx"]
    assert(mock_config.recursive)==True
    assert(mock_config.design_system)==mock_design_system
    assert(mock_config.design_system.name)=="Chauncey"
    assert(mock_config.design_system.url)=="www.misterbigshot.com"

def test_document_loader(): 
    """Test document protocol"""

    class MockDocLoader: 
        def load(self) -> list[Document]:
            return []

        def load_single_doc(self, source_path: str) -> Document:
            return Document(id="chauncey", content="he's kind of a big deal", source_path="", metadata={})
        
        def supports_source(self, source: str) -> bool:
            return True
    
    mock_loader: DocumentLoader = MockDocLoader()

    assert(mock_loader.load_single_doc(source_path="./home").id)=="chauncey"
    assert(mock_loader.load_single_doc(source_path="./home").content)=="he's kind of a big deal"