from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from urllib.parse import quote_plus
from fastapi.staticfiles import StaticFiles
import os
import uvicorn

print("Starting backend.py script...")

app = FastAPI()

# Configuración de conexión
user = "giomont"
password = "Semeolvido@712510"  # Actualizo la contraseña a la nueva clave proporcionada
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

# Montar el directorio principal para servir archivos estáticos
app.mount("/static", StaticFiles(directory="/home/gio/menu_mongodb_pyback"), name="static")

@app.get("/productos")
def get_productos(categoria: str = None):
    try:
        filtro = {}
        if categoria:
            filtro["categoria"] = categoria
        productos = list(db.productos.find(filtro, {"_id": 0}))
        print(f"Productos fetched from MongoDB: {productos}")  # Debug print
        return productos
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

@app.get("/categorias")
def get_categorias():
    categorias = db.productos.distinct("categoria")
    return categorias

@app.get("/check_db")
def check_db_connection():
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        return {"status": "success", "message": "MongoDB connection successful!"}
    except Exception as e:
        return {"status": "error", "message": f"MongoDB connection failed: {e}"}

print("backend.py script finished setup.")

if __name__ == "__main__":
    print("Running uvicorn server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
