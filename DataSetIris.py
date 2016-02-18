# Archivo: DataSetIris.py
# Este archivo contiene el metodo generador del data Set para el ejercicio
# 1.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

# Lee un data set, en el archivo de texto con nombre "nombre",
# el data set debe ser el del ejercicio 3. Durante la lectura
# de archivo, los puntos leidos son normalizados.
def leer_data_set(nombre):
  try:
    xs = []
    ys = []
    zs = []
    ws = []
    salidas = []
    f = open(nombre,'r') 
    datos = f.readlines()
    for linea in datos:
        palabras = linea.split(",")
        xs.append(float(palabras[0]))
        ys.append(float(palabras[1]))
        zs.append(float(palabras[2]))
        ws.append(float(palabras[3]))
        salidas.append(palabras[4])
    f.close()
    return (xs,ys,zs,ws,salidas)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    return ([],[],[],[],[])

# Retorna el data set normalizado y con clasificacion binaria,
# del data set de iris.
def obtener_data_set_binario(nombre):
  xs,ys,zs,ws,salidas = leer_data_set(nombre)
  res = []
  for i in range(len(xs)):
    xn = (xs[i]-min(xs))/(max(xs)-min(xs))
    yn = (ys[i]-min(ys))/(max(ys)-min(ys))
    zn = (zs[i]-min(zs))/(max(zs)-min(zs))
    wn = (ws[i]-min(ws))/(max(ws)-min(ws))
    if ((salidas[i] == "Iris-setosa\n") or (salidas[i] == "Iris-setosa")):
      res.append([[xn,yn,zn,wn],[1]])
    else:
      res.append([[xn,yn,zn,wn],[0]])
  return res

# Retorna el data set normalizado y con clasificacion ternaria,
# del data set de iris.
def obtener_data_set_ternario(nombre):
  xs,ys,zs,ws,salidas = leer_data_set(nombre)
  res = []
  for i in range(len(xs)):
    xn = (xs[i]-min(xs))/(max(xs)-min(xs))
    yn = (ys[i]-min(ys))/(max(ys)-min(ys))
    zn = (zs[i]-min(zs))/(max(zs)-min(zs))
    wn = (ws[i]-min(ws))/(max(ws)-min(ws))
    if ((salidas[i] == "Iris-setosa\n") or (salidas[i] == "Iris-setosa")):
      res.append([[xn,yn,zn,wn],[1]])
    elif ((salidas[i] == "Iris-versicolor\n") or (salidas[i] == "Iris-versicolor")):
      res.append([[xn,yn,zn,wn],[0.5]])
    else:
      res.append([[xn,yn,zn,wn],[0]])
  return res
