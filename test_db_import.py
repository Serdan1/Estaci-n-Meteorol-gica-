# test_db_import.py
from src.model.database import Database

db = Database()
db.close()
print("Importación y uso de Database exitoso")