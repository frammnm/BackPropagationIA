# Archivo: RedNeural.py
# Este archivo contiene las clases utilizadas para la implementacion de una
# red neural.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import random
import math
import DataSetEjercicio1
import time 
import DataSetIris

###############################################################################
#############################      RED NEURAL      ############################
###############################################################################
class RedNeural: 
  APRENDIZAJE = 0.5 # Constante de aprendizaje.

  def __init__(self, cantidadEntradas, cantidadNeuronas, cantidadSalidas, 
               pesosNeuronas = None, biasNeuronas = None, pesosSalidas = None, 
               biasSalidas = None):
    self.cantidadEntradas = cantidadEntradas
    self.cantidadSalidas = cantidadSalidas
    self.capa_oculta = CapaNeuronas(cantidadNeuronas,biasNeuronas)
    self.capa_salida = CapaNeuronas(cantidadSalidas,biasSalidas)
    self.inicializar_pesos_entrada_ocultos(pesosNeuronas)
    self.inicializar_pesos_ocultos_salida(pesosSalidas)

  def inicializar_pesos_entrada_ocultos(self, pesosNeuronas):
    d = math.sqrt(6/(self.cantidadEntradas + len(self.capa_oculta.neuronas))) # Numero utilizado para el rango de los pesos.
    num_peso = 0
    for i in range(len(self.capa_oculta.neuronas)):
      for j in range(self.cantidadEntradas):
          if not pesosNeuronas:
            self.capa_oculta.neuronas[i].pesos.append(random.uniform(-d,d))
          else:
            self.capa_oculta.neuronas[i].pesos.append(pesosNeuronas[num_peso])
          num_peso += 1 

  def inicializar_pesos_ocultos_salida(self, pesosSalidas):
    d = math.sqrt(6/(self.cantidadSalidas + len(self.capa_oculta.neuronas))) # Numero utilizado para el rango de los pesos.
    num_peso = 0
    for i in range(len(self.capa_salida.neuronas)):
      for j in range(len(self.capa_oculta.neuronas)):
          if not pesosSalidas:
            self.capa_salida.neuronas[i].pesos.append(random.uniform(-d,d))
          else:
            self.capa_salida.neuronas[i].pesos.append(pesosSalidas[num_peso])
          num_peso += 1 

  def inspect(self):
    print('------')
    print('Entradas: {}'.format(self.cantidadEntradas))
    print('------')
    print('Capa oculta')
    self.capa_oculta.inspect()
    print('------')
    print('Capa salida')
    self.capa_salida.inspect()
    print('------')

  def alimentar_neuronas(self, entradas):
    salidasOcultas = self.capa_oculta.calcular_salidas(entradas)
    self.capa_salida.calcular_salidas(salidasOcultas)

  def entrenar(self, entradas, salidas):
    self.alimentar_neuronas(entradas)

    erroresDerivadasRespectoNeuronasSalidas = [0] * len(self.capa_salida.neuronas)
    for i in range(len(self.capa_salida.neuronas)):
      erroresDerivadasRespectoNeuronasSalidas[i] = self.capa_salida.neuronas[i].derivada_error_respecto_entrada_total_red(salidas[i])

    erroresDerivadasRespectoNeuronasOcultas = [0] * len(self.capa_oculta.neuronas)
    for i in range(len(self.capa_oculta.neuronas)):
      sumaError = 0 
      for j in range(len(self.capa_salida.neuronas)):
        sumaError += erroresDerivadasRespectoNeuronasSalidas[j] * self.capa_salida.neuronas[j].pesos[i]
      erroresDerivadasRespectoNeuronasOcultas[i] = sumaError * self.capa_oculta.neuronas[i].derivada_funcion_logistica()

    for i in range(len(self.capa_salida.neuronas)):
      for j in range(len(self.capa_salida.neuronas[i].pesos)):
        errorRespectoPeso = erroresDerivadasRespectoNeuronasSalidas[i] * self.capa_salida.neuronas[i].derivada_entrada_total_red_respecto_peso(j)
        self.capa_salida.neuronas[i].pesos[j] -= self.APRENDIZAJE * errorRespectoPeso

    for i in range(len(self.capa_oculta.neuronas)):
      for j in range(len(self.capa_oculta.neuronas[i].pesos)):
        errorRespectoPeso = erroresDerivadasRespectoNeuronasOcultas[i] * self.capa_oculta.neuronas[i].derivada_entrada_total_red_respecto_peso(j)
        self.capa_oculta.neuronas[i].pesos[j] -= self.APRENDIZAJE * errorRespectoPeso
  
  def calcular_error_total(self, training_sets):
    total_error = 0
    for t in range(len(training_sets)):
      training_inputs, training_outputs = training_sets[t]
      self.alimentar_neuronas(training_inputs)
      for o in range(len(training_outputs)):
        total_error += self.capa_salida.neuronas[o].calcular_error(training_outputs[o])
    return total_error

