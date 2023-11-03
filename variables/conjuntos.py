# los conjuntos son elementos mutables que almacenan datos inmutables

# creando conjuntos
conjunto = {'dato1', 'dato2'}

# creando conjuntos con set()
conjunto1 = set(['Dato1', ('Dato1 de tupla', 'Dato2 de tupla')])

# almacenando un conjunto dentro de otro 
conjunto_congelado = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto_congelado, 'dato3'}

print(type(conjunto_congelado))
print(conjunto, conjunto1, conjunto2)