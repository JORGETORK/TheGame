#historia del juego

import os
import datetime 
import subprocess 
import sys 
import time
from io import open
from caminos_de_la_historia import camino_numero_1

def inicio_del_juego():
  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()

  archivo.close()

  Ahora = datetime.datetime.now()
  print(Ahora)
  print("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + texto[2].rstrip("\n") + " para ir en busca de tu hermano " + texto[5].rstrip("\n") + " que fue secuestrado por " + texto[3].rstrip("\n") + ".")
  print("Te han revelado que " + texto[3].rstrip("\n") +" y tu padre " + texto[4].rstrip("\n") + " tenian una fuerte rivalidad porque alguna ves fueron aprendices del guerrero mas grande de toda la historia, pero tu padre demostro ser mucho mas poderoso y tener mas corazon.\n Sin embargo tu padre fallecio hace ya 10 años por su gran corazon al proteger a este mundo de las mas grandes amenasas,\n amenasas que ahora estan a punto de ser liveradas y por eso necesitas rescatar a tu hermano para juntar su fragemnto del mapa con el tuyo para averiguar como tu padre salvo al mundo.\n")
  primer_movimiento = int(input("Bien ya que tienes todo listo y has salido del pueblo te encontraste dos caminos uno por la izquierda y otro por la derecha\n 1)izquierda\n 2)derecha\n ¿por cual camino quiere ir 1 o 2?: "))
  os.system ("clear")

  if primer_movimiento == 1 :
    camino_numero_1.camino()

  elif primer_movimiento == 2 :
    print("muy bien " + texto[1].rstrip("\n") + " has elejido ir por la derecha")
    camino_2 = int(input("Tu historia comensó hace ya 3 dias te estas quedando sin proviciones y no has descansado en un buen lugar, ¿quieres seguir por este camino?\n 1)quiero regresar y tomar el camino 1\n 2)seguire por aqui\n elije una opcion: "))

    if camino_2 == 1 :
      print("Muy bien " + texto[1].rstrip("\n") + " regresemos al camino de la izquierda")
      time.sleep(1)
      os.system ("clear")
      print("REGRESANDO AL CAMINO DE LA IZQUIERDA")
      print(Ahora)
      print("[                    ] 0% ")
      time.sleep(.5)
      os.system ("clear")
      print("REGRESANDO AL CAMINO DE LA IZQUIERDA")
      print(Ahora)
      print("[=====               ] 25%")
      time.sleep(.5)
      os.system ("clear")
      print("REGRESANDO AL CAMINO DE LA IZQUIERDA")
      print(Ahora)
      print("[==========          ] 50%")
      time.sleep(.5)
      os.system ("clear")
      print("REGRESANDO AL CAMINO DE LA IZQUIERDA")
      print(Ahora)
      print("[===============     ] 75%")
      time.sleep(.5)
      os.system ("clear")
      print("REGRESANDO AL CAMINO DE LA IZQUIERDA")
      print(Ahora)
      print("[====================] 100%")
      time.sleep(.5)
      os.system ("clear")

      camino_numero_1.camino()
    
    elif camino_2 == 2 :
      print("Deacuerdo seguiremos por este camino espero te queden fuersas porque a lo lejos se ve un pequeño pueblo")
