from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="milvus-mcp-server",
    version="0.1.0",
    author="Tony Cai",
    author_email="caicloud@gmail.com",
    description="A connector enabling LLMs to interface with Milvus vector databases through Model Context Protocol (MCP)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonycai/milvus-mcp-server",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "milvus-mcp=server:main",
        ],
    },
)