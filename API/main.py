from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def hola_mundo():
#   return "Bienvenido! :D"

# Url local: http://127.0.0.1:8000
@app.get("/")
async def root():
  return "Hola mundo!"

# Url local: http://127.0.0.1:8000/url
@app.get("/url")
async def get_url():
  return "http://localhost:8000/url"