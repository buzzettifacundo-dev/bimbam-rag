# 🛒 BimBam Buy - Asistente Inteligente RAG

Asistente inteligente desarrollado con **LangChain**, **FAISS**, **Cohere** y **Streamlit** para responder consultas utilizando exclusivamente la información contenida en documentos PDF de la empresa.

## 🌐 Aplicación

https://bimbam-rag-lr8wn3odu6ov8ddbn3bngq.streamlit.app/

---

## 🚀 Tecnologías utilizadas

- Python
- Streamlit
- LangChain
- Cohere
- FAISS
- Hugging Face Embeddings
- PyPDF

---

## 📷 Captura

![Demo](imagenes/demo.png)

---

## ❓ Ejemplos de preguntas

- ¿Cómo solicito un reembolso?
- ¿Cuáles son los medios de pago?
- ¿Cómo funciona la garantía?
- ¿Cuánto demora un envío?
- ¿Cómo realizo una devolución?

---

## 💬 Ejemplos de respuestas

### Pregunta

> ¿Cómo solicito un reembolso?

### Respuesta

El cliente debe solicitar el reembolso desde su cuenta o comunicándose con el servicio de atención al cliente, siguiendo las condiciones establecidas en la política de devoluciones.

---

### Pregunta

> ¿Cuáles son los medios de pago?

### Respuesta

BimBam Buy acepta tarjetas de crédito, tarjetas de débito y otros medios de pago electrónicos indicados en sus políticas.

---

## 🎥 Video demostración

Agregar aquí el enlace al video.

Video completo mostrando el funcionamiento del asistente, desde la carga de la aplicación hasta la resolución de consultas utilizando la base documental.

https://youtu.be/gePjii4wkUI

---

## ▶️ Ejecutar localmente

```bash
git clone https://github.com/TU_USUARIO/bimbam-rag.git

cd bimbam-rag

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 📂 Estructura

```
bimbam_rag/
│
├── documentos/
├── src/
├── vectorstore/
├── imagenes/
├── app.py
├── crear_vectorstore.py
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Autor

Facundo Buzzetti
