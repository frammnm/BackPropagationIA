# Archivo: data_set_ejercicio1.py
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
    f = open(str(n)+'_DataSet.txt', 'w') 
    nc = 0 # Numero de puntos dentro del circulo.
    ns = 0 # Numero de puntos dentro del cuadrado y afuera del circulo.
    for i in range(n):
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
    f.close()
    return
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(1)

# Lee un data set, en el archivo de texto con nombre "nombre",
# el data set debe ser el del ejercicio 1. Durante la lectura
# de archivo, los puntos leidos son normalizados.
def obtener_data_set(nombre):
  try:
    puntos_y_salidas = []
    f = open(nombre,'r') 
    datos = f.readlines()
    for linea in datos:
        palabras = linea.split()
        x = (float(palabras[0]))
        y = (float(palabras[1]))
        xn = x / 20 # Normalizar el punto.
        yn = y / 20 # Normalizar el punto.
        if palabras[2] == "-1":
          puntos_y_salidas.append([[xn,yn],[1]])
        else:
          puntos_y_salidas.append([[xn,yn],[0]])
    f.close()
    return puntos_y_salidas
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(1)

# Genera un data set balanceado, de tamano n, para el ejercicio 1.
# Se crea una lista de listas que contiene los puntos y sus salidas.
def generar_data_set_lista(n):
  puntos_y_salidas = []
  nc = 0 # Numero de puntos dentro del circulo.
  ns = 0 # Numero de puntos dentro del cuadrado y afuera del circulo.
  for i in range(n):
    x = random.uniform(0,20)
    y = random.uniform(0,20)
    xn = x / 20 # Normalizar el punto.
    yn = y / 20 # Normalizar el punto.
    point = (x - 10)**2 + (y - 10)**2
    if ((point <= 49) and (nc < n/2)):
      nc += 1
      puntos_y_salidas.append([[xn,yn],[1]])
    elif ((point <= 49) and (nc >= n/2)):
      continue
    elif ((point > 49) and (ns < n/2)):
      ns += 1
      puntos_y_salidas.append([[xn,yn],[0]])
    elif ((point > 49) and (ns >= n/2)):
      continue
  return puntos_y_salidas

# Genera un data set de 10000 puntos utilizados para el ejercicio 2.
# Los cuales son utilizados para probar la red neural.
def generar_barrido_cuadrado(n):
  puntos_y_salidas = []
  unidad = n / 100.0
  y = 0 
  for i in range(101):
    x = 0
    for j in range(101):
      puntos_y_salidas.append([x,y])
      x = x + unidad
    y = y + unidad
  return puntos_y_salidas