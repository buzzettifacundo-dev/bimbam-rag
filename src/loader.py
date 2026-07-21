from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import DOCUMENTOS_DIR


def cargar_documentos():

    loader = PyPDFDirectoryLoader(DOCUMENTOS_DIR)

    documentos = loader.load()

    return documentos


def dividir_documentos(documentos):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documentos)

    return chunks