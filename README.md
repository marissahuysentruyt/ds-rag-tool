# ds-rag-tool

Design system comparison tool

## Set up

- Create virtual environment

```bash
python -m venv .venv
```

- Activate it (Mac/Linux)

```bash
source .venv/bin/activate
```

- Or Windows

.venv\Scripts\activate

- Install your dependencies

```bash
pip install -e .
```

## Running Tests

Run the test suite with pytest:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_local_loader.py
```
