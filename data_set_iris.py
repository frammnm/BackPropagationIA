# Archivo: data_set_iris.py
# Este archivo contiene el metodo generador del data Set para el ejercicio
# 3.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

# Lee un data set, en el archivo de texto con nombre "nombre",
# el data set debe ser el del ejercicio 3.
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
    sys.exit(1)

# Retorna el data set normalizado con z score y con clasificacion binaria,
# del data set de iris.
def obtener_data_set_binario_z_score(nombre):
  xs,ys,zs,ws,salidas = leer_data_set(nombre)
  res = []
  mean_xs = sum(xs)/len(xs)
  mean_ys = sum(ys)/len(ys)
  mean_zs = sum(zs)/len(zs)
  mean_ws = sum(ws)/len(ws)
  sd_xs = ((sum([ (x_i - mean_xs)**2 for x_i in xs]))/len(xs))**0.5
  sd_ys = ((sum([ (y_i - mean_ys)**2 for y_i in ys]))/len(ys))**0.5
  sd_zs = ((sum([ (z_i - mean_zs)**2 for z_i in zs]))/len(zs))**0.5
  sd_ws = ((sum([ (w_i - mean_ws)**2 for w_i in ws]))/len(ws))**0.5
  for i in range(len(xs)):
    xn = (xs[i]-mean_xs)/sd_xs
    yn = (ys[i]-mean_ys)/sd_ys
    zn = (zs[i]-mean_zs)/sd_zs
    wn = (ws[i]-mean_ws)/sd_ws
    if ((salidas[i] == "Iris-setosa\n") or (salidas[i] == "Iris-setosa")):
      res.append([[xn,yn,zn,wn],[1]])
    else:
      res.append([[xn,yn,zn,wn],[0]])
  return res

# Retorna el data set normalizado con minmax y con clasificacion ternaria,
# del data set de iris.
def obtener_data_set_binario_minmax(nombre):
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

# Retorna el data set normalizado con z score y con clasificacion ternaria,
# del data set de iris.
def obtener_data_set_ternario_z_score(nombre):
  xs,ys,zs,ws,salidas = leer_data_set(nombre)
  res = []
  mean_xs = sum(xs)/len(xs)
  mean_ys = sum(ys)/len(ys)
  mean_zs = sum(zs)/len(zs)
  mean_ws = sum(ws)/len(ws)
  sd_xs = ((sum([ (x_i - mean_xs)**2 for x_i in xs]))/len(xs))**0.5
  sd_ys = ((sum([ (y_i - mean_ys)**2 for y_i in ys]))/len(ys))**0.5
  sd_zs = ((sum([ (z_i - mean_zs)**2 for z_i in zs]))/len(zs))**0.5
  sd_ws = ((sum([ (w_i - mean_ws)**2 for w_i in ws]))/len(ws))**0.5
  for i in range(len(xs)):
    xn = (xs[i]-mean_xs)/sd_xs
    yn = (ys[i]-mean_ys)/sd_ys
    zn = (zs[i]-mean_zs)/sd_zs
    wn = (ws[i]-mean_ws)/sd_ws
    if ((salidas[i] == "Iris-setosa\n") or (salidas[i] == "Iris-setosa")):
      res.append([[xn,yn,zn,wn],[1]])
    elif ((salidas[i] == "Iris-versicolor\n") or (salidas[i] == "Iris-versicolor")):
      res.append([[xn,yn,zn,wn],[0.5]])
    else:
      res.append([[xn,yn,zn,wn],[0]])
  return res

# Retorna el data set normalizado con minmax y con clasificacion ternaria,
# del data set de iris.
def obtener_data_set_ternario_minmax(nombre):
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
