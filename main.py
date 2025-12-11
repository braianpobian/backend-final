from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app =FastAPI()
@app.get("/health")
def obtener_salud_sitio():
    return "braian"

@app.get("/usuarios")
def obtener_usuarios_sitio():
    collection = db.collection("usuarios").stream()
    return [doc.to_dict() for doc in collection]



@app.get("/cursos")
def obtener_cursos_sitio():
    collection = db.collection("cursos").stream()
    return [doc.to_dict() for doc in collection]


