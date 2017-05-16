import pymysql
import requests
import time

def getInfoTuberia(idNickname):
    lista=[]
    db = pymysql.connect("127.0.0.1", "root", "1234", "BD_Alcantarilla")
    curs=db.cursor()
    curs.execute ("SELECT diametro, elevacion_entrada, elevacion_salida, longitud, altura_momental, material, y_d FROM tbl_tuberia WHERE nickname_tuberia = '" + idNickname  +"'")
    for reading in curs.fetchall():
        for valor in reading:
            lista.append(valor)
            print(valor)
    return lista

def getValorMaterial(material):
    db = pymysql.connect("127.0.0.1", "root", "1234", "BD_Alcantarilla")
    curs=db.cursor()
    curs.execute ("SELECT n_maning_tuberia FROM tbl_material WHERE material_tuberia = '"+ material  +"'")
    for reading in curs.fetchall():
        print(material,": ",reading[0])
        return reading[0]
    print("")

def getX_D(yd):
    lista=[]
    db = pymysql.connect("127.0.0.1", "root", "1234", "BD_Alcantarilla")
    curs=db.cursor()
    curs.execute ("SELECT * FROM tbl_tcritico_circular WHERE y_d = "+str(yd))
    for reading in curs.fetchall():
        lista.append(reading[1])
        lista.append(reading[2])
        lista.append(reading[3])
        print("--------------------------")
        print("a_d: ",lista[0])
        print("p_d: ",lista[1])
        print("r_d: ",lista[2])
        print("--------------------------")
    print("")
    return lista

#Calculos-----

def getPendiente(elevacionEntrada,elevacionSalida,longitudTuberia):
    return (elevacionEntrada - elevacionSalida) / longitudTuberia

def getCaudal(n,R,P,pendiente):
    return (1/n) * ((R**5/3)/(P**2/3)) * (pendiente**1/2)

def getTiranteActual(diametroTuberia,lecturaSensor):
    return diametroTuberia-lecturaSensor

def getT_Critico(porcentajeMaximoAltura,diametroTuberia):
    return porcentajeMaximoAltura*diametroTuberia

def getVelocidadCorriente(n,R,pendiente):
    return (1/n) * (R**2/3) * (pendiente**1/2)

def getPorcentajeCaudalActual(tiranteActual,diametroTuberia):
    return (tiranteActual*100/diametroTuberia)

def getVelocidadAcenso(tiranteActual,tiranteAnterior,TiempoActual,TiempoAnterior):
    return (tiranteActual-tiranteAnterior)/(TiempoActual-TiempoAnterior)



def getDatos():
    lista = getInfoTuberia("tub1")
    valorPorMaterial = float(getValorMaterial(lista[-2]))
    lista[-2]=valorPorMaterial
    lista_x_d = getX_D(lista[-1])
    lista.append(lista_x_d[1])
    lista.append(lista_x_d[2])
    print("Lista: ",lista)

    diametroTuberia=lista[0]
    elevacionEntrada=lista[1]
    elevacionSalida=lista[2]
    longitudTuberia=lista[3]
    lecturaSensor=lista[4]
    n=lista[5]
    porcentajeMaximoAltura=lista[6]
    PD=lista[7]
    RD=lista[8]
    
    P = PD*diametroTuberia
    R = RD*diametroTuberia

    pendiente = getPendiente(elevacionEntrada,elevacionSalida,longitudTuberia)
    caudal = getCaudal(n,R,P,pendiente)
    tiranteActual = getTiranteActual(diametroTuberia,lecturaSensor)
    t_Critico = getT_Critico(porcentajeMaximoAltura,diametroTuberia)
    velocidadCorriente = getVelocidadCorriente(n,R,pendiente)

    print("Pendiente: ", pendiente)
    print("Caudal: ", caudal)
    print("Tirante Actual: ", tiranteActual)
    print("Tirante Critico: ", t_Critico)
    print ("Velocidad Corriente: ", velocidadCorriente)


def enviarDatosPHP(altura,hora,velocidad,tirante,q_ins):
    infoTub = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('http://zarus.cr/registro_valores.php', params=infoTub)

def main():
    while(True):
        getDatos()
        time.sleep(60)

main()
