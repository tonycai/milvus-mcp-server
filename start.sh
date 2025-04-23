#!/bin/bash

# Load environment variables if .env file exists
if [ -f .env ]; then
    source .env
fi

# Start the Milvus MCP server with environment variables or default values
python server.py \
    --milvus-uri "${MILVUS_URI:-http://localhost:19530}" \
    --milvus-token "${MILVUS_TOKEN:-}" \
    --milvus-db "${MILVUS_DB:-default}"

echo "Milvus MCP Server started."