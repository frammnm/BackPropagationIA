# Archivo: main.py
# Este es el archivo principal el cual se encarga de utilizar la red neural.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import red_neural
import data_set_circulo
import data_set_iris
import time
import sys
import random

# Genera los resultados de entrenar la red neural con los data sets.
def generar_resultados(nombre,const_aprendizaje,num_iteraciones,
                       min_neuronas,max_neuronas,data_set):
  try:
    f = open(nombre, 'a')
    str1 = "Constante-de-Aprendizaje: "
    str2 = "  Neuronas: "
    str3 = "  Error-Total: "
    str4 = "  Error-Promedio: "
    str5 = "  Tiempo: "
    for j in range(min_neuronas,max_neuronas+1):
      rn = red_neural.RedNeural(len(data_set[0][0]), j, len(data_set[0][1]),
      	                        aprendizaje = const_aprendizaje)
      tiempo = time.time()
      i = 0
      for k in range(num_iteraciones):
        entradas_entrenamiento = data_set[i][0]
        salidas_entrenamiento = data_set[i][1]
        rn.entrenar(entradas_entrenamiento, salidas_entrenamiento)
        if i == len(data_set)-1:
          i = 0
        else:
          i += 1
      error_total = rn.calcular_error_total(data_set)
      resultado = str1+str(const_aprendizaje)+str2+str(j)+str3+str(error_total)
      resultado += str4+str(error_total/len(data_set))+str5
      resultado += str(time.time() - tiempo)+"\n"
      f.write(resultado)
    f.write("\n")
    f.close()
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(1)

# Genera los resultados de todos los data sets del ejercicio 1.
def generar_resultados_ejercicio1(nombres_de_archivos,data_sets,
                                  const_aprendizaje):
  for i in range(6):
    generar_resultados(nombres_de_archivos[i],const_aprendizaje,
    	                 10000,2,10,data_sets[i])

# Genera los resultados de todos los data sets del ejercicio 3.
def generar_resultados_ejercicio3(nombres_de_archivos,data_sets,
                                  const_aprendizaje):
  for i in range(6,16):
    generar_resultados(nombres_de_archivos[i],const_aprendizaje,
    	               10000,4,10,data_sets[i])

# Genera los resultados para una barrida de 10000 puntos, utilizando
# los data sets del ejercicio 1, utilizando la normalizacion z score.
def generar_resultados_barrida_z_score(rn):
  xs,ys = data_set_circulo.generar_barrido_cuadrado(20)
  mean_xs = sum(xs)/len(xs)
  mean_ys = sum(ys)/len(ys)
  sd_xs = ((sum([ (x_i - mean_xs)**2 for x_i in xs]))/len(xs))**0.5
  sd_ys = ((sum([ (y_i - mean_ys)**2 for y_i in ys]))/len(ys))**0.5
  salidas = []
  for i in range(len(xs)):
    xn = (xs[i]-mean_xs)/sd_xs
    yn = (ys[i]-mean_ys)/sd_ys
    salidas.append(rn.alimentar_neuronas([xn,yn])[0])
  return (xs,ys,salidas)

# Genera los resultados para una barrida de 10000 puntos, utilizando
# los data sets del ejercicio 1, utilizando la normalizacion minmax.
def generar_resultados_barrida_minmax(rn):
  xs,ys = data_set_circulo.generar_barrido_cuadrado(20)
  salidas = []
  for i in range(len(xs)):
    xn = (xs[i]-min(xs))/(max(xs)-min(xs))
    yn = (ys[i]-min(ys))/(max(ys)-min(ys))
    salidas.append(rn.alimentar_neuronas([xn,yn])[0])
  return (xs,ys,salidas)

