

datos= read.table("archivo.txt") 

attach(d)
names(d)

plot(d[ d$V3 == "1" ,]$V1,d[ d$V3 == "-1" ,]$V2,main="Distribucion de predicciones",col=c("black","firebrick3"),pch=16,sub="Negro positivas,Rojo negativas")