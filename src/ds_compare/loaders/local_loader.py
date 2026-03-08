from pathlib import Path
from ds_compare.loaders import LoaderConfig
from ds_compare.models.documents import Document

"""LocalFileLoader loads documents from the local file system.

    Supports loading multiple files based on file extensions and
    recursive directory traversal.
"""
class LocalFileLoader:
    def __init__(self, config: LoaderConfig) -> None:
        self.config = config
        self.path = Path(config.base_source)

    def load(self) -> list[Document]:
        """Returns all documents from the base_source directory.

        Iterates through configured file extensions and loads matching files.
        Skips files that cannot be read due to permissions or encoding errors.
        """
        documents = []

        for file_extension in self.config.file_extensions:
            file_pattern = f"*{file_extension}"
            if self.config.recursive:
                files = self.path.rglob(file_pattern)
            else:
                files = self.path.glob(file_pattern)
            for file in files:
                try: 
                    content=file.read_text(encoding="utf-8")
                except (PermissionError, UnicodeDecodeError) as error:
                    print(f"Skipping {file}. \n Error message :{error}")
                    continue

                new_doc = Document(
                    id=str(file.relative_to(self.path)),
                    content=content,
                    source_path=str(file),
                    metadata={
                        "filename": file.name,
                        "extension": file.suffix,
                        "design_system": self.config.design_system.name
                        }
                )
                documents.append(new_doc)

        return documents

    def load_single_doc(self, source_path: str) -> Document:
        """Returns a single document from the given file path.

        Args:
            source_path: absolute or relative file path to load

        Raises:
            FileNotFoundError: if the file does not exist
        """
        file = Path(source_path)
        
        if not file.exists():
            raise FileNotFoundError(f"File not found: {source_path}")
        
        new_doc = Document(
            id=str(file.relative_to(self.path)),
            content=file.read_text(),
            source_path=str(file),
            metadata={
                "filename": file.name,
                "extension": file.suffix,
                "design_system": self.config.design_system.name
                }
        )

        return new_doc
        
    def supports_source(self, source: str) -> bool:
        """Returns true if the source path exists in the local file system.

        Args:
            source: file path or directory path to check
        """
        return Path(source).exists()


if __name__ == "__main__":
    from ds_compare.loaders import LoaderConfig
    from ds_compare.models.documents import DSInfo

    config = LoaderConfig(
        base_source="test_docs",
        file_extensions=[".md"],
        recursive=True,
        design_system=DSInfo(name="Test DS")
    )

    loader = LocalFileLoader(config)
    docs = loader.load()
    print(f"Loaded {len(docs)} documents")
    for doc in docs:
        print(doc)