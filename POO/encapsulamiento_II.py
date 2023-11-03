class Persona:
  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self.__edad = edad

  # getter
  @property
  def nombre(self):
    return self.__nombre
  
  # setter
  @nombre.setter
  def nombre(self, nombre):
    self.__nombre = nombre

  
persona = Persona('daniel', 22)

print(persona._Persona__edad)