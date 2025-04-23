# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands
- **Run server**: `python server.py`
- **Run with args**: `python server.py --milvus-uri http://localhost:19530 --milvus-token <token> --milvus-db <db_name>`
- **Linting**: `flake8 .` or `pylint .`
- **Type checking**: `mypy .`

## Code Style Guidelines
- **Imports**: Sort imports by standard library, third-party, then local. Group by type.
- **Formatting**: Follow PEP 8 guidelines. Use 4 spaces for indentation.
- **Types**: Use explicit typing for all function parameters and return types.
- **Naming**: Use snake_case for functions/variables, PascalCase for classes.
- **Docstrings**: Use triple quotes with Google-style docstrings for classes and functions.
- **Error Handling**: Always use try/except blocks with specific exception types, raising ValueError with descriptive messages.
- **Async**: Use proper async/await patterns for asynchronous operations.

## Known Issues and Workarounds
- **Milvus Vector Format**: When working with vectors in Milvus collections, use numpy arrays with explicit dtype='float32' when calling ORM methods directly. When using the MilvusClient API, convert vectors to Python lists using vector.tolist().
- **Collection Creation**: Use the ORM API with properly defined FieldSchema objects for reliable collection creation. The primary key field should not use auto_id=True if you're supplying IDs manually.
- **MCP Tool Access**: Note that pymilvus string data types like "INT64" need to be converted to corresponding DataType enum values (DataType.INT64) when passed to the Milvus API.