<div>
  <img style="100%" src="https://capsule-render.vercel.app/api?type=waving&height=105&section=header&reversal=false&text=proyecto%20final%20&fontSize=40&fontColor=#572929&fontAlign=40&fontAlignY=25&rotate=4&stroke=-&animation=twinkling&descSize=20&descAlign=50&descAlignY=50&textBg=true&color=undefined"  />
</div>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" height="40" alt="github logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg" height="40" alt="firebase logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" alt="git logo"  />
</div>

###

<p align="left">from fastapi import FastAPI<br>import firebase_admin<br>from firebase_admin import credentials, firestore<br>from pydantic import BaseModel <br><br>cred = credentials.Certificate("firebase.json")<br>firebase_admin.initialize_app(cred)<br><br>db = firestore.client()<br><br>app =FastAPI()<br>@app.get("/health")<br>def obtener_salud_sitio():<br>    return "braian"<br><br>Este código crea una API web usando FastAPI que:<br>Se conecta a Firebase (Firestore) usando credenciales seguras.<br>Levanta un servidor backend listo para trabajar con una base de datos.<br>Expone un endpoint de prueba (/health) para verificar que todo funciona.<br><br>class Usuario(BaseModel):<br>    nombre:str<br>    email:str<br>    edad:int<br>    contraseña:str<br>    repetir_contraseña:str<br><br>@app.get("/usuarios")<br>def obtener_usuarios_sitio():<br>    collection = db.collection("usuarios").stream()<br>    return [doc.to_dict() for doc in collection]<br><br>@app.post("/usuarios")<br>def crear_usuario (usuario: Usuario):<br>    if usuario.contraseña != usuario.repetir_contraseña:<br>        return "Las contraseñas no coinciden"<br>    <br>    del usuario.repetir_contraseña<br>    <br>    db.collection("usuarios").add(usuario.dict())<br>    return "Usuario creado exitosamente"<br><br>Esta parte del codigo define cómo debe ser un usuario, especificando qué datos son obligatorios y validando automáticamente lo que llega desde el cliente.<br>Expone un endpoint para listar usuarios, que obtiene todos los registros almacenados en la base de datos.<br>Expone un endpoint para crear usuarios, que:<br>recibe los datos de registro,<br>verifica que las contraseñas coincidan,<br>guarda el usuario en la base de datos si la validación es correcta.<br><br>@app.get("/cursos")<br>def obtener_cursos_sitio():<br>    collection = db.collection("cursos").stream()<br>    return [doc.to_dict() for doc in collection]<br><br>class Curso (BaseModel):<br>    nombre:str<br>    descripcion:str<br>    duracion:int<br><br>@app.post("/cursos")<br>def crear_curso (curso: Curso):<br>    if curso.nombre.lower() == "admin":<br>        return "No se puede crear un curso con el nombre 'admin'"<br>        <br>    db.collection("cursos").add(curso.dict())<br>    return "Curso creado exitosamente"<br><br>Define la estructura de un curso, indicando qué datos debe tener obligatoriamente (nombre, descripción y duración).<br>Expone un endpoint para listar cursos (GET /cursos), que obtiene todos los cursos guardados en la base de datos y los devuelve en formato JSON.<br>Expone un endpoint para crear cursos (POST /cursos), que:<br>recibe los datos del curso desde el cliente,<br>valida que el nombre del curso no sea "admin" (para evitar nombres reservados),<br>guarda el curso en la base de datos si pasa la validación,<br>devuelve un mensaje indicando si la creación fue exitosa o no.</p>

###

<br clear="both">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/braianpobian/braianpobian/output/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/braianpobian/braianpobian/output/pacman-contribution-graph.svg">
  <img alt="pacman contribution graph" src="https://raw.githubusercontent.com/braianpobian/braianpobian/output/pacman-contribution-graph.svg">
</picture>

###
