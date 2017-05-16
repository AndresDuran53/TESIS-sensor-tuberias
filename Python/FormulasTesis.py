'''
Usuario Final Ingresa:
-nombreTuberia::TEXT
-elevacionEntrada::DOUBLE
-elevacionSalida::DOUBLE
-longitudTuberia::DOUBLE
-materialTuberia::TEXT (PVC,Concreto,NovaFort)
            PVC:      0.010
            Concreto: 0.013
            NovaFort: 0.009
-formaTuberia::TEXT (Circular)
-diametroTuberia::DOUBLE
-nivelTeoricoAltura::DOUBLE
-porcentajeMaximoAltura::DOUBLE
'''

#n = materialTuberia
#AD = datoTabla
#RD = datoTabla
#PD = datoTabla 
A = AD**2 * diametroTuberia**2
R = RD*diametroTuberia
P = PD*diametroTuberia
pendiente = (elevacionEntrada - elevacionOutput) / longitudTuberia # = S
caudal = (1/n) * ((R**5/3)/(P**2/3)) * (pendiente**1/2) # = Q

tiranteActual = diametroTuberia-lecturaSensor # = yActual
tCritico = porcentajeMaximoAltura*diametroTuberia
velocidadCorriente = (1/n) * (R**2/3) * (pendiente**1/2) # = V
porcentajeCaudalActual = (tiranteActual*100/diametroTuberia)
caudal = (1/n) * ((R**5/3)/(P**2/3)) * (pendiente**1/2) # = Q

#Tiempo = segundos
velocidadAcenso = (tiranteActual-tiranteAnterior)/(TiempoActual-TiempoAnterior) #60
distanciaLectura = velocidadAcenso*Tiempo