# Genera los resultados para una barrida de 10000 puntos, utilizando
# los data sets del ejercicio 1 y los escribe en el archivo de texto.
def generar_resultados_barrida(nombre,opcion,rn):
  try:
    if opcion == 0:
      xs,ys,salidas = generar_resultados_barrida_minmax(rn)
    else:
      xs,ys,salidas = generar_resultados_barrida_z_score(rn)
    f = open(nombre, 'w')
    umbral = (max(salidas) + min(salidas))/2
    for i in range(len(xs)):
      if salidas[i] <= umbral:
        f.write(str(xs[i])+" "+str(ys[i])+" 0\n")
      else:
        f.write(str(xs[i])+" "+str(ys[i])+" 1\n")
    f.close()
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(1)

# Genera los resultados para verificar el cambio del error.
def generar_resultados_cambio_del_error(nombre,data_set,const_aprendizaje,
	                                    neuronas,num_iteraciones):
  try:
    f = open(nombre, 'w')
    rn = red_neural.RedNeural(len(data_set[0][0]), neuronas, len(data_set[0][1]),
      	                        aprendizaje = const_aprendizaje)
    i = 0
    for j in range(num_iteraciones):
      entradas_entrenamiento = data_set[i][0]
      salidas_entrenamiento = data_set[i][1]
      rn.entrenar(entradas_entrenamiento, salidas_entrenamiento)
      if i == len(data_set)-1:
        i = 0
      else:
        i += 1
      error_total = rn.calcular_error_total(data_set)
      f.write(str(j+1)+" "+str(error_total)+"\n")
    f.close()
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(1)

# Obtiene la red neural con el menor error, variando la constante de aprendizaje.
def obtener_mejor_red_neural(data_set,neuronas,constantes_de_aprendizaje):
  error = sys.maxint
  mejor_red_neural = None
  for const_aprendizaje in constantes_de_aprendizaje:
    rn = red_neural.RedNeural(len(data_set[0][0]), neuronas, len(data_set[0][1]),
                                  aprendizaje = const_aprendizaje)
    i = 0
    error_total_actual = sys.maxint
    while error_total_actual > 0.001:
      entradas_entrenamiento = data_set[i][0]
      salidas_entrenamiento = data_set[i][1]
      rn.entrenar(entradas_entrenamiento, salidas_entrenamiento)
      if i == len(data_set)-1:
        i = 0
      else:
        i += 1
      error_total_actual = rn.calcular_error_total(data_set)/len(data_set)
      print error_total_actual
    error_total_final = rn.calcular_error_total(data_set)
    if error_total_final < error:
      error = error_total_final
      mejor_red_neural = rn
  return mejor_red_neural

