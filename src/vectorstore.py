from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from src.config import VECTORSTORE_DIR


def crear_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def crear_vectorstore(chunks):

    embeddings = crear_embeddings()

    return FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )


def guardar_vectorstore(vectorstore):

    vectorstore.save_local(VECTORSTORE_DIR)


def cargar_vectorstore():

    embeddings = crear_embeddings()

    return FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )