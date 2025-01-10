from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import locale

# Configuramos la localización en español (español de España o el que desees)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para español de España

app = FastAPI()

# Configuración del CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],  # Solo permite métodos GET y OPTIONS
    allow_headers=["*"],  # Permite todas las cabeceras
)

@app.get("/")
async def root():
    # Obtenemos la fecha actual y la formateamos en español
    today = datetime.now().strftime("%A, %d de %B de %Y")  # Formato: "lunes, 01 de enero de 2025"
    
    return {
        "greeting": "Hello, World!",
        "message": "¡Bienvenido a la API de solo lectura!",
        "date": today  # Fecha de hoy en español
    }
