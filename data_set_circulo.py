# Archivo: data_set_circulo.py
# Este archivo contiene el metodo generador del data Set del circulo.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import random

# Genera un data set balanceado, de tamano n, para el ejercicio 1.
# Se crea un archivo de texto con los puntos y sus respectivas salidas.
def generar_data_set(n):
  try:
    if n % 2 != 0:
      n += 1
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

# Lee un data set, en el archivo de texto con nombre "nombre".
def leer_data_set(nombre):
  try:
    xs = []
    ys = []
    salidas = []
    f = open(nombre,'r') 
    datos = f.readlines()
    for linea in datos:
        palabras = linea.split()
        xs.append(float(palabras[0]))
        ys.append(float(palabras[1]))
        if palabras[2] == "-1":
          salidas.append(1)
        else:
          salidas.append(0)
    f.close()
    return (xs,ys,salidas)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(1)

# Retorna el data set normalizado con z score.
def obtener_data_set_z_score(nombre):
  xs,ys,salidas = leer_data_set(nombre)
  res = []
  mean_xs = sum(xs)/len(xs)
  mean_ys = sum(ys)/len(ys)
  sd_xs = ((sum([ (x_i - mean_xs)**2 for x_i in xs]))/len(xs))**0.5
  sd_ys = ((sum([ (y_i - mean_ys)**2 for y_i in ys]))/len(ys))**0.5
  for i in range(len(xs)):
    xn = (xs[i]-mean_xs)/sd_xs
    yn = (ys[i]-mean_ys)/sd_ys
    res.append([[xn,yn],[salidas[i]]])
  return res

# Retorna el data set normalizado con minmax.
def obtener_data_set_minmax(nombre):
  xs,ys,salidas = leer_data_set(nombre)
  res = []
  for i in range(len(xs)):
    xn = (xs[i]-min(xs))/(max(xs)-min(xs))
    yn = (ys[i]-min(ys))/(max(ys)-min(ys))
    res.append([[xn,yn],[salidas[i]]])
  return res

# Genera un data set balanceado, de tamano n, para el ejercicio 1.
# Se crea una lista de listas que contiene los puntos y sus salidas.
def generar_data_set_lista(n):
  if n % 2 != 0:
    n += 1
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
  xs = []
  ys = []
  unidad = n / 100.0
  y = 0 
  for i in range(101):
    x = 0
    for j in range(101):
      xs.append(x)
      ys.append(y)
      x = x + unidad
    y = y + unidad
  return (xs,ys)