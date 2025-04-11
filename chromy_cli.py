"""
CLI interface for interacting with the Chroma database.
"""
from typing import Dict, List, Any
import chroma_client

def display_results(results: Dict[str, List[Any]]) -> None:
    """
    Display query results in a readable format.
    
    Args:
        results: The results dictionary from query_input
    """
    if not results["documents"][0]:
        print("No matching documents found.")
        return
        
    print("\nQuery Results:")
    print("-" * 40)
    
    for i, (doc, id, distance) in enumerate(zip(
            results["documents"][0], 
            results["ids"][0],
            results["distances"][0]
        )):
        print(f"Result {i+1}:")
        print(f"Document: {doc}")
        print(f"ID: {id}")
        print(f"Distance: {distance:.4f}")
        print("-" * 40)


def run_cli() -> None:
    """
    Run the command-line interface for interacting with the Chroma database.
    The CLI runs until the user types 'quit'.
    
    Supports inline arguments with commands:
    - 'add text' - directly adds the text to the database
    - 'query text' - directly queries for the text
    - 'quit' - exits the CLI
    """
    print("Welcome to Chroma CLI")
    print("Type 'add <text>' to add input, 'query <text>' to search, or 'quit' to exit")
    print("Examples: 'add dog' or 'query pet'")
    
    while True:
        user_input = input("\nCommand (add/query/quit): ").strip()
        
        # Split the input into command and arguments
        parts = user_input.split(maxsplit=1)
        command = parts[0].lower() if parts else ""
        args = parts[1] if len(parts) > 1 else ""
        
        if command == "quit":
            print("Exiting Chroma CLI. Goodbye!")
            break
            
        elif command == "add":
            if args:
                # Use the provided argument as the text to add
                chroma_client.add_input(args)
            else:
                # If no argument was provided, prompt for input
                text = input("Enter text to add: ")
                if text:
                    chroma_client.add_input(text)
                else:
                    print("Empty input not added.")
                
        elif command == "query":
            if args:
                # Use the provided argument as the query
                results = chroma_client.query_input(args)
                display_results(results)
            else:
                # If no argument was provided, prompt for input
                query = input("Enter search query: ")
                if query:
                    results = chroma_client.query_input(query)
                    display_results(results)
                else:
                    print("Empty query not processed.")
                
        else:
            print("Unknown command. Available commands: add <text>, query <text>, quit")


if __name__ == "__main__":
    run_cli()
