import streamlit as st

from src.rag import preguntar_documentos


st.set_page_config(
    page_title="BimBam Buy",
    page_icon="🛒",
    layout="wide"
)


# ==================================
# Sidebar
# ==================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/shopping-cart.png",
        width=80
    )

    st.title("BimBam Buy")

    st.caption("Asistente Inteligente")

    st.divider()

    st.write(
        f"💬 Mensajes: {len(st.session_state.get('mensajes', []))}"
    )

    st.divider()

    if st.button(
        "🗑 Nueva conversación",
        use_container_width=True
    ):

        st.session_state.mensajes = []

        st.rerun()


# ==================================
# Pantalla principal
# ==================================

st.title("🛒 Asistente Inteligente de BimBam Buy")

st.markdown(
    """
Consulta políticas de:

- 📦 Envíos
- 💳 Pagos
- 🔄 Cambios
- 💰 Reembolsos
- 🛡 Garantías
"""
)

st.divider()

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for mensaje in st.session_state.mensajes:

    with st.chat_message(
        mensaje["role"]
    ):

        st.markdown(
            mensaje["content"]
        )

pregunta = st.chat_input(
    "Escribe tu consulta..."
)

if pregunta:

    st.session_state.mensajes.append(
        {
            "role": "user",
            "content": pregunta
        }
    )

    with st.chat_message("user"):

        st.markdown(pregunta)

    with st.spinner("Buscando información..."):

        respuesta, fuentes, encontrada = preguntar_documentos(
            pregunta
        )

    with st.chat_message("assistant"):

        if encontrada:

            st.success("Información encontrada en la documentación.")

            st.markdown(respuesta)

        else:

            st.warning(respuesta)

        if fuentes:

            st.divider()

            st.markdown("### 📚 Documentos consultados")

            for fuente in fuentes:

                with st.expander(
                    f"📄 {fuente['archivo']} (Página {fuente['pagina']})"
                ):

                    st.write(
                        fuente["contenido"]
                    )

    texto_guardado = respuesta

    if fuentes:

        texto_guardado += "\n\nFuentes:\n"

        for fuente in fuentes:

            texto_guardado += (
                f"\n• {fuente['archivo']} - Página {fuente['pagina']}"
            )

    st.session_state.mensajes.append(
        {
            "role": "assistant",
            "content": texto_guardado
        }
    )

st.divider()

st.caption(
    "BimBam Buy • Asistente Inteligente • Versión 1.0"
)