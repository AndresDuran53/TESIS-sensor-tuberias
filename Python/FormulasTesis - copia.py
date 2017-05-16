
diametroTuberia = 2
elevacionEntrada = 3
elevacionSalida = 5
longitudTuberia = 10
lecturaSensor = 1
porcentajeMaximoAltura = 0.9
tiranteAnterior=1

n = 0.013
#AD = 0.5872
PD = 1.9823
RD = 0.2962

#A = AD**2 * diametroTuberia**2
P = PD*diametroTuberia
R = RD*diametroTuberia

pendiente = (elevacionEntrada - elevacionSalida) / longitudTuberia # = S
caudal = (1/n) * ((R**5/3)/(P**2/3)) * (pendiente**1/2) # = Q

tiranteActual = diametroTuberia-lecturaSensor # = yActual
tCritico = porcentajeMaximoAltura*diametroTuberia
velocidadCorriente = (1/n) * (R**2/3) * (pendiente**1/2) # = V
porcentajeCaudalActual = (tiranteActual*100/diametroTuberia)


#Tiempo = segundos
#velocidadAcenso = (tiranteActual-tiranteAnterior)/(TiempoActual-TiempoAnterior) #60
#distanciaLectura = velocidadAcenso*Tiempo

