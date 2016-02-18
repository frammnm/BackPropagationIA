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
    puntos_y_salidas = []
    f = open(nombre,'r') 
    datos = f.readlines()
    for linea in datos:
        palabras = linea.split(",")
        print palabras
        x = (float(palabras[0]))
        y = (float(palabras[1]))
        z = (float(palabras[2]))
        w = (float(palabras[3]))
        puntos_y_salidas.append([[x,y,z,w],[palabras[4]]])
    f.close()
    return puntos_y_salidas
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    return []