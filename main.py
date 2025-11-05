import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import redis.asyncio as redis  # Async Redis client

# Intenta cargar dotenv solo si está disponible (para desarrollo local)
try:
    from dotenv import load_dotenv
    load_dotenv()  # Carga .env si existe
except ImportError:
    pass  # En producción (como Railway), ignora y usa variables de entorno directamente

app = FastAPI()

# Configuración de CORS (restringe orígenes si es posible para mayor seguridad; "*" es abierto)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia a dominios específicos en prod si sabes cuáles son
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

# Conexión async a Redis (usando REDIS_URL de Railway)
async def get_redis():
    return await redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

@app.get("/")
async def root():
    # Accede a variables de entorno con valores por defecto
    hello = os.getenv("HELLO", "default_hello_value")
    hola = os.getenv("HOLA", "default_hola_value")
    
    # Fecha actual en ISO 8601 (optimizado: usa isoformat() para eficiencia)
    fecha_iso = datetime.now().date().isoformat()
    
    return {
        "greeting": "Hello, World!",
        "message": "¡Bienvenido a la API de solo lectura!",
        "date": fecha_iso,
        "hello": hello,
        "hola": hola
    }

@app.get("/holamundo")
async def hola_mundo():
    return {"message": "¡Hola, Mundo we!"}

# Nuevo endpoint para probar Redis
@app.get("/redis")
async def test_redis():
    r = await get_redis()
    try:
        # Set y get simple para probar
        await r.set("test_key", "test_value")
        value = await r.get("test_key")
        await r.delete("test_key")  # Limpia después del test
        return {
            "status": "success",
            "redis_value": value.decode("utf-8") if value else None,
            "message": "Redis connection tested successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to connect to Redis: {str(e)}"
        }
    finally:
        await r.aclose()  # Cierra la conexión async

# Endpoint de debug: coméntalo o remuévelo en producción para seguridad
# @app.get("/debug")
# async def debug_env():
#     env_vars = dict(os.environ)
#     return {"environment_variables": env_vars}
