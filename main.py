from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from vector import retriever

# -------------------------------
# Configuration
# -------------------------------

MODEL_NAME = "llama3.2:1b"

TEMPLATE = """
You are an exeprt in answering questions about a pizza restaurant

Relevant reviews:
{reviews}

Question:
{question}
"""

# -------------------------------
# Model Setup
# -------------------------------

def create_model():
    return ChatOllama(model=MODEL_NAME)

def create_chain(model):
    
    prompt = ChatPromptTemplate.from_template(TEMPLATE)

    return prompt | model

# -------------------------------
# Retrieval
# -------------------------------

def retrieve_reviews(question):

    docs = retriever.invoke(question)

    return "\n\n".join(
        doc.page_content for doc in docs
    )

# -------------------------------
# Response Generation
# -------------------------------

def generate_answer(chain, question, reviews):

    result =  chain.invoke({
        "reviews": reviews,
        "question": question
    })

    return result.content.strip()

# -------------------------------
# Main Application
# -------------------------------

def main():

    print("Loading model...")

    model = create_model()

    chain = create_chain(model)

    print("Restaurant Review Assistant Ready!")

    while True:

        print("\n-------------------------------")

        question = input(
            "Ask your question (q to quit): "
        ).strip()

        if question.lower() == "q":
            print("Goodbye!")
            break

        reviews = retrieve_reviews(question)

        result = generate_answer(
            chain,
            question,
            reviews
        )

        print("\nAnswer:")
        print(result)

# -------------------------------
# Entry Point
# -------------------------------

if __name__ == "__main__":
    main()