from typing import Protocol
from dataclasses import dataclass
from ds_compare.models.documents import DSInfo, Document

class DocumentLoader(Protocol): 
    def load(self) -> list[Document]:
        """Returns all of the documents from a source (url, file path)"""
        ...

    def load_single_doc(self, source_path: str) -> Document:
        """Returns a single document from the source"""
        ...

    def supports_source(self, source: str) -> bool:
        """Returns true if a loader supports a source

            Args:
                source: a file path, directory path, URL, or git repo URL.   
                    Loaders will determine what's supported.
        """
        ...
@dataclass
class LoaderConfig: 
    base_source: str
    file_extensions: list[str]
    recursive: bool
    design_system: DSInfo
