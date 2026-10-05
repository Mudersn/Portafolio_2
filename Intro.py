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
 image = Image.open('El_coco.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicacione para encontra la cercania entre frutas") 
 url = "https://fruit-app.streamlit.app/"
 st.write(f"cercania: [Enlace]({url})")

 st.subheader("dectector de anomalias")
 image = Image.open('visor_de_anomalias.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan las anomalias en una alarma que se dispara con una condición fija que tú defines.") 
 url = "https://dectectoranomaly-bgxq2qlvhgxjcv3kqecbxw.streamlit.app/"
 st.write(f"Dectector: [Enlace]({url})")

 st.subheader("graficos de niveles rios y quebradas")
 image = Image.open('rios_y_quebradas.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos los niveles de inudacion que pueden cojer los rios y quebradas de colombia por sensores.") 
 url = "https://marcopolo.streamlit.app/"
 st.write(f"Niveles: [Enlace]({url})")

with col2: 
 st.subheader("Series de Tiempo Sensor IoT interactivo")
 image = Image.open('sensortemp.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa sensores para calcular la temperatura de una serie de tiempo simulada.") 
 url = "https://seriestempo-jkdnyxqnwdvxlwvpljnuzn.streamlit.app//"
 st.write(f"Sensores: [Enlace]({url})")

 st.subheader("dataset preparado")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos Antes de construir cualquier modelo o método computacional, es necesario entender, limpiar y estructurar los datos disponibles. Esta aplicación acompaña el notebook del módulo y permite experimentar en vivo con cada concepto usando un dataset sintético de sensores IoT.") 
 url = "https://datapreparet-pa4yxvx6wpeg9kkiexqk54.streamlit.app/"
 st.write(f"Dataset: [Enlace]({url})")

 st.subheader("probabilidad de lluvia")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos proyeciones para la probabilidad de que llueeva no moviendo diferente datos.") 
 url = "https://regresionlog.streamlit.app/"
 st.write(f"Lluvia: [Enlace]({url})")


with col3: 
 st.subheader("evaluacion de metricas de regrecion")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación La regresión permite predecir valores numéricos a partir de datos históricos. Esta app recorre, de forma interactiva, las piezas que componen un modelo de regresión: el modelo, la función de costo, el gradiente, el algoritmo de aprendizaje y las métricas para evaluar qué tan bien predice. Todo con datos reales de vivienda en California.") 
 url = "https://regrecionapp.streamlit.app/"
 st.write(f"Regrecion: [Enlace]({url})")

 st.subheader("Explora KNN con datos del suelo")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de explorar el KNN Datos abiertos del Laboratorio de Química y Física de Suelos de AGROSAVIA") 
 url = "https://fertiart-n9kzchy8k9nug9zb2lcjhu.streamlit.app/"
 st.write(f"KNN: [Enlace]({url})")
 
 st.subheader("Gradiente Interactivo")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como explora en vivo cómo la tasa de aprendizaje el punto inicial que afectan la convergencia del descenso del gradiente.") 
 url = "https://gradiente-kp3sfhxqfoakl5neebbe9v.streamlit.app/"
 st.write(f"Gradiante: [Enlace]({url})")


