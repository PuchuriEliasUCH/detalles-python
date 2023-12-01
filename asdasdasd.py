def obtener_numero_impares(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero % 2 != 0 and numero > 0:
                return numero
            else:
                print("Por favor, ingresa un número impar y positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def dibujar_triangulo(filas, columnas):
    for i in range(1, filas + 1, 2):
        espacios = (columnas - i) // 2
        fila = [" "] * espacios + ["*"] * i
        print("".join(fila))

# Solicita al usuario el número de filas y columnas (ambos impares)
num_filas = obtener_numero_impares("Ingresa el número impar de filas para el triángulo: ")
num_columnas = obtener_numero_impares("Ingresa el número impar de columnas para el triángulo: ")

dibujar_triangulo(num_filas, num_columnas)