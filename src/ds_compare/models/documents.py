"""Document represent the raw document before chunking.

    Fields:
        id,
        content,
        source_path,
        metadata (dict)
"""
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Document:
    id: str
    content: str
    source_path: str
    metadata: dict = field(default_factory=dict)

"""Chunks represent a piece of a document.
    Fields:
        id,
        content,
        document_id,
        start_index,
        end_index
        metadata (dict)
"""
@dataclass
class Chunk:
    id: str
    content: str
    document_id: str
    start_index: int
    end_index: int
    metadata: dict = field(default_factory=dict)

"""Design system info represents the metadata of particular design system.
    Fields:
        name,
        version (optional),
        url (optional),
        framework (optional)
"""

@dataclass
class DSInfo:
    name: str
    version: Optional[str] = None
    url: Optional[str] = None
    framework: Optional[str] = None

"""Component info represents the metadata of particular design system component.
    Fields:
        name,
        aliases,
        category (optional),
"""

@dataclass
class Component: 
     name: str
     aliases: list[str]
     category: Optional[str] = None
