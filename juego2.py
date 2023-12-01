def main():
  while True:
    try:
      num_players = int(input("Ingresar número de jugadores "))
      
      if num_players > 0:
        break
      else:
        print("Ingrese una cantidad de jugadores correcta")
    except ValueError:
      print("Debe ingresar solo números")

  game = []

  for player in range(num_players + 1):
    print(f"==== {f'Jugador {player + 1}' if player != num_players else "Arbitro"} ====")

    nums_jugador(game) if player != num_players else nums_jugador(game, 2)

  game[-1].sort()

  a,b = game[-1]

  print(mostrar_resultados(game, a,b))



def nums_jugador(lista, ultimo = 4):
  nums = []
  for _ in range(ultimo):
    while True:
      try:
        num = int(input("Ingresar el número de la jugada [1-10]: ")) 
      except ValueError:
        print("Debe ingresar solo números")
      else:
        if 0 < num <= 10:
          nums.append(num)
          break
        else:
          print("Ingrese un número dentro del rango establecido")

  lista.append(nums)

def mostrar_resultados(lista, a, b):
  res = f"Números de la casa: {lista[-1]}\n"

  for i in range(len(lista) - 1):
    aciertos = list(filter(lambda x: x in range(a+1, b), lista[i]))
    prom = 0
    if len(aciertos) != 0:
      prom = sum(aciertos)/len(aciertos)
    
    res += f"""\n==== jugador {i+1} ====
Números ingresados: {lista[i]}
Aciertos: {aciertos if len(aciertos) != 0 else "0"}
Promedio de aciertos: {prom}
"""
    
  return res;

main()