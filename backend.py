from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from urllib.parse import quote_plus
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Configuración de conexión
user = "giomont"
password = "Semeolvido@7125"
user_escaped = quote_plus(user)
password_escaped = quote_plus(password)
uri = f"mongodb+srv://{user_escaped}:{password_escaped}@cluster0.p6sdz0h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["productos"]  # Cambiado de 'test' a 'productos' para usar la base correcta

# Permitir CORS para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar el directorio 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/productos")
def get_productos(categoria: str = None):
    filtro = {}
    if categoria:
        filtro["categoria"] = categoria
    productos = list(db.productos.find(filtro, {"_id": 0}))
    return productos

@app.get("/categorias")
def get_categorias():
    categorias = db.productos.distinct("categoria")
    return categorias
