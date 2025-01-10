import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configuración del CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],  # Solo permite métodos GET y OPTIONS (lectura)
    allow_headers=["*"],  # Permite todas las cabeceras
)

@app.get("/")
async def root():
    # Acceder a las variables de entorno HELLO y HOLA
    hello = os.getenv("HELLO", "default_hello_value")  # Valor predeterminado por si no está configurado
    hola = os.getenv("HOLA", "default_hola_value")    # Valor predeterminado por si no está configurado

    # Obtener la fecha actual en formato ISO 8601: YYYY-MM-DD
    fecha_iso = datetime.now().strftime("%Y-%m-%d")
    
    return {
        "greeting": "Hello, World!",
        "message": "¡Bienvenido a la API de solo lectura!",
        "date": fecha_iso,
        "hello": hello,  # Mostrar el valor de la variable HELLO
        "hola": hola     # Mostrar el valor de la variable HOLA
    }

@app.get("/holamundo")
async def hola_mundo():
    return {"message": "¡Hola, Mundo we!"}
