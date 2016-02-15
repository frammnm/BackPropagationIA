# Archivo: dataSetGenerator.py
# Este archivo contiene el metodo generador del data Set para el ejercicio
# 1.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import random

# Generates a data set of numbers inside the area of a square.
def generateDataSet(n):
  nc = 0 # The number of points inside the area of a circle.
  ns = 0 # The number of points inside the area of a square.
  i = 0
  
  try:
    f = open(str(n)+'_DataSet', 'w') 
  
    while (i < n):

      x = random.uniform(0,20)
      y = random.uniform(0,20)
      point = (x - 10)**2 + (y - 10)**2
  
      if ((point <= 49) and (nc < n/2)):
        nc += 1
        f.write(str(x)+' '+str(y)+' -1\n')
      elif ((point <= 49) and (nc >= n/2)):
        continue
      elif ((point > 49) and (ns < n/2)):
        ns += 1
        f.write(str(x)+' '+str(y)+' 1\n')
      elif ((point > 49) and (ns >= n/2)):
        continue
      i += 1
	  
    f.close()
    return

  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

generateDataSet(500)
generateDataSet(1000)
generateDataSet(2000)
    