###############################################################################
#############################     CAPA NEURONAS    ############################
###############################################################################
class CapaNeuronas:

  def __init__(self, cantidad, bias):
    self.bias = bias if bias else random.random()
    self.neuronas = []
    for i in range(cantidad):
      self.neuronas.append(Neurona(self.bias))

  def inspect(self):
    print('Neuronas:', len(self.neuronas))
    for n in range(len(self.neuronas)):
      print(' Neurona', n)
      print(' Evaluacion', self.neuronas[n].evaluacion)
      for w in range(len(self.neuronas[n].pesos)):
          print('  Peso:', self.neuronas[n].pesos[w])
      print('  Bias:', self.bias)

  def calcular_salidas(self, entradas):
    salidas = []
    for neurona in self.neuronas:
      salidas.append(neurona.calcular_salida(entradas))
    return salidas

  def devolver_salidas():
    salidas = [] 
    for neurona in self.neuronas:
      salidas.append(neurona.evaluacion)
    return salidas

###############################################################################
#############################        NEURONA       ############################
###############################################################################
class Neurona:

  def __init__(self, bias):
    self.bias = bias
    self.pesos = []

  def calcular_salida(self, entradas):
    self.entradas = entradas
    self.evaluacion = self.funcion_logistica(self.calcular_entrada_total())
    return self.evaluacion

  def calcular_entrada_total(self):
    total = 0
    for i in range(len(self.entradas)):
      total += self.entradas[i] * self.pesos[i]
    return total + self.bias

  def funcion_logistica(self, x):
    return 1 / (1 + math.exp(-x))

  def derivada_error_respecto_entrada_total_red(self, valor_objetivo):
    return self.derivada_error_respecto_salida(valor_objetivo) * self.derivada_funcion_logistica()

  def derivada_error_respecto_salida(self,valor_objetivo):
    return -(valor_objetivo - self.evaluacion)

  def derivada_funcion_logistica(self):
    return self.evaluacion * (1 - self.evaluacion)
 
  def derivada_entrada_total_red_respecto_peso(self,index):
    return self.entradas[index]

  def calcular_error(self, valor_objetivo):
    return 0.5 * (valor_objetivo - self.evaluacion) ** 2

data_set_1 = DataSetEjercicio1.leer_data_set("data_sets/Ejercicio1/datos_P1_RN_EM2016_n500.txt")
data_set_2 = DataSetEjercicio1.leer_data_set("data_sets/Ejercicio1/datos_P1_RN_EM2016_n1000.txt")
data_set_3 = DataSetEjercicio1.leer_data_set("data_sets/Ejercicio1/datos_P1_RN_EM2016_n2000.txt")
data_set_4 = DataSetEjercicio1.leer_data_set("data_sets/Ejercicio1/500_DataSet")
data_set_5 = DataSetEjercicio1.leer_data_set("data_sets/Ejercicio1/1000_DataSet")
data_set_6 = DataSetEjercicio1.leer_data_set("data_sets/Ejercicio1/2000_DataSet")

for j in range(2,11):

  nn = RedNeural(len(data_set_3[0][0]), j, len(data_set_3[0][1]))
  tiempo = time.time()

  for i in (range(len(data_set_3))):
    entradas_entrenamiento = data_set_3[i][0]
    salidas_entrenamiento = data_set_3[i][1]
    nn.entrenar(entradas_entrenamiento, salidas_entrenamiento)

  print(len(data_set_3[0][0]),j,nn.calcular_error_total(data_set_3),time.time() - tiempo)

# data_set_7a = DataSetIris.obtener_data_set_binario("iris75.data")
# data_set_7b = DataSetIris.obtener_data_set_ternario("iris75.data")
# data_set_8a = DataSetIris.obtener_data_set_binario("iris90.data")
# data_set_8b = DataSetIris.obtener_data_set_ternario("iris90.data")
# data_set_9a = DataSetIris.obtener_data_set_binario("iris105.data")
# data_set_9b = DataSetIris.obtener_data_set_ternario("iris105.data")
# data_set_10a = DataSetIris.obtener_data_set_binario("iris120.data")
# data_set_10b = DataSetIris.obtener_data_set_ternario("iris120.data")
# data_set_11a = DataSetIris.obtener_data_set_binario("iris135.data")
# data_set_11b = DataSetIris.obtener_data_set_ternario("iris135.data")
# try:
#     f = open('Resultados.txt', 'w') 
#     for j in range(4,11):
#     nn = RedNeural(len(data_set_11b[0][0]), j, len(data_set_11b[0][1]))
#     tiempo = time.time()

#     for i in (range(len(data_set_11b))):
#       entradas_entrenamiento = data_set_11b[i][0]
#       salidas_entrenamiento = data_set_11b[i][1]
#       nn.entrenar(entradas_entrenamiento, salidas_entrenamiento)

#     f.write(str(j)+" "+str(nn.calcular_error_total(data_set_11b))+" "+str(time.time() - tiempo)+"\n")
#     f.close()
# except IOError as e:
#     print "I/O error({0}): {1}".format(e.errno, e.strerror)