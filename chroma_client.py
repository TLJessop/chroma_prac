"""
Core functionality for interacting with the Chroma vector database.
Provides functions to add and query text inputs.
"""

import chromadb
import uuid
from typing import Dict, List, Any

# Initialize the Chroma client with persistent storage
client = chromadb.PersistentClient(path="./chromadb")

# Get or create a collection for storing inputs
collection = client.get_or_create_collection(name="input_storage")


def add_input(input_text: str) -> None:
    """
    Add a text input to the Chroma database with a unique ID.
    
    Args:
        input_text: The text to store in the database
    """
    # Generate a unique ID for each document
    unique_id = str(uuid.uuid4())
    collection.upsert(
        documents=[
            input_text
        ],
        ids=[unique_id]
    )
    print(f"Added input with ID: {unique_id}")


def query_input(input_text: str) -> Dict[str, List[Any]]:
    """
    Query the Chroma database for similar texts.
    
    Args:
        input_text: The text to use as a query
        
    Returns:
        Dictionary containing query results with the top 2 matches
    """
    results = collection.query(
        query_texts=[input_text],
        n_results=2
    )
    return results