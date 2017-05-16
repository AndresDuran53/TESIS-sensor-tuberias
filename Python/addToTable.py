import pymysql

db = pymysql.connect("192.168.0.61", "user", "1234", "BD_Alcantarillas")
curs=db.cursor()
try:
    curs.execute ("""INSERT INTO tbl_tuberia
                  (nickname_tuberia,
 ubicacion_tuberia, diametro_tuberi, elevacion_entrada,
elevacion_salida, forma_tuberia, altura_maxima_tuberia,
cudal_maximo, tiempo_llenado, status, tbl_status_id_status, tbl_forma_tuberia_id_forma_tuberia,
tbl_material_tuberia_id_material_tuuberia)
            values(
"a",
"b",
1,
2,
3,
4,
5,
6,
7,
2,
2,
2,
1)""")
    db.commit()
    print ("Data committed")
except:
    print ("Error: the database is being rolled back")
    db.rollback()