data_sets = [ 
  data_set_circulo.obtener_data_set_z_score("data_sets/Ejercicio1/datos_P1_RN_EM2016_n500.txt"),
  data_set_circulo.obtener_data_set_z_score("data_sets/Ejercicio1/datos_P1_RN_EM2016_n1000.txt"),
  data_set_circulo.obtener_data_set_z_score("data_sets/Ejercicio1/datos_P1_RN_EM2016_n2000.txt"),
  data_set_circulo.obtener_data_set_z_score("data_sets/Ejercicio1/500_DataSet.txt"),
  data_set_circulo.obtener_data_set_z_score("data_sets/Ejercicio1/1000_DataSet.txt"),
  data_set_circulo.obtener_data_set_z_score("data_sets/Ejercicio1/2000_DataSet.txt"),
  data_set_iris.obtener_data_set_binario_z_score("data_sets/Iris-Setosa/iris75.data"),
  data_set_iris.obtener_data_set_ternario_z_score("data_sets/Iris-Setosa/iris75.data"),
  data_set_iris.obtener_data_set_binario_z_score("data_sets/Iris-Setosa/iris90.data"),
  data_set_iris.obtener_data_set_ternario_z_score("data_sets/Iris-Setosa/iris90.data"),
  data_set_iris.obtener_data_set_binario_z_score("data_sets/Iris-Setosa/iris105.data"),
  data_set_iris.obtener_data_set_ternario_z_score("data_sets/Iris-Setosa/iris105.data"),
  data_set_iris.obtener_data_set_binario_z_score("data_sets/Iris-Setosa/iris120.data"),
  data_set_iris.obtener_data_set_ternario_z_score("data_sets/Iris-Setosa/iris120.data"),
  data_set_iris.obtener_data_set_binario_z_score("data_sets/Iris-Setosa/iris135.data"),
  data_set_iris.obtener_data_set_ternario_z_score("data_sets/Iris-Setosa/iris135.data")
]
nombres_de_archivos = [
  "resultados/Ejercicio1/Resultados_Profesora_500.txt",
  "resultados/Ejercicio1/Resultados_Profesora_1000.txt",
  "resultados/Ejercicio1/Resultados_Profesora_2000.txt",
  "resultados/Ejercicio1/Resultados_Nosotros_500.txt",
  "resultados/Ejercicio1/Resultados_Nosotros_1000.txt",
  "resultados/Ejercicio1/Resultados_Nosotros_2000.txt",
  "resultados/Iris-Setosa/Binario/Resultados_Iris_75_Binario.txt",
  "resultados/Iris-Setosa/Ternario/Resultados_Iris_75_Ternario.txt",
  "resultados/Iris-Setosa/Binario/Resultados_Iris_90_Binario.txt",
  "resultados/Iris-Setosa/Ternario/Resultados_Iris_90_Ternario.txt",
  "resultados/Iris-Setosa/Binario/Resultados_Iris_105_Binario.txt",
  "resultados/Iris-Setosa/Ternario/Resultados_Iris_105_Ternario.txt",
  "resultados/Iris-Setosa/Binario/Resultados_Iris_120_Binario.txt",
  "resultados/Iris-Setosa/Ternario/Resultados_Iris_120_Ternario.txt",
  "resultados/Iris-Setosa/Binario/Resultados_Iris_135_Binario.txt",
  "resultados/Iris-Setosa/Ternario/Resultados_Iris_135_Ternario.txt",
]

constantes_de_aprendizaje = [0.01,0.05,0.1,0.2,0.3,0.5]

# # Esta parte sirve para generar todos los resultados posibles de todos los data sets.
# for const_aprendizaje in constantes_de_aprendizaje:
#   generar_resultados_ejercicio1(nombres_de_archivos,data_sets,const_aprendizaje)
#   generar_resultados_ejercicio3(nombres_de_archivos,data_sets,const_aprendizaje)

# nombres_de_archivos_de_error = [
#   'resultados/Error/Resultados_Cambio_del_Error_2000_Profesora.txt',
#   'resultados/Error/Resultados_Cambio_del_Error_2000_Nosotros.txt'
# ]
# generar_resultados_cambio_del_error(nombres_de_archivos_de_error[0],data_sets[2],constantes_de_aprendizaje[1],10,10000)
# generar_resultados_cambio_del_error(nombres_de_archivos_de_error[1],data_sets[5],constantes_de_aprendizaje[0],10,10000)

nombres_de_archivos_de_barrida = [
  "resultados/10000-Puntos/Resultados_Profesora.txt",
  "resultados/10000-Puntos/Resultados_Nosotros.txt"
]

rn = red_neural.RedNeural(len(data_sets[2][0][0]), 10, len(data_sets[2][0][1]), aprendizaje=0.01)
i = 0
for k in range(100000):
  entradas_entrenamiento = data_sets[2][i][0]
  salidas_entrenamiento = data_sets[2][i][1]
  rn.entrenar(entradas_entrenamiento, salidas_entrenamiento)
  if i == len(data_sets[2])-1:
    i = 0
  else:
    i += 1

generar_resultados_barrida(nombres_de_archivos_de_barrida[0],1,rn)

rn = red_neural.RedNeural(len(data_sets[5][0][0]), 10, len(data_sets[5][0][1]), aprendizaje=0.01)
i = 0
for k in range(100000):
  entradas_entrenamiento = data_sets[5][i][0]
  salidas_entrenamiento = data_sets[5][i][1]
  rn.entrenar(entradas_entrenamiento, salidas_entrenamiento)
  if i == len(data_sets[5])-1:
    i = 0
  else:
    i += 1

generar_resultados_barrida(nombres_de_archivos_de_barrida[1],1,rn)