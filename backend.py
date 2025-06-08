from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pymongo import MongoClient
from urllib.parse import quote_plus
import os
import uvicorn

print("Starting backend.py script...")

app = FastAPI()

# Configuración de conexión MongoDB
user = "giomont"
password = "Semeolvido@712510"
user_escaped = quote_plus(user)
password_escaped = quote_plus(password)
uri = f"mongodb+srv://{user_escaped}:{password_escaped}@cluster0.p6sdz0h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["productos"]

# Permitir CORS para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas API
@app.get("/productos")
def get_productos(categoria: str = None):
    try:
        filtro = {}
        if categoria:
            filtro["categoria"] = categoria
        productos = list(db.productos.find(filtro, {"_id": 0}))
        print(f"Productos encontrados: {productos}")
        return productos
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

@app.get("/")
async def read_index():
    return FileResponse('productos.html')

# Servir archivos estáticos
app.mount("/", StaticFiles(directory="/home/gio/menu_mongodb_pyback", html=True), name="static")

print("Backend setup completed.")

if __name__ == "__main__":
    print("Starting uvicorn server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
