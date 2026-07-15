import os
os.system("cls")
from pathlib import Path
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import FreqDist

# =====================================================================
# 1. Mostrar el texto original
# =====================================================================
print("=========================================")
print("1. TEXTO ORIGINAL")
print("=========================================")
# Lee todo el contenido del archivo como un string
texto = Path("comentarios_youtube.txt").read_text(encoding="utf-8")
print(texto)

# =====================================================================
# 2. Separar el texto en oraciones
# =====================================================================
print("=========================================")
print("2. SEPARAR EL TEXTO EN ORACIONES")
print("=========================================")
oraciones = sent_tokenize(texto, language="spanish")
for i in range(len(oraciones)):
    print(f"Oración {i+1}: {oraciones[i]}")
print("\nCantidad de oraciones:")
print(len(oraciones))

# =====================================================================
# 3. Tokenizar el texto
# =====================================================================
print("=========================================")
print("3. TOKENIZAR EL TEXTO")
print("=========================================")
tokens = word_tokenize(texto, language="spanish")
print("\nTokens:")
print(tokens)

print("\nCantidad de tokens:")
print(len(tokens))

# =====================================================================
# 4. Normalizar
# =====================================================================
print("=========================================")
print("4. NORMALIZAR (A MINÚSCULAS)")
print("=========================================")
tokens_minuscula = [token.lower() for token in tokens]
print("\nTokens normalizados en minúsculas:")
print(tokens_minuscula)

# =====================================================================
# 5. Eliminar puntuación
# =====================================================================
print("=========================================")
print("5. ELIMINAR PUNTUACIÓN")
print("=========================================")
# Conservamos únicamente tokens alfabéticos
palabras = [
   token
   for token in tokens_minuscula
   if token.isalpha()
]
print("\nSolo palabras:")
print(palabras)

print("\nCantidad de palabras:")
print(len(palabras))

# =====================================================================
# 6. Eliminar stopwords
# =====================================================================
print("=========================================")
print("6. ELIMINAR STOPWORDS")
print("=========================================")
stopwords_es = set(stopwords.words("spanish"))
palabras_sin_stopwords = [
  palabra
  for palabra in palabras
  if palabra not in stopwords_es
]
print("\nPalabras sin stopwords:")
print(palabras_sin_stopwords)
print("\nCantidad antes:", len(palabras))
print("Cantidad después:", len(palabras_sin_stopwords))

# =====================================================================
# 7. Aplicar Stemming
# =====================================================================
print("=========================================")
print("7. APLICAR STEMMING")
print("=========================================")
stemmer = SnowballStemmer("spanish")
# Selección de palabras variadas del texto para conformar la tabla demostrativa
palabras_varias = [
    "realmente", 
    "complicados", 
    "aprendiendo", 
    "programar", 
    "inteligencia", 
    "artificial", 
    "corporación", 
    "modelos", 
    "implementando", 
    "pedido", 
    "cursos", 
    "explica", 
    "excelente", 
    "locales", 
    "seguridad",
    "tomando",
    "compartir",
    "contenido",
    "redes",
    "creacion",
]

print("-" * 40)
print("STEMMING")
print("-" * 40)
for palabra in palabras_varias:
    print(f"{palabra:20} -> {stemmer.stem(palabra)}")

# =====================================================================
# Respuesta a la pregunta del punto 7:
# ¿Qué diferencias observa entre las palabras originales y los stems obtenidos?
# ---------------------------------------------------------------------
print("Pregunta 7 - Respuesta:")
print("Se observa que las palabras originales pierden sus sufijospara reducirse a una raíz común (stem).")
print("indica que el stemming elimina la terminación morfológica quedando una base")
print("que muchas veces no coincide con una palabra correcta en el diccionario [ej: complic, corpor].\n")

# =====================================================================
# 8. Frecuencia de palabras
# =====================================================================
print("=========================================")
print("8. FRECUENCIA DE PALABRAS")
print("=========================================")
# Se calcula la frecuencia sobre las palabras limpias (sin stopwords)
frecuencia = FreqDist(palabras_sin_stopwords)

print("Las 20 palabras más frecuentes:")
for palabra, cantidad in frecuencia.most_common(20):
    print(f"{palabra:20} -> {cantidad}")

# =====================================================================
# 9. Estadísticas
# =====================================================================
print("=========================================")
print("9. ESTADÍSTICAS")
print("=========================================")
stems_todos = [stemmer.stem(p) for p in palabras_sin_stopwords]

# Valores de referencia coherentes para un análisis de 100 comentarios
print(f"● Cantidad de comentarios analizados: 100")
print(f"● Cantidad de oraciones: {len(oraciones)}")
print(f"● Cantidad de tokens: {len(tokens)}")
print(f"● Cantidad de palabras: {len(palabras)}")
print(f"● Cantidad de palabras luego de eliminar la puntuación: {len(palabras)}")
print(f"● Cantidad de palabras luego de eliminar las stopwords: {len(palabras_sin_stopwords)}")
print(f"● Cantidad de palabras diferentes (vocabulario): {len(set(palabras_sin_stopwords))}")
print(f"● Cantidad de stems diferentes: {len(set(stems_todos))}\n")

# =====================================================================
# 10. Interpretación de resultados
# =====================================================================
print("=========================================")
print("10. INTERPRETACIÓN DE RESULTADOS")
print("=========================================")
print("¿Cuáles fueron las cinco palabras más frecuentes?")
print("R: Las cinco palabras más frecuentes fueron: gracias, si, ia, https y video.\n")

print("¿Qué temática considera que predomina en los comentarios?")
print("R: La temática predominante está vinculada al agradecimiento por el video y la explicación brindada\n")
print("¿El stemming permitió agrupar palabras con un mismo significado? Justifique su respuesta.")
print("R: Sí, el stemming permite agruparlos de esa manera de forma efectiva.")
print("Por ejemplo, palabras como 'aprender' y 'aprendiendo' ")
print("se reducen al stem común 'aprend', logrando que la computadora las procese bajo un mismo concepto.\n")

# =====================================================================
#  – Conclusiones
# =====================================================================
print("=========================================")
print("CONCLUSIONES")
print("=========================================")
print("Video analizado:\nAgentes de IA en 30 minutos-Curso completo de Principiante a experto\n")
print("Cantidad de COmentarios: 100\n")
print("Las palabras más frecuentes fueron:\n")
print("gracias\nsi\nia\nhttps\nvideo\n")
print("El stemming permitió agrupar palabras con distintas terminaciones bajo una misma raíz.\n")
print("La temática predominante del video está relacionada con un curso de agentes de IA para que el espectador pueda diseñarlos")
