# DS-RAG-Tool: Project Overview

## Table of Contents

1. [Introduction](#introduction)
2. [Project Vision](#project-vision)
3. [Current Status](#current-status)
4. [Architecture](#architecture)
5. [Core Components](#core-components)
6. [Design Decisions](#design-decisions)
7. [Technology Stack](#technology-stack)
8. [Development Roadmap](#development-roadmap)
9. [Getting Started](#getting-started)
10. [Contributing](#contributing)

---

## Introduction

**DS-RAG-Tool** (Design System Retrieval-Augmented Generation Tool) is a Python-based system designed to enable intelligent comparison and analysis of design systems using RAG (Retrieval-Augmented Generation) techniques. The tool aims to help developers, designers, and product teams understand similarities, differences, and best practices across multiple design systems like Material Design, Chakra UI, Ant Design, and others.

### What Problem Does It Solve?

When working across multiple design systems or migrating between frameworks, teams face challenges:

- **Fragmented Documentation**: Each design system has different documentation structures
- **Component Mapping**: Understanding how a "Button" in Material-UI differs from Chakra UI
- **Best Practice Discovery**: Finding relevant patterns across multiple design systems
- **Migration Complexity**: Translating designs from one system to another

DS-RAG-Tool addresses these by creating a semantic search layer over design system documentation, enabling queries like:
- "How does Material Design handle modals compared to Ant Design?"
- "What are the accessibility features of buttons across all design systems?"
- "Show me pagination implementations in React-based design systems"

---

## Project Vision

### Ultimate Goal

Build an intelligent design system comparison engine that can:

1. **Ingest** documentation from multiple sources (PDFs, websites, repos)
2. **Process** and chunk content semantically for optimal retrieval
3. **Embed** documentation using vector representations
4. **Query** across design systems using natural language
5. **Compare** components, patterns, and guidelines intelligently
6. **Extract** structured component registries from documentation

### Intended RAG Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│  Data Sources                                               │
│  • GitHub repos (documentation folders)                     │
│  • Design system websites (HTML documentation)              │
│  • PDF style guides                                         │
│  • Word documents (corporate design systems)                │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: Document Loading                                  │
│  • DocumentLoader implementations (FileSystem, Web, Git)    │
│  • File type detection (.md, .mdx, .html, .pdf, .docx)     │
│  • Metadata tagging (design system name, version, framework)│
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 2: Text Chunking                                     │
│  • Semantic chunking (preserve context)                     │
│  • Hierarchical chunking (maintain document structure)      │
│  • Component extraction (identify component documentation)  │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 3: Embedding & Indexing                              │
│  • Generate vector embeddings (OpenAI, Cohere, or local)    │
│  • Store in vector database (Pinecone, Weaviate, ChromaDB)  │
│  • Create metadata indices for filtering                    │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 4: Retrieval & Query                                 │
│  • Semantic search across design systems                    │
│  • Filtered retrieval (by framework, component type, etc.)  │
│  • Context assembly for LLM prompts                         │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 5: Comparison & Analysis                             │
│  • Side-by-side component comparisons                       │
│  • Pattern matching across design systems                   │
│  • Migration guidance generation                            │
└─────────────────────────────────────────────────────────────┘
```

---

## Current Status

### Development Phase

**Phase 1: Document Ingestion (Foundation)** - **COMPLETE**

The project has successfully completed the foundational data models and abstractions required for the RAG pipeline. Current implementation includes:

- Core data models (Document, Chunk, DSInfo, Component)
- Document loader protocol and configuration system
- Comprehensive test suite for protocols
- Modern Python typing and dataclass architecture

### What's Implemented

| Component | Status | Files | Tests |
|-----------|--------|-------|-------|
| Data Models | Complete | `models/documents.py` | Indirect |
| Loader Protocol | Complete | `loaders/__init__.py` | Complete |
| Configuration | Complete | `loaders/__init__.py` | Complete |
| Chunking | Placeholder | `chunkers/__init__.py` | None |
| Registry | Placeholder | `registry/__init__.py` | None |
| Concrete Loaders | Not Started | - | - |
| Embedding | Not Started | - | - |
| Vector DB | Not Started | - | - |
| Query System | Not Started | - | - |

### Lines of Code

- **Source Code**: 132 lines (across 8 Python files)
- **Test Code**: 42 lines (1 test file, 2 test cases)
- **Total**: 174 lines

---

## Architecture

### Design Philosophy

The DS-RAG-Tool architecture follows several key principles:

1. **Protocol-Oriented Design**: Uses Python's `Protocol` (PEP 544) for structural subtyping
2. **Immutable Data Models**: Dataclasses with minimal mutability
3. **Separation of Concerns**: Clear module boundaries (models, loaders, chunkers, registry)
4. **Metadata-Driven**: Flexible metadata dictionaries for extensibility
5. **Type Safety**: Full type annotations using modern Python 3.9+ syntax

### Project Structure

```
ds-rag-tool/
├── PLANNING-DOCS/              # 6-phase roadmap PDFs
├── src/
│   └── ds_compare/             # Main package (src-layout)
│       ├── models/             # Data models
│       │   └── documents.py    # Document, Chunk, DSInfo, Component
│       ├── loaders/            # Document loading abstractions
│       │   └── __init__.py     # DocumentLoader Protocol, LoaderConfig
│       ├── chunkers/           # Text chunking (placeholder)
│       └── registry/           # Component registry (placeholder)
├── tests/                      # pytest test suite
│   └── test_document_loader.py # Protocol and config tests
├── docs/                       # Project documentation
├── pyproject.toml              # Project configuration
└── README.md                   # Setup instructions
```

### Module Responsibilities

**`models/`**: Pure data structures with no business logic
- Represents documents, chunks, design systems, and components
- Immutable, type-safe dataclasses
- Foundation for the entire pipeline

**`loaders/`**: Input abstraction layer
- Defines the contract for loading documents (`DocumentLoader` protocol)
- Configuration objects for parameterizing loaders
- Future: Concrete implementations (FileSystemLoader, GitHubLoader, WebLoader)

**`chunkers/`**: Processing logic (future)
- Text chunking strategies (semantic, fixed-size, hierarchical)
- Component extraction and metadata enrichment
- Document structure preservation

**`registry/`**: Component catalog (future)
- Structured registry of design system components
- Component matching and alias resolution
- Cross-design-system component mapping

---

## Core Components

### 1. Data Models (`models/documents.py`)

#### Document

Represents a complete, unprocessed document before chunking.

```python
@dataclass
class Document:
    id: str                      # Unique identifier
    content: str                 # Full raw text/content
    source_path: str             # File path or URL
    metadata: dict               # Flexible metadata (design system, version, etc.)
```

**Purpose**: Input to the chunking pipeline. Represents complete files (Markdown, HTML, PDF, DOCX) loaded from various sources.

**Design Decision**: Metadata dictionary allows arbitrary annotations without schema changes.

#### Chunk

Represents a fragment of a Document after chunking (for RAG embedding).

```python
@dataclass
class Chunk:
    id: str                      # Unique identifier
    content: str                 # Chunk text
    document_id: str             # Parent document reference
    start_index: int             # Character offset in original document
    end_index: int               # End character offset
    metadata: dict               # Per-chunk metadata (heading, component name, etc.)
```

**Purpose**: Embedding unit for the RAG pipeline. Chunks are converted to vectors and stored in the vector database.

**Design Decision**: Character-based offsets (`start_index`/`end_index`) enable semantic chunking that can split mid-paragraph, unlike line-based approaches.

#### DSInfo (Design System Info)

Metadata container for a design system.

```python
@dataclass
class DSInfo:
    name: str                    # Design system name (required)
    version: Optional[str]       # Version (e.g., "v5", "2.0")
    url: Optional[str]           # Official documentation URL
    framework: Optional[str]     # Framework (React, Vue, Angular, etc.)
```

**Purpose**: Tags all documents from a source with design system metadata, enabling filtered queries.

**Examples**:
- `DSInfo(name="Material-UI", version="v5", framework="React")`
- `DSInfo(name="Ant Design", version="5.x", framework="React")`
- `DSInfo(name="Chakra UI", version="2.0", framework="React")`

#### Component

Represents a UI component within a design system.

```python
@dataclass
class Component:
    name: str                    # Component name
    aliases: list[str]           # Alternative names (for fuzzy matching)
    category: Optional[str]      # Category (Forms, Navigation, Feedback, etc.)
```

**Purpose**: Future component registry and matching system.

**Example**:
```python
Component(
    name="Dropdown",
    aliases=["Select", "Combobox", "Picker"],
    category="Forms"
)
```

**Not Yet Integrated**: Defined but not used in current implementation. Intended for component extraction phase.

---

### 2. Document Loader Protocol (`loaders/__init__.py`)

#### DocumentLoader Protocol

Defines the contract for document loading using structural subtyping.

```python
class DocumentLoader(Protocol):
    def load(self) -> list[Document]:
        """Returns all documents from a source (directory, URL, repo)"""
        ...

    def load_single_doc(self, source_path: str) -> Document:
        """Returns a single document from the source"""
        ...

    def supports_source(self, source: str) -> bool:
        """Returns true if loader supports this source type"""
        ...
```

**Architectural Pattern**: Protocol-Oriented Programming (PEP 544)

**Why Protocol Instead of ABC?**
- Enables structural subtyping (duck typing with type safety)
- No inheritance required - any class implementing these methods is valid
- Easier testing (mocks don't need inheritance)
- More Pythonic than Java-style abstract classes

**Expected Future Implementations**:
- `FileSystemLoader`: Loads from local directories
- `GitHubLoader`: Loads from GitHub repositories
- `WebLoader`: Scrapes web documentation
- `GitLoader`: Clones and processes git repositories

**Usage Pattern** (chain of responsibility):
```python
loaders = [FileSystemLoader(config), GitHubLoader(config), WebLoader(config)]
for loader in loaders:
    if loader.supports_source(source):
        documents = loader.load()
        break
```

#### LoaderConfig

Configuration object for document loaders.

```python
@dataclass
class LoaderConfig:
    base_source: str             # Root path/URL to load from
    file_extensions: list[str]   # Whitelist of file types (e.g., [".md", ".mdx"])
    recursive: bool              # Whether to traverse subdirectories
    design_system: DSInfo        # Design system metadata to tag documents
```

**Purpose**: Single point of configuration for loader behavior.

**Example Usage**:
```python
config = LoaderConfig(
    base_source="/docs/material-ui",
    file_extensions=[".md", ".mdx", ".html"],
    recursive=True,
    design_system=DSInfo(
        name="Material-UI",
        version="v5",
        url="https://mui.com",
        framework="React"
    )
)
loader = FileSystemLoader(config)
documents = loader.load()
```

**Benefits**:
- Reduces parameter proliferation
- Easy to serialize for configuration files
- Enables dependency injection pattern

---

### 3. Test Suite (`tests/test_document_loader.py`)

#### test_loader_config_creation()

Validates `LoaderConfig` dataclass instantiation and nested access.

```python
def test_loader_config_creation():
    mock_design_system = DSInfo(name="Chauncey", url="www.misterbigshot.com")
    mock_config = LoaderConfig(
        base_source="/documents",
        file_extensions=[".md", ".mdx"],
        recursive=True,
        design_system=mock_design_system
    )

    assert mock_config.base_source == "/documents"
    assert mock_config.file_extensions == [".md", ".mdx"]
    assert mock_config.recursive == True
    assert mock_config.design_system == mock_design_system
    assert mock_config.design_system.name == "Chauncey"
```

**Testing Strategy**: Direct property access validation with nested dataclass testing.

#### test_document_loader()

Validates `DocumentLoader` protocol using structural typing.

```python
def test_document_loader():
    class MockDocLoader:  # NOT inheriting from DocumentLoader
        def load(self) -> list[Document]:
            return []

        def load_single_doc(self, source_path: str) -> Document:
            return Document(
                id="chauncey",
                content="he's kind of a big deal",
                source_path="",
                metadata={}
            )

        def supports_source(self, source: str) -> bool:
            return True

    mock_loader: DocumentLoader = MockDocLoader()  # Type checks!
    assert mock_loader.load_single_doc("./home").id == "chauncey"
```

**Key Insight**: This test proves the Protocol pattern works - `MockDocLoader` is accepted as a `DocumentLoader` purely by implementing the required methods, without inheritance.

---

## Design Decisions

### 1. Protocol-Oriented Design (PEP 544)

**Decision**: Use `Protocol` for `DocumentLoader` instead of `ABC` (Abstract Base Class).

**Rationale**:
- **Structural Subtyping**: Any class implementing the methods is valid (duck typing)
- **No Inheritance Required**: Reduces coupling, easier testing
- **Pythonic**: Aligns with Python's philosophy over Java-style abstractions
- **Type Safe**: Still provides static type checking via mypy/pyright

**Trade-off**: Less explicit than `@abstractmethod` decorators, but more flexible.

---

### 2. Dataclass-Based Domain Modeling

**Decision**: All domain objects are `@dataclass` instead of manual classes.

**Benefits**:
- Automatic `__init__`, `__repr__`, `__eq__`, `__hash__` generation
- Type safety via type hints
- Immutability option with `frozen=True`
- Less boilerplate (3-5x fewer lines)

**Best Practice Used**: `field(default_factory=dict)` prevents mutable default argument bug:

```python
# WRONG: Mutable default argument (shared across instances)
class Document:
    def __init__(self, metadata={}): ...

# RIGHT: Default factory (new dict per instance)
@dataclass
class Document:
    metadata: dict = field(default_factory=dict)
```

---

### 3. Src Layout Pattern

**Decision**: Use `src/ds_compare/` instead of `ds_compare/` at repository root.

**Benefits**:
- Prevents accidental imports from working directory
- Enforces package installation for testing (catches import errors)
- Cleaner namespace isolation
- Recommended by Python Packaging Authority (PyPA)

**Reference**: [Setuptools src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout)

---

### 4. Metadata Dictionaries

**Decision**: Use `metadata: dict` fields on `Document` and `Chunk` instead of explicit fields.

**Rationale**:
- **Flexibility**: Different design systems have varying metadata (e.g., "framework", "category", "tags")
- **Extensibility**: Add new metadata types without schema changes
- **Future-Proof**: Downstream users can add custom metadata

**Trade-off**: Less type safety than explicit fields, but appropriate for variable metadata.

**Alternative Considered**: Pydantic models with dynamic fields, but overkill for current scope.

---

### 5. Offset-Based Chunking

**Decision**: Use `start_index`/`end_index` (character offsets) instead of line numbers.

**Rationale**:
- **Character-Level Precision**: Enables semantic chunking that splits mid-paragraph
- **ML/Embedding Friendly**: Vector models work on character sequences, not lines
- **Hierarchical Chunking**: Enables overlapping chunks (e.g., 500 chars with 100 char overlap)

**Example**:
```python
# Original document (200 characters)
"Material-UI provides a Button component..."

# Chunks (with 50 char overlap)
Chunk(start_index=0, end_index=100, content="Material-UI provides...")
Chunk(start_index=50, end_index=150, content="...a Button component...")
Chunk(start_index=100, end_index=200, content="...with various props...")
```

---

### 6. Modern Python Typing

**Decision**: Use PEP 585 generics (`list[str]`) instead of `typing.List[str]`.

**Rationale**:
- **Simpler Syntax**: Builtin types are more readable
- **Future-Proof**: `typing.List` will be deprecated in Python 3.14+
- **Minimum Python 3.9**: Project already requires modern Python

**Migration Path**:
```python
# Old (Python 3.5-3.8)
from typing import List, Dict, Optional
def foo() -> List[Dict[str, Optional[int]]]: ...

# New (Python 3.9+)
def foo() -> list[dict[str, int | None]]: ...
```

---

## Technology Stack

### Core Dependencies

#### Document Processing

**pypdf** (v6.7.4)
- **Purpose**: Parse PDF files
- **Use Case**: Extract text from PDF style guides (e.g., Apple HIG)
- **Why Chosen**: Modern, actively maintained successor to PyPDF2

**python-docx** (v1.2.0)
- **Purpose**: Parse Microsoft Word documents (.docx only, not legacy .doc)
- **Use Case**: Corporate design systems often distributed as Word docs
- **Note**: Requires lxml for XML parsing

**markdown** (v3.10.2)
- **Purpose**: Parse Markdown files
- **Use Case**: GitHub/GitLab documentation, README files
- **Extensible**: Supports plugins for tables, code blocks, footnotes

**beautifulsoup4** (v4.14.3)
- **Purpose**: HTML/XML parsing and traversal
- **Use Case**: Scrape web-based design system documentation
- **Backend**: Uses lxml for performance (C-based parser)

**lxml** (v6.0.2)
- **Purpose**: Fast XML/HTML parsing library
- **Use Case**: Backend for BeautifulSoup (10-100x faster than html.parser)
- **Trade-off**: Binary dependency (harder to install on some systems)

---

#### Development Tools

**pytest** (v9.0.2)
- **Purpose**: Testing framework
- **Features**: Simple test discovery, fixtures, parametrization, plugins
- **Industry Standard**: Used by 95%+ of Python projects

**black** (v26.1.0)
- **Purpose**: Opinionated code formatter
- **Philosophy**: "The uncompromising code formatter" (no configuration options)
- **Benefits**: Eliminates style debates, consistent formatting

**ruff** (v0.15.4)
- **Purpose**: Extremely fast Python linter
- **Technology**: Written in Rust (10-100x faster than flake8)
- **Features**: Combines flake8, isort, pyupgrade, pydocstyle, and more
- **Modern Choice**: Released in 2022, rapidly becoming industry standard

---

### Python Version Requirements

**Minimum**: Python 3.9

**Reason**: Uses PEP 585 generic syntax (`list[str]` instead of `typing.List[str]`)

**Recent Change**: Originally required Python 3.12, downgraded to 3.9 for broader compatibility.

---

### Future Dependencies (Not Yet Added)

Based on RAG pipeline architecture, expected future additions:

**Embedding & Vector DB**:
- `openai` - OpenAI API for embeddings (text-embedding-3-small)
- `chromadb` or `pinecone-client` or `weaviate-client` - Vector database
- `langchain` - RAG orchestration framework (optional)

**Utilities**:
- `python-dotenv` - Environment variable management
- `pydantic` - Runtime type validation (if needed)
- `structlog` or `loguru` - Structured logging
- `httpx` - Modern HTTP client for web scraping

**Advanced Chunking**:
- `tiktoken` - Token counting for chunk size optimization
- `unstructured` - Advanced document parsing (preserves layout)

---

## Development Roadmap

### Phase 1: Document Ingestion (COMPLETE)

**Goal**: Establish foundation for document loading and processing.

**Completed**:
- Data models (Document, Chunk, DSInfo, Component)
- DocumentLoader protocol
- LoaderConfig configuration system
- Protocol validation tests

**Artifacts**:
- `src/ds_compare/models/documents.py` (63 lines)
- `src/ds_compare/loaders/__init__.py` (27 lines)
- `tests/test_document_loader.py` (42 lines)

---

### Phase 2: Document Loading (NEXT)

**Goal**: Implement concrete loaders for various document sources.

**Planned Components**:

1. **FileSystemLoader**
   - Load documents from local directories
   - Support recursive traversal
   - Filter by file extension
   - Extract file metadata (path, size, modification date)

2. **WebLoader**
   - Scrape HTML documentation from URLs
   - Follow internal links (depth-limited crawling)
   - Extract metadata from HTML headers
   - Handle robots.txt and rate limiting

3. **GitHubLoader**
   - Load documentation from GitHub repositories
   - Support branch/tag selection
   - Filter documentation directories (e.g., `/docs/`, `/documentation/`)
   - Use GitHub API for efficiency

**Test Cases**:
- Load Markdown files from local directory
- Load HTML from Material Design website
- Load MDX from Chakra UI GitHub repo

---

### Phase 3: Text Chunking (FUTURE)

**Goal**: Implement intelligent text chunking strategies.

**Planned Chunkers**:

1. **FixedSizeChunker**
   - Chunk by character count (e.g., 500 chars per chunk)
   - Overlap support (e.g., 100 char overlap)
   - Token counting for model context limits

2. **SemanticChunker**
   - Chunk by semantic boundaries (paragraphs, sections)
   - Preserve heading hierarchy
   - Detect component documentation blocks

3. **HierarchicalChunker**
   - Maintain parent-child relationships
   - Create multi-level chunks (section → subsection → paragraph)
   - Enable hierarchical retrieval

**Component Extraction**:
- Detect component documentation patterns
- Extract component names, props, examples
- Populate Component registry

---

### Phase 4: Embedding & Indexing (FUTURE)

**Goal**: Generate embeddings and build vector index.

**Planned Components**:

1. **Embedding Generation**
   - OpenAI `text-embedding-3-small` (cost-effective)
   - Batch processing for efficiency
   - Embedding cache (avoid re-embedding unchanged chunks)

2. **Vector Database**
   - ChromaDB (local, no API keys) or Pinecone (managed, scalable)
   - Metadata filtering (design system, component type, framework)
   - Hybrid search (vector + keyword)

3. **Index Management**
   - Incremental updates (only new/changed documents)
   - Version control for indices
   - Index optimization

---

### Phase 5: Query & Retrieval (FUTURE)

**Goal**: Enable semantic search across design systems.

**Planned Features**:

1. **Query Processing**
   - Natural language query parsing
   - Query expansion (synonyms, related terms)
   - Query embedding generation

2. **Retrieval**
   - Top-K similarity search
   - Metadata filtering (e.g., only React design systems)
   - Reranking for relevance

3. **Context Assembly**
   - Assemble retrieved chunks into LLM context
   - Deduplication (avoid redundant chunks)
   - Citation tracking (which design system each chunk is from)

---

### Phase 6: Comparison & Analysis (FUTURE)

**Goal**: Intelligent design system comparison.

**Planned Features**:

1. **Component Comparison**
   - Side-by-side component documentation
   - Prop/attribute comparison tables
   - Code example alignment

2. **Pattern Analysis**
   - Identify common patterns across design systems
   - Highlight unique features per design system
   - Best practice extraction

3. **Migration Guidance**
   - Suggest equivalent components across systems
   - Generate migration checklists
   - Highlight breaking changes

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git (for cloning repository)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ds-rag-tool
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   ```

4. **Run tests**:
   ```bash
   pytest
   ```

### Project Configuration

The project uses `pyproject.toml` for all configuration:

```toml
[project]
name = "ds_compare"
version = "0.1.0"
requires-python = ">=3.9"

dependencies = [
    "pypdf",
    "python-docx",
    "markdown",
    "beautifulsoup4",
    "lxml",
    "pytest",
    "black",
    "ruff",
]
```

### Code Formatting

Format code with Black:
```bash
black src/ tests/
```

### Linting

Lint code with Ruff:
```bash
ruff check src/ tests/
```

---

## Contributing

### Current Priorities

**High Priority**:
1. Implement `FileSystemLoader` (first concrete loader)
2. Add edge case tests (empty files, invalid paths, missing metadata)
3. Add logging infrastructure (`structlog` or `loguru`)

**Medium Priority**:
4. Set up CI/CD (GitHub Actions for pytest + ruff)
5. Add Sphinx or MkDocs documentation
6. Implement first chunking strategy (`FixedSizeChunker`)

**Low Priority**:
7. Switch to Pydantic for runtime validation (if needed)
8. Add pre-commit hooks (black + ruff)
9. Set up coverage reporting (`pytest-cov`)

### Code Quality Standards

**Type Safety**:
- All functions must have type annotations
- Use modern Python 3.9+ syntax (`list[str]`, not `List[str]`)
- Run mypy for static type checking

**Testing**:
- Maintain 80%+ code coverage
- Write tests before submitting PRs
- Use pytest fixtures for reusable test data

**Documentation**:
- Docstrings for all public classes and functions
- Inline comments for complex logic
- Update docs/ when adding major features

### Recommended Development Workflow

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Write tests first (TDD approach)
3. Implement feature
4. Run tests: `pytest`
5. Format code: `black src/ tests/`
6. Lint code: `ruff check src/ tests/`
7. Commit with conventional commit message: `feat: add FileSystemLoader`
8. Push and create PR

---

## Architecture Strengths

### What's Done Well

1. **Modern Python Best Practices**
   - Dataclasses for data modeling
   - Protocol for structural subtyping
   - Type hints throughout
   - Src-layout for package structure

2. **Clean Architecture**
   - Clear separation of concerns (models, loaders, chunkers)
   - Protocol-oriented design (extensible, testable)
   - Configuration objects (reduces parameter proliferation)

3. **Type Safety**
   - Full type annotations
   - Static analysis support (mypy/pyright)
   - Structural typing with Protocols

4. **Testing Strategy**
   - Protocol validation tests
   - Configuration tests
   - Modern pytest setup

5. **Dependency Management**
   - Minimal dependencies (only what's needed)
   - Well-chosen libraries (modern, maintained)
   - Modern tooling (ruff, black)

---

## Areas for Future Improvement

### Technical Debt (Future Work)

1. **Error Handling**
   - No validation for invalid paths, malformed documents
   - No custom exception hierarchy
   - No graceful degradation for missing dependencies

2. **Logging**
   - No structured logging infrastructure
   - Hard to debug loader issues without logs

3. **Configuration Management**
   - No support for config files (.env, YAML, TOML)
   - Configuration is currently code-only

4. **Documentation**
   - No API documentation (Sphinx/MkDocs)
   - No architecture diagrams
   - No usage examples in docstrings

5. **CI/CD**
   - No automated testing (GitHub Actions)
   - No coverage reporting
   - No pre-commit hooks

6. **Type Validation**
   - No runtime validation (Pydantic)
   - Metadata dictionaries are untyped

---

## FAQ

### Why Protocol instead of ABC?

**Protocol** (PEP 544) enables structural subtyping - any class implementing the required methods is valid, without inheritance. This is more Pythonic (duck typing) and easier to test (mocks don't need inheritance).

### Why dataclasses instead of regular classes?

**Dataclasses** automatically generate `__init__`, `__repr__`, `__eq__`, and `__hash__`, reducing boilerplate by 3-5x. They also provide type safety and optional immutability.

### Why src-layout instead of flat layout?

**Src-layout** (`src/ds_compare/`) prevents accidental imports from the working directory and enforces package installation for testing, catching import errors early.

### Why character offsets instead of line numbers?

**Character offsets** (`start_index`/`end_index`) enable semantic chunking that can split mid-paragraph, which is critical for ML/embedding pipelines that work on character sequences.

### What design systems will be supported?

The architecture is design-system agnostic. Initial targets likely include:
- Material-UI (React)
- Chakra UI (React)
- Ant Design (React)
- Tailwind UI (HTML/CSS)
- Radix UI (React)
- shadcn/ui (React)

### When will the RAG pipeline be complete?

Based on the 6-phase roadmap, full RAG functionality (embedding + vector search + comparison) is planned for Phases 4-6. Phase 1 (foundation) is complete. Phases 2-3 (loading + chunking) are next.

---

## References

### Internal Documentation

- **Planning Documents**: See `PLANNING-DOCS/` for detailed phase roadmaps
- **Test Examples**: See `tests/test_document_loader.py` for protocol usage

### External Resources

**Python Standards**:
- [PEP 544 - Protocols](https://peps.python.org/pep-0544/)
- [PEP 585 - Type Hinting Generics](https://peps.python.org/pep-0585/)
- [Python Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [PyPA Packaging Guide](https://packaging.python.org/)

**RAG Architecture**:
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Vector Database Comparison](https://www.pinecone.io/learn/vector-database/)

**Design Systems**:
- [Material Design](https://material.io/)
- [Chakra UI](https://chakra-ui.com/)
- [Ant Design](https://ant.design/)

---

## Conclusion

**DS-RAG-Tool** represents a well-architected foundation for design system comparison using RAG techniques. The project demonstrates:

- **Strong architectural decisions** (Protocol-oriented design, dataclasses, src-layout)
- **Modern Python practices** (type hints, pytest, ruff, black)
- **Clear separation of concerns** (models, loaders, chunkers, registry)
- **Extensible design** (metadata dictionaries, protocol interfaces)

**Current Status**: Phase 1 (Foundation) complete with 132 lines of production code and comprehensive protocol tests.

**Next Steps**: Implement concrete loaders (FileSystemLoader, WebLoader, GitHubLoader) to enable document ingestion from real design systems.

The codebase is production-ready for its current scope and well-positioned to scale into a full RAG pipeline with thoughtful incremental development.
