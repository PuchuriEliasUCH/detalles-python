class MiClase: 
  def __init__(self, privado) -> None:
    self.__privado = privado
    # doble guion bajo __

  def get_privado(self):
    return self.__privado
  
  def set_privado(self, __privado):
    self.__privado = __privado


esPrivado = MiClase("No es privado")

esPrivado.set_privado("Ya no es privado")

print(esPrivado.get_privado())