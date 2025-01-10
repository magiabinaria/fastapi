from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configuración del CORS para permitir solo lectura desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],  # Solo permite métodos GET y OPTIONS (lectura)
    allow_headers=["*"],  # Permite todas las cabeceras
)

@app.get("/")
async def root():
    # Obtener la fecha actual en formato ISO 8601: YYYY-MM-DD
    fecha_iso = datetime.now().strftime("%Y-%m-%d")  # Formato: 2025-01-01
    
    return {
        "greeting": "Hello, World!",
        "message": "¡Bienvenido a la API de solo lectura!",
        "date": fecha_iso  # Fecha en formato internacional
    }

@app.get("/holamundo")
async def hola_mundo():
    return {"message": "¡Hola Mundo!"}
