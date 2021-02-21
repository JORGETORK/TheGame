# juego creado por JORGETORK
 
import os
import datetime 
import subprocess 
import sys 
import time
from time import sleep
from io import open
from colorama import Cursor, init, Fore, Back, Style
from acciones_de_hostales import hostal_1

def camino():
  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()

  archivo.close()

  archivo_1 = open(".stats.txt","r")

  texto_1 = archivo_1.readlines()

  archivo_1.close()
  Ahora = datetime.datetime.now()
  print(Ahora)
  print("como ves ya cambiaron tus stats porque al lejir este camino has caminado mucho")
  print("Dinero: $" + texto_1[0].rstrip("\n") + " Energia: " + texto_1[1].rstrip("\n") + "%" +" comida: " + texto_1[2].rstrip("\n") + "%")
  print("muy bien " + texto[1].rstrip("\n") + " has elejido ir por la izquierda")
  camino_1 = input("Hace ya 3 dias que tu historia comenzó te aventuraste sin rumbo has caminado mucho y descansado muy poco pero que suerte te encontraste un hostal\n ¿quieres entrar?\n 1)si\n 2)no\n Elije una opcion: ")
  os.system ("clear")

  if camino_1 == "1" :

    Archivo = open("Tu Historia De TheGame.txt","w")

    Archivo.write("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + texto[2].rstrip("\n") + " para ir en busca de tu hermano " + texto[5].rstrip("\n") + " que fue secuestrado por " + texto[3].rstrip("\n") + ".\n")
    Archivo.write("Te han revelado que " + texto[3].rstrip("\n") +" y tu padre " + texto[4].rstrip("\n") + " tenian una fuerte rivalidad porque alguna ves fueron aprendices del guerrero mas grande de toda la historia, pero tu padre demostro ser mucho mas poderoso y tener mas corazon.\n Sin embargo tu padre fallecio hace ya 10 años por su gran corazon al proteger a este mundo de las mas grandes amenasas,\n amenasas que ahora estan a punto de ser liveradas y por eso necesitas rescatar a tu hermano para juntar su fragemnto del mapa con el tuyo para averiguar como tu padre salvo al mundo.\n")
    Archivo.write("Por el momento solo has llegado hasta el hostal de JA Silva")

    Archivo.close()
    init()
    print(Ahora)
    print("ENTRANDO AL HOSTAL... ")
    for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
      sleep(2)
      print(Cursor.UP(1)+Cursor.FORWARD(21)+str(arch))
    os.system("clear")
    print("Bienvenido al hostal de JA Silva")
    print("(se guardo una copia de la historia en un archivo .txt en la carpeta del juego por si te interesa.)")
    print("Bien " + texto[1].rstrip("\n") + " ya estas dentro del hostal ¿que quieres hacer?\n")
    hostal_1.acciones_del_hostal_1()
      

  elif camino_1 == "2" :
    print("que mal quien sabe cuando encontraras otro buen lugar para descansar")

  else:
    os.system ("clear")
    print("Elije una opcion valida")
    camino()