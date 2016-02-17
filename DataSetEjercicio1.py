# Archivo: DataSetEjercicio1.py
# Este archivo contiene el metodo generador del data Set para el ejercicio
# 1.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import random

# Genera un data set balanceado, de tamano n, para el ejercicio 1.
# Se crea un archivo de texto con los puntos y sus respectivas salidas.
def generar_data_set(n):
  try:
    f = open(str(n)+'_DataSet', 'w') 
    nc = 0 # Numero de puntos dentro del circulo.
    ns = 0 # Numero de puntos dentro del cuadrado y afuera del circulo.
    i = 0
    while (i < n):
      x = random.uniform(0,20)
      y = random.uniform(0,20)
      punto = (x - 10)**2 + (y - 10)**2
      if ((punto <= 49) and (nc < n/2)):
        nc += 1
        f.write(str(x)+' '+str(y)+' -1\n')
      elif ((punto <= 49) and (nc >= n/2)):
        continue
      elif ((punto > 49) and (ns < n/2)):
        ns += 1
        f.write(str(x)+' '+str(y)+' 1\n')
      elif ((punto > 49) and (ns >= n/2)):
        continue
      i += 1
    f.close()
    return
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

# Genera un data set balanceado, de tamano n, para el ejercicio 1.
# Se crea una lista de puntos y de salidas; y se retornan en una tupla.
def generar_data_set_lista(n):
  puntos = []
  salidas = [] 
  nc = 0 # Numero de puntos dentro del circulo.
  ns = 0 # Numero de puntos dentro del cuadrado y afuera del circulo.
  i = 0
  while (i < n):
    x = random.uniform(0,20)
    y = random.uniform(0,20)
    point = (x - 10)**2 + (y - 10)**2
    if ((point <= 49) and (nc < n/2)):
      nc += 1
      puntos.append(point)
      salidas.append(1)
    elif ((point <= 49) and (nc >= n/2)):
      continue
    elif ((point > 49) and (ns < n/2)):
      ns += 1
      puntos.append(point)
      salidas.append(-1)
    elif ((point > 49) and (ns >= n/2)):
      continue
    i += 1
  return (puntos,salidas)
    