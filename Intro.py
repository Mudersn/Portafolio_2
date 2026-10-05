import streamlit as st
from PIL import Image
st.title("Aplicaciones del portafolio 2 .")

with st.sidebar:
  st.subheader("Aplicaciones para el portafolio 2.")
  parrafo = (
    "En estas sesiones aprendimos diferentes técnicas de análisis de datos aplicadas a problemas reales.",
    "Exploramos la visualización de datos, storytelling y PCA para entender mejor el consumo energético. También trabajamos" ,
    "con el algoritmo KNN, una herramienta sencilla pero muy útil para clasificar información, como la fertilidad de los suelos, ",
    "además de conocer sus aplicaciones en recomendadores, salud, agricultura y detección de anomalías.",
    "También vimos cómo pasar de la regresión lineal a la regresión logística para predecir categorías en lugar de valores numéricos. Por otra parte, utilizamos tecnologías IoT para capturar y procesar datos provenientes de sensores,",
    "fortaleciendo el trabajo con datos reales.",
    "Finalmente, estudiamos series de tiempo y modelos predictivos como ARIMA, SARIMA y Holt-Winters para analizar y pronosticar variables como la calidad del aire. Esto nos permitió comprender cómo usar datos históricos para identificar tendencias,",
    "nticipar comportamientos futuros y apoyar la toma de decisiones basadas en datos."
  )
  st.write(parrafo)

url_ia="https://portafolio-2.streamlit.app/"
st.subheader("En el siguiente enlace puedes encontrar una paginas acerca de diferentes aplicaciones.")
st.write(f"Enlace para app de tremas diversos: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("cercania entre frutas")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicacione para encontra la cercania entre frutas") 
 url = "https://fruit-app.streamlit.app/"
 st.write(f"cercania: [Enlace]({url})")

 st.subheader("dectector de anomalias")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan las anomalias en una alarma que se dispara con una condición fija que tú defines.") 
 url = "https://dectectoranomaly-bgxq2qlvhgxjcv3kqecbxw.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("graficos de niveles rios y quebradas")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos los niveles de inudacion que pueden cojer los rios y quebradas de colombia por sensores.") 
 url = "https://marcopolo.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


