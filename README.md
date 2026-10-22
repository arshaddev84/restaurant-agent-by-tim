# RestaurantAgentByTim

## Contributions Made
```text
* Refactored code into modular functions
* Updated deprecated LangChain imports
* Improved readability and maintainability
* Added reusable configuration constants
* Improved vector database initialization flow
```

## Restaurant Review RAG Application
```text
A simple Retrieval-Augmented Generation (RAG) application built with:

* LangChain
* Ollama
* ChromaDB
* Local LLMs

This project allows users to ask questions about restaurant reviews using semantic search and local language models.
```

## Features
```text
* Local embeddings using Ollama
* Chroma vector database
* Semantic review retrieval
* Modularized project structure
* Updated LangChain package imports
* Compatible with modern LangChain ecosystem
```

## Technologies Used
```text
* Python
* LangChain
* Ollama
* ChromaDB
* Pandas
```

## Project Structure
```text
project/
│
├── main.py
├── vector.py
├── realistic_restaurant_reviews.csv
└── chroma_langchain_db/
```

## Setup
```bash
Install dependencies:
pip install -U langchain langchain-core langchain-ollama langchain-chroma pandas

Install Ollama models:
ollama pull llama3.2:1b
ollama pull all-minilm:l6-v2

Run the application:
python main.py
```

## Credits
Original tutorial/project by Tim Ruscica.
