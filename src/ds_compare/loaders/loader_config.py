from dataclasses import dataclass
from ds_compare.models.documents import DSInfo

@dataclass
class LoaderConfig: 
    base_source: str
    file_extensions: list[str]
    recursive: bool
    design_system: DSInfo