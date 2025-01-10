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

# Diccionario para traducir los días y meses al español
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

@app.get("/")
async def root():
    # Obtener la fecha y formatearla manualmente
    hoy = datetime.now()
    dia_semana = dias_semana[hoy.weekday()]  # Obtener el día de la semana (0: lunes, 6: domingo)
    mes = meses[hoy.month - 1]  # Obtener el mes (1: enero, 12: diciembre)
    fecha = f"{dia_semana}, {hoy.day} de {mes} de {hoy.year}"  # Formato: lunes, 1 de enero de 2025
    
    return {
        "greeting": "Hello, World!",
        "message": "¡Bienvenido a la API de solo lectura!",
        "date": fecha  # Fecha de hoy en español
    }
