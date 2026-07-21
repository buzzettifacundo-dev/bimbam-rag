from src.loader import cargar_documentos
from src.loader import dividir_documentos

from src.vectorstore import crear_vectorstore
from src.vectorstore import guardar_vectorstore

documentos = cargar_documentos()

chunks = dividir_documentos(documentos)

print(f"Chunks: {len(chunks)}")

vectorstore = crear_vectorstore(chunks)

guardar_vectorstore(vectorstore)

print("Vectorstore guardado correctamente.")