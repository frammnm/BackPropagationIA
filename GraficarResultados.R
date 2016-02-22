

dd = read.table("resultados/10000-Puntos/Resultados_Nosotros.txt") 

attach(dd)
names(dd)
plot(0:20,0:20,type = "n",main="Distribucion de predicciones",sub="Morado positivas,Gris negativas")
symbols(10,10,7,add=TRUE)
points(dd[ dd$V3 == "1" ,]$V1,dd[ dd$V3 == "1" ,]$V2,col="mediumorchid3",pch=3)
points(dd[ dd$V3 == "0" ,]$V1,dd[ dd$V3 == "0" ,]$V2,col="dimgray",pch=4)
