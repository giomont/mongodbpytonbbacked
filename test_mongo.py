from pymongo import MongoClient
from urllib.parse import quote_plus

user = "giomont"
password = "Semeolvido@7125"
user_escaped = quote_plus(user)
password_escaped = quote_plus(password)

uri = f"mongodb+srv://{user_escaped}:{password_escaped}@cluster0.p6sdz0h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("¡Conexión exitosa a MongoDB Atlas!")
    # Listar bases de datos
    dbs = client.list_database_names()
    print("Bases de datos:", dbs)
    db_name = "productos"
    if db_name in dbs:
        db = client[db_name]
        collections = db.list_collection_names()
        print(f"Colecciones en la base de datos '{db_name}':", collections)
        if "productos" in collections:
            print("Contenido de la colección 'productos':")
            for doc in db["productos"].find():
                print(doc)
        else:
            print("La colección 'productos' no existe en la base de datos.")
    else:
        print(f"La base de datos '{db_name}' no se encontró. Bases disponibles:", dbs)
except Exception as e:
    print("Error al conectar:", e)
