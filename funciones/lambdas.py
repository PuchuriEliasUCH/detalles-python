# nombre = lambda parametro : [...]

# creando funcione lambda, solo para instruccines 'simples' -> una sola entrada
multiplicar_por_2 = lambda x : x*2

def multiplicar_x_2(x):
  return x*2

# Creando funcion comun para determinar numeros pares
num = [1,2,3,4,5,6]

def es_par(num):
  if num % 2 == 0:
    return True
  
numeros_pares = filter(es_par, num)

# creando funcion lambda para el ejemplo anterior

numeros_pares = filter(lambda x : x%2==0, num)

print(list(numeros_pares))