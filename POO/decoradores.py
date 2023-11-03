# un decorador recibe una funcion, realiza modificaciones EXTRAS a ella
# luego devuelve la función modificada
def decorador(funcion):
  def funcion_modificada():
    print("Modificaciones antes de ejecutar la función")
    funcion()
    print("Modificaciones luego de ejecutar la función")

  return funcion_modificada

# def saludo():
#   print("Hola mundo")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
  print("Hola Fer :3")

saludo()