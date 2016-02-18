data_set_1 = DataSetEjercicio1.leer_data_set("datos_P1_RN_EM2016_n500.txt")
data_set_2 = DataSetEjercicio1.leer_data_set("datos_P1_RN_EM2016_n1000.txt")
data_set_3 = DataSetEjercicio1.leer_data_set("datos_P1_RN_EM2016_n2000.txt")
data_set_4 = DataSetEjercicio1.leer_data_set("500_DataSet")
data_set_5 = DataSetEjercicio1.leer_data_set("1000_DataSet")
data_set_6 = DataSetEjercicio1.leer_data_set("2000_DataSet")

data_set = data_set_1 + data_set_2 + data_set_3 + data_set_4 + data_set_5 + data_set_6
nn = RedNeural(len(data_set[0][0]), 2, len(data_set[0][1]))

for i in (range(len(data_set))):
  entradas_entrenamiento = data_set[i][0]
  salidas_entrenamiento = data_set[i][1]
  nn.entrenar(entradas_entrenamiento, salidas_entrenamiento)
  print(i, nn.calcular_error_total(data_set))