from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore
from pydantic import BaseModel 

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app =FastAPI()
@app.get("/health")
def obtener_salud_sitio():
    return "braian"

class Usuario(BaseModel):
    nombre:str
    email:str
    edad:int
    contraseña:str
    repetir_contraseña:str

@app.get("/usuarios")
def obtener_usuarios_sitio():
    collection = db.collection("usuarios").stream()
    return [doc.to_dict() for doc in collection]

@app.post("/usuarios")
def crear_usuario (usuario: Usuario):
    if usuario.contraseña != usuario.repetir_contraseña:
        return "Las contraseñas no coinciden"
    
    del usuario.repetir_contraseña
    
    db.collection("usuarios").add(usuario.dict())
    return "Usuario creado exitosamente"




@app.get("/cursos")
def obtener_cursos_sitio():
    collection = db.collection("cursos").stream()
    return [doc.to_dict() for doc in collection]

class Curso (BaseModel):
    nombre:str
    descripcion:str
    duracion:int

@app.post("/cursos")
def crear_curso (curso: Curso):
    if curso.nombre.lower() == "admin":
        return "No se puede crear un curso con el nombre 'admin'"
        
    db.collection("cursos").add(curso.dict())
    return "Curso creado exitosamente"

#crear una ruta post para crear cursos
#no se puede subir un curso con el nombre admin
#desarrollen una prueba



