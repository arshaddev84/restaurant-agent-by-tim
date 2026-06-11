from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

import os
import pandas as pd

# -------------------------------
# Configuration
# -------------------------------

CSV_FILE = "realistic_restaurant_reviews.csv"
DB_LOCATION = "./chroma_langchain_db"

EMBED_MODEL = "all-minilm:l6-v2"

COLLECTION_NAME = "restaurant_reviews"

TOP_K = 5

# -------------------------------
# Embeddings
# -------------------------------

def create_embeddings():
    return OllamaEmbeddings(model=EMBED_MODEL)

# -------------------------------
# Load CSV
# -------------------------------

def load_reviews(csv_file):
    return pd.read_csv(csv_file)

# -------------------------------
# Convert Dataframe -> Documents
# -------------------------------

def create_documents(df):
    documents = []
    ids = []

    for i, row in df.iterrows():

        document= Document(
            page_content=f"{row['Title']} {row['Review']}",
            metadata={
                "rating": row["Rating"],
                "date": row["Date"]
            },
            id=str(i)
        )

        documents.append(document)
        ids.append(str(i))

    return documents, ids

# -------------------------------
# Create Vector Store
# -------------------------------

def create_vector_store(embeddings):
    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=DB_LOCATION,
        embedding_function=embeddings
    )

# -------------------------------
# Populate Database
# -------------------------------

def populate_database(vector_store):

    if os.path.exists(DB_LOCATION):
        return
    
    print("Creating vector database...")

    df = load_reviews(CSV_FILE)

    documents, ids = create_documents(df)

    vector_store.add_documents(
        documents=documents,
        ids=ids
    )

# -------------------------------
# Create Retriever
# -------------------------------

def create_retriever(vector_store):
    return vector_store.as_retriever(
        search_kwargs={"k": TOP_K}
    )

# ------------------------
# Application Setup
# ------------------------

embeddings = create_embeddings()

vector_store = create_vector_store(embeddings)

populate_database(vector_store)

retriever = create_retriever(vector_store)