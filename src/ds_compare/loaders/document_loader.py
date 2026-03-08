from typing import Protocol
from dataclasses import dataclass
from ds_compare.models.documents import Document

"""Any classes that implement this Protocol must use this data shape. 
   Define these methods with matching signatures.
"""
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