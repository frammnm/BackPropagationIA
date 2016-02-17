
import random
import math

# n es el numero de nodos en la capa A y m es el numero de nodos en la capa B.
def inicializarPesos(n,m):
	i = 0
	pesos = []
	d = 1 / math.sqrt(n) # Numero utilizado para el rango de random.
	while (i < (n*m)):
		pesos.append(random.uniform(-d,d))
		i += 1
	return pesos

print inicializarPesos(5,3)