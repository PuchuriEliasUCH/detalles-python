from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn <file>:app --reload

# Entidad user
class User(BaseModel):
  id: int
  name: str
  surname: str
  age: int


users_fake_db = [User(id = 1, name = "Fernanda", surname = "Beltrán", age = 18),
                 User(id = 2, name = "Daniel", surname = "Puchuri", age = 22),
                 User(id = 3, name = "Hector", surname = "Mego", age = 17)]

@app.get("/users")
async def users():
  return users_fake_db

# Atributos por parametro
@app.get("/users/{id}")
async def user(id: int):
  return search_user(id)
  
# Atributos por query
@app.get("/userquery")
async def userquery(id:int):
  return search_user(id)

@app.post("/users")
async def user(user: User):
  if type(search_user(user.id)) == User:
    return {"error":"El usuario ya existe"}
  else:
    users_fake_db.append(user)


def search_user(id: int):
  users = filter(lambda user: user.id == id, users_fake_db)
  try:
    return list(users)[0]
  except:
    return {"error": "No se ha encontrado el usuario"}
  