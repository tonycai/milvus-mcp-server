# Milvus MCP Server

A connector enabling Large Language Models to interface with Milvus vector databases through Anthropic's Model Context Protocol (MCP).

## Overview

This server implements Anthropic's Model Context Protocol (MCP), allowing AI assistants to directly query and manage vector databases in Milvus. It provides tools for vector search, text search, and collection management.

## Features

- **Vector Similarity Search**: Find similar vectors using various distance metrics (COSINE, L2, IP)
- **Full-Text Search**: Perform text searches across collections
- **Collection Management**: Create, load, release, and query collections
- **Data Manipulation**: Insert, delete, and update vector data
- **Database Operations**: List and switch between databases

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd mcp-server-milvus
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your environment:
   ```bash
   cp example.env .env
   # Edit .env with your Milvus connection details
   ```

## Usage

### Starting the Server

```bash
python server.py --milvus-uri http://localhost:19530 --milvus-token <token> --milvus-db <db_name>
```

Or use environment variables defined in `.env`.

### Available MCP Tools

- `milvus_text_search`: Search for documents using full text search
- `milvus_list_collections`: List all collections in the database
- `milvus_query`: Query collection using filter expressions
- `milvus_vector_search`: Perform vector similarity search
- `milvus_create_collection`: Create a new collection with specified schema
- `milvus_insert_data`: Insert data into a collection
- `milvus_delete_entities`: Delete entities from a collection
- `milvus_load_collection`: Load a collection into memory
- `milvus_release_collection`: Release a collection from memory
- `milvus_list_databases`: List all databases in the Milvus instance
- `milvus_use_database`: Switch to a different database

## Data Format

### Collection Schema Format

When creating a collection, use this schema format:

```python
{
    "dimension": 128,                 # Vector dimension
    "primary_field": "id",            # Primary key field name
    "id_type": "INT64",               # Primary key data type (will be converted to DataType.INT64)
    "vector_field": "vector",         # Vector field name
    "metric_type": "COSINE",          # Distance metric
    "auto_id": True,                  # Auto-generate IDs
    "enable_dynamic_field": True,     # Enable dynamic fields
    "other_fields": [                 # Additional fields
        {
            "name": "description",
            "type": "VARCHAR",
            "max_length": 65535
        }
    ]
}
```

### Vector Data Format

When inserting vectors:

```python
# Insert data
data = {
    "vector": [[0.1, 0.2, ...], [0.3, 0.4, ...], ...],  # List of vectors
    "description": ["First item", "Second item", ...]    # Optional field values
}
```

## Known Issues and Workarounds

See CLAUDE.md for known issues and best practices when working with this codebase.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.