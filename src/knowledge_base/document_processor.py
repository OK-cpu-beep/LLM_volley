"""
Load text files from knowledge directory and split them into chunks.
"""

import os
from pathlib import Path
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents_from_dir(directory: str) -> List[str]:
    """Read all .txt files in directory and return list of full texts."""
    docs = []
    data_path = Path(directory)
    if not data_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory