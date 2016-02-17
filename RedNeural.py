# Archivo: RedNeural.py
# Este archivo contiene las clases utilizadas para la implementacion de una
# red neural.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import random
import math
import DataSetEjercicio1

###############################################################################
#############################      RED NEURAL      ############################
###############################################################################
class RedNeural: 
  APRENDIZAJE = 0.5 # Constante de aprendizaje.

  def __init__(self, cantidadEntradas, cantidadNeuronas, cantidadSalidas, 
               pesosNeuronas = None, biasNeuronas = None, pesosSalidas = None, 
               biasSalidas = None):
    self.cantidadEntradas = cantidadEntradas
    self.capa_oculta = CapaNeuronas(cantidadNeuronas,biasNeuronas)
    self.capa_salida = CapaNeuronas(cantidadSalidas,biasSalidas)
    self.inicializar_pesos_entrada_ocultos(pesosNeuronas)
    self.inicializar_pesos_ocultos_salida(pesosSalidas)

  def inicializar_pesos_entrada_ocultos(self, pesosNeuronas):
    d = 1 / math.sqrt(self.cantidadEntradas) # Numero utilizado para el rango de los pesos.
    num_peso = 0
    for i in range(len(self.capa_oculta.neuronas)):
      for j in range(self.cantidadEntradas):
          if not pesosNeuronas:
            self.capa_oculta.neuronas[i].pesos.append(random.uniform(-d,d))
          else:
            self.capa_oculta.neuronas[i].pesos.append(pesosNeuronas[num_peso])
          num_peso += 1 

  def inicializar_pesos_ocultos_salida(self, pesosSalidas):
    d = 1 / math.sqrt(self.cantidadEntradas) # Numero utilizado para el rango de los pesos.
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
        errorRespectoPeso = erroresDerivadasRespectoNeuronasOcultas[i] * self.capa_oculta.neuronas[i].derivada_entrada_total_red_respecto_peso(j)
        self.capa_oculta.neuronas[i].pesos[j] -= self.APRENDIZAJE * errorRespectoPeso

    for i in range(len(self.capa_oculta.neuronas)):
      for j in range(len(self.capa_oculta.neuronas[i].pesos)):
        errorRespectoPeso = erroresDerivadasRespectoNeuronasOcultas[i] * self.capa_oculta.neuronas[i].derivada_entrada_total_red_respecto_peso(j)
        self.capa_oculta.neuronas[i].pesos[j] -= self.APRENDIZAJE * errorRespectoPeso

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
    return derivada_error_respecto_salida(valor_objetivo) * derivada_funcion_logistica();

  def derivada_error_respecto_salida(self,valor_objetivo):
    return -(valor_objetivo - self.evaluacion)

  def derivada_funcion_logistica(self):
    return self.evaluacion * (1 - self.evaluacion)
 
  def derivada_entrada_total_red_respecto_peso(self,index):
    return self.entradas[index]

  def calcular_error(self, valor_objetivo):
    return 0.5 * (valor_objetivo - self.evaluacion) ** 2


entradas,salidas = DataSetEjercicio1.generar_data_set_lista(4)
print entradas
print salidas

nn = RedNeural(4, 2, 2, biasNeuronas = 0.5, biasSalidas = 0.5)
nn.alimentar_neuronas(entradas)
nn.inspect()