# nltk_acosta_jose_RiosM_Vanesa-
Trabajo Práctico Integrador – Procesamiento de Lenguaje Natural con NLTK
Integrantes: Acosta José Luis - Rios Morinigo Vanesa
Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial

Objetivo del Trabajo: Analizar comentarios de un video de YouTube utilizando NLTK.
URL del video analizado: https://www.youtube.com/watch?v=nU4aONpAK0g
Cantidad de comentarios descargados: 100
Bibliotecas utilizadas: nltk; youtube-comment-downloader

Instrucciones para ejecutar el programa
1.	Clonar el repositorio:
2.	git clone [URL de este repositorio]
3.	cd [nombre del repositorio]
4.	Crear un entorno virtual (opcional pero recomendado):
5.	python -m venv venv
6.	venv\Scripts\activate        # Windows
7.	source venv/bin/activate     # Linux / Mac
8.	Instalar las dependencias:
9.	pip install nltk youtube-comment-downloader
10.	Descargar los recursos de NLTK (solo la primera vez):
11.	import nltk
12.	nltk.download("punkt")
13.	nltk.download("punkt_tab")
14.	nltk.download("stopwords")
15.	Editar descargar_comentarios.py y reemplazar VIDEO_URL por la URL del video elegido. Luego ejecutar:
16.	python descargar_comentarios.py
Esto genera el archivo comentarios_youtube.txt.
17.	Ejecutar el análisis:
18.	python analizar_comentarios.py
Esto muestra en consola todo el procesamiento (tokenización, normalización, stopwords, stemming, frecuencias, estadísticas y conclusiones).
