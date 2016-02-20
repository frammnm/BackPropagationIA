# Archivo: red_neural.py
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

  def __init__(self, cantidadEntradas, cantidadNeuronas, cantidadSalidas, 
               pesosNeuronas = None, biasNeuronas = None, pesosSalidas = None, 
               biasSalidas = None, aprendizaje = 0.5):
    self.cantidadEntradas = cantidadEntradas
    self.cantidadSalidas = cantidadSalidas
    self.capa_oculta = CapaNeuronas(cantidadNeuronas,biasNeuronas)
    self.capa_salida = CapaNeuronas(cantidadSalidas,biasSalidas)
    self.APRENDIZAJE = aprendizaje
    self.inicializar_pesos_entrada_ocultos(pesosNeuronas)
    self.inicializar_pesos_ocultos_salida(pesosSalidas)

  def __str__(self):
    string = '------\n'
    string += 'Entradas: {}\n'.format(self.cantidadEntradas)
    string += '------\n'
    string += 'Capa oculta\n'
    string += str(self.capa_oculta)+"\n"
    string += '------\n'
    string += 'Capa salida\n'
    string += str(self.capa_salida)+"\n"
    string += '-------'
    return string

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

  def alimentar_neuronas(self, entradas):
    salidasOcultas = self.capa_oculta.calcular_salidas(entradas)
    return self.capa_salida.calcular_salidas(salidasOcultas)

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

  def __str__(self):
    string = 'Neuronas: '+str(len(self.neuronas))+"\n"
    for n in range(len(self.neuronas)):
      string += ' Neurona '+str(n)+"\n"
      string += ' Evaluacion '+str(self.neuronas[n].evaluacion)+"\n"
      for w in range(len(self.neuronas[n].pesos)):
        string += '  Peso: '+str(self.neuronas[n].pesos[w])+"\n"
      string += '  Bias: '+str(self.bias)+"\n"
    return string

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