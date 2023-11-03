class Persona:
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad

  def hablar(self):
    return "Hola, estoy hablando"
  
class Empleado(Persona):
  def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
    super.__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario

daniel = Empleado('Daniel', 22, 'Peruano', 'Estudiante', 1500)
