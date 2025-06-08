from pymongo import MongoClient
from urllib.parse import quote_plus

print("Starting MongoDB query script...")

user = "giomont"
password = "Semeolvido@712510"
user_escaped = quote_plus(user)
password_escaped = quote_plus(password)
uri = f"mongodb+srv://{user_escaped}:{password_escaped}@cluster0.p6sdz0h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = None # Initialize client to None

try:
    print(f"Attempting to connect to MongoDB at {uri}...")
    client = MongoClient(uri)
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
    print("MongoDB connection successful!")

    db = client["productos"]
    print("Accessing 'productos' database.")

    # Fetch one product to inspect its structure
    one_product = db.productos.find_one({}, {"_id": 0})
    print("Sample Product Structure:")
    if one_product:
        print(one_product)
    else:
        print("No products found in the 'productos' collection.")

except Exception as e:
    print(f"Error during MongoDB operation: {e}")

finally:
    if client:
        client.close()
        print("MongoDB connection closed.")

print("MongoDB query script finished.")
