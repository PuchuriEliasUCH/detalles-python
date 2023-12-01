nums = []

while True:
  x = int(input("Ingresar la cantidad de números: "))

  if x > 0:
    break

  print("Ingrese una cantidad positiva.")

for i in range(x):
  num = int(input(f"Ingresar el número #{i + 1}: "))
  nums.append(num)
    
pos = len(list(filter(lambda x: x > 0, nums)))
neg = len(list(filter(lambda x: x < 0, nums)))
nul = len(list(filter(lambda x: x == 0, nums)))

print(f"""
{"No hay #positivos" if pos == 0 else f"Positivos: {pos}"}
{"No hay #negativos" if neg == 0 else f"Negativos: {neg}"}
{"No hay ceros" if nul == 0 else f"Ceros: {nul}"}
""")