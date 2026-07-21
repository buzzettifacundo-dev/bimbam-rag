from dotenv import load_dotenv
import os

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

DOCUMENTOS_DIR = "documentos"
VECTORSTORE_DIR = "vectorstore"