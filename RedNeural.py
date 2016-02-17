# Archivo: RedNeural.py
# Este archivo contiene las clases utilizadas para la implementacion de una
# red neural.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import random
import math

###############################################################################
#############################      RED NEURAL      ############################
###############################################################################
class RedNeural: 
  APRENDIZAJE = 0.5

  def __init__(self, cantidadEntradas, cantidadNeuronas, cantidadSalidas, pesosNeuronas, biasNeuronas = None, pesosSalidas, biasSalidas = None):
    self.cantidadEntradas = cantidadEntradas
    self.capa_oculta = CapaNeuronas(cantidadNeuronas,biasNeuronas)
    self.capa_salida = CapaNeuronas(cantidadSalidas,biasSalidas)
    self.inicializar_pesos_entrada_ocultos(pesosNeuronas)
    self.inicializar_pesos_ocultos_salida(pesosSalidas)

  def inicializar_pesos_entrada_ocultos(self, pesosNeuronas):
    for i in range(len(self.capa_oculta.neuronas)):
      for j in range(self.cantidadEntradas):
          self.capa_oculta.neuronas[i].pesos.append(pesosNeuronas[n])
          n += 1 

  def inicializar_pesos_ocultos_salida(self, pesosSalidas):
    for i in range(len(self.capa_salida.neuronas)):
      for j in range(self.capa_oculta.neuronas):
          self.capa_salida.neuronas[i].pesos.append(pesosSalidas[n])
          n += 1 

  def inspect(self):
    print('------')
    print('Entradas: {}'.format(self.num_inputs))
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
    self.bias = bias
    self.neuronas = []
    for i in range(cantidad):
      self.neuronas.append(Neurona(self.bias))

  def inspect():

  def calcular_salidas():
    salidas = []
    for neurona in self.neuronas:
      salidas.append(neurona.calcular_salida(entradas)) 

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
    self.salidas = [] 

  def calcular_salida(self, entradas):
    self.entradas = entradas
    self.evaluacion = self.funcion_logistica(self.calcular_entrada_total())
    return self.evaluacion

  def calcular_entrada_total(self):
    total = 0
    for i in range(len(self.inputs)):
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
