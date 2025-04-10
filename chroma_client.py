import chromadb

client = chromadb.PersistentClient(path="./chromadb")

collection = client.get_or_create_collection(name="input_storage")

def add_input(input_text: str):
    collection.upsert(
    documents=[
        input_text
    ],
    ids=["id1"]
)

def query_input(input_text: str):
    return collection.query([input_text])