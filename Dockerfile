FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment variables
ENV MILVUS_URI=http://localhost:19530
ENV MILVUS_TOKEN=
ENV MILVUS_DB=default

# Expose the MCP server port
EXPOSE 8085

# Run the server
CMD ["python", "server.py"]