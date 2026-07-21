import os
import streamlit as st

from langchain_cohere import ChatCohere

from src.config import COHERE_API_KEY
from src.vectorstore import cargar_vectorstore
from src.prompts import construir_prompt


llm = ChatCohere(
    model="command-a-03-2025",
    cohere_api_key=COHERE_API_KEY,
    temperature=0
)


@st.cache_resource(
    show_spinner="⏳ Preparando el asistente, aguarda unos segundos..."
)
def obtener_vectorstore():
    return cargar_vectorstore()


vectorstore = obtener_vectorstore()

historial = []


def preguntar_documentos(pregunta):

    global historial

    try:

        resultados = vectorstore.similarity_search_with_score(
            pregunta,
            k=3
        )

        documentos = [doc for doc, _ in resultados]

        if len(documentos) == 0:

            return (
                "No encontré información sobre ese tema en los documentos disponibles.",
                [],
                False
            )

        contexto = "\n\n".join(
            doc.page_content for doc in documentos
        )

        historial.append(f"Usuario: {pregunta}")

        conversacion = "\n".join(historial[-6:])

        prompt = construir_prompt(
            contexto=contexto,
            pregunta=pregunta,
            historial=conversacion
        )

        respuesta = llm.invoke(prompt)

        texto = respuesta.content

        historial.append(
            f"Asistente: {texto}"
        )

        if "No encontré información" in texto:

            return texto, [], False

        fuentes = []

        for doc in documentos:

            archivo = os.path.basename(
                doc.metadata["source"]
            )

            pagina = doc.metadata["page"] + 1

            fuentes.append(
                {
                    "archivo": archivo,
                    "pagina": pagina,
                    "contenido": doc.page_content
                }
            )

        return texto, fuentes, True

    except Exception:

        return (
            "Lo siento. En este momento ocurrió un inconveniente al consultar la base de conocimiento. Inténtalo nuevamente en unos instantes.",
            [],
            False
        )