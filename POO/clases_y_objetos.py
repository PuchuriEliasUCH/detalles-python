class Celular:
  def __init__(self, marca, modelo, camara):
    self.marca = marca
    self.modelo = modelo
    self.camara = camara

  def llamar(self):
    return "Estas realizando una llamada"

  def cortar(self):
    return "Cortaste la llamada"

celular1 = Celular('Apple', 'iPhone X', '48MP')

print(celular1.llamar())