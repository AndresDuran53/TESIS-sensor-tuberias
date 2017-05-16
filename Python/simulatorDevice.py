import requests
import tkinter
import time
from random import randint

hostIp = "192.168.0.61"
idTuberia="1"
alturaActual=0
'''
while True:
    alturaActual=(randint(0,100))/100
    print("Altura Actual:",alturaActual)
    requests.get("http://"+hostIp+"/actualizar_estado_tuberia.php",
                    data={"id":idTuberia,"altura":alturaActual})
    time.sleep(10)
'''

r = requests.get("http://zarus.cr/registro_tuberia.php?nick=nickName&ubicacion=SanPedro&diametro=2&eleen=2&elesa=2&forma=1&altura=2&caudal=2&tiempo=20")
