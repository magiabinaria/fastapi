from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"greeting": "Hello, World!", "message": "¡Bienvenido a la API de solo lectura gera!"}
