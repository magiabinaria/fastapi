import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from dotenv import load_dotenv  # Importamos dotenv para cargar variables locales

# Carga las variables del archivo .env (solo si existe, para entorno local)
load_dotenv()

# Definir la versión de la API
API_VERSION = "v1"

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
    hello = os.getenv("HELLO", "default_hello_value")  # Valor predeterminado si no está configurado
    hola = os.getenv("HOLA", "default_hola_value")    # Valor predeterminado si no está configurado

    # Obtener la fecha actual en formato ISO 8601: YYYY-MM-DD
    fecha_iso = datetime.now().strftime("%Y-%m-%d")
    
    return {
        "version": API_VERSION,  # Devuelve la versión de la API
        "greeting": "Hello, World!",
        "message": "¡Bienvenido a la API de solo lectura!",
        "date": fecha_iso,
        "hello": hello,  # Mostrar el valor de la variable HELLO
        "hola": hola     # Mostrar el valor de la variable HOLA
    }

@app.get("/holamundo")
async def hola_mundo():
    return {
        "version": API_VERSION,  # Devuelve la versión de la API
        "message": "¡Hola, Mundo we!"
    }

# Depuración (solo para desarrollo)
@app.get("/debug")
async def debug_env():
    # Imprime todas las variables de entorno disponibles (para depurar)
    env_vars = dict(os.environ)
    return {
        "version": API_VERSION,  # Devuelve la versión de la API
        "environment_variables": env_vars
    }
