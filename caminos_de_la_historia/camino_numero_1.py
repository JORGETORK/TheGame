# juego creado por JORGETORK
 
import os
import datetime 
import subprocess 
import sys 
import time
from io import open
from menus_de_preguntas_de_los_hostales import Menu_de_preguntas_hostal_1

def camino():
  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()

  archivo.close()
  Ahora = datetime.datetime.now()
  print("muy bien " + texto[1].rstrip("\n") + " has elejido ir por la izquierda")
  camino_1 = int(input("Hace ya 3 dias que tu historia comenzó te aventuraste sin rumbo has caminado mucho y descansado muy poco pero que suerte te encontraste un hostal\n ¿quieres entrar?\n 1)si\n 2)no\n Elije una opcion: "))
  os.system ("clear")

  if camino_1 == 1 :

    Archivo = open("Tu Historia De TheGame.txt","w")

    Archivo.write("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + texto[2].rstrip("\n") + " para ir en busca de tu hermano " + texto[5].rstrip("\n") + " que fue secuestrado por " + texto[3].rstrip("\n") + ".\n")
    Archivo.write("Te han revelado que " + texto[3].rstrip("\n") +" y tu padre " + texto[4].rstrip("\n") + " tenian una fuerte rivalidad porque alguna ves fueron aprendices del guerrero mas grande de toda la historia, pero tu padre demostro ser mucho mas poderoso y tener mas corazon.\n Sin embargo tu padre fallecio hace ya 10 años por su gran corazon al proteger a este mundo de las mas grandes amenasas,\n amenasas que ahora estan a punto de ser liveradas y por eso necesitas rescatar a tu hermano para juntar su fragemnto del mapa con el tuyo para averiguar como tu padre salvo al mundo.\n")
    Archivo.write("Por el momento solo has llegado hasta el hostal de JA Silva")

    Archivo.close()
    print(Ahora)
    print("Entrando al hostal")
    print("[                    ] 0% ")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Entrando al hostal")
    print("[=====               ] 25%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Entrando al hostal")
    print("[==========          ] 50%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Entrando al hostal")
    print("[===============     ] 75%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Entrando al hostal")
    print("[===================] 100%")
    time.sleep(2)
    os.system ("clear")
    print("Bienvenido al hostal de JA Silva")
    print("(se guardo una copia de la historia en un archivo .txt en la carpeta del juego por si te interesa.)")
    print("Bien " + texto[1].rstrip("\n") + " ya estas dentro del hostal ¿que quieres hacer?\n")
    acciones_del_hostal_1()
      

  elif camino_1 == 2 :
    print("que mal quien sabe cuando encontraras otro buen lugar para descansar")

#esta es la accion basica para los hostales dentro del juego
def acciones_del_hostal_1():
  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()

  archivo.close()
  Ahora = datetime.datetime.now()
  Menu_de_opciones_del_hotal = int(input("Menu de opciones:\n 1)Dormir\n 2)Comer\n 3)Hacer una pregunta al dueño\n 4)salir\n Elije una opcion: "))
  os.system ("clear")

  if Menu_de_opciones_del_hotal == 1:
    print("muy bien " + texto[1].rstrip("\n") + " que suerte te toco una cama muy comoda a dormir un poco")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Durmiendo")
    print("[                    ] 0% ")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Durmiendo")
    print("[=====               ] 25%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Durmiendo")
    print("[==========          ] 50%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Durmiendo")
    print("[===============     ] 75%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Durmiendo")
    print("[===================] 100%")
    time.sleep(2)
    os.system ("clear")
    print("Que increible descanso")
    time.sleep(1)
    os.system ("clear")
    print("sigues dentro del hostal ¿que quieres hacer?\n")
    acciones_del_hostal_1()


  elif Menu_de_opciones_del_hotal == 2:
    print("Bien " + texto[1].rstrip("\n") + " vamos a sentarnos a comer")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Comiendo")
    print("[                    ] 0% ")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Comiendo")
    print("[=====               ] 25%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Comiendo")
    print("[==========          ] 50%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Comiendo")
    print("[===============     ] 75%")
    time.sleep(2)
    os.system ("clear")
    print(Ahora)
    print("Comiendo")
    print("[===================] 100%")
    time.sleep(2)
    os.system ("clear")
    print("Que deliciosa comida")
    time.sleep(1)
    os.system ("clear")
    print("sigues dentro del hostal ¿que quieres hacer?\n")
    acciones_del_hostal_1()

  elif Menu_de_opciones_del_hotal == 3:
    print("¿Que quieres preguntar?:\n")
    preguntas_dueño_del_hostal_1()

  elif Menu_de_opciones_del_hotal == 4:
      print(Ahora)
      print("Saliendo del hostal")
      print("[                    ] 0% ")
      time.sleep(2)
      os.system ("clear")
      print(Ahora)
      print("Saliendo del hostal")
      print("[=====               ] 25%")
      time.sleep(2)
      os.system ("clear")
      print(Ahora)
      print("Saliendo del hostal")
      print("[==========          ] 50%")
      time.sleep(2)
      os.system ("clear")
      print(Ahora)
      print("Saliendo del hostal")
      print("[===============     ] 75%")
      time.sleep(2)
      os.system ("clear")
      print(Ahora)
      print("Saliendo del hostal")
      print("[===================] 100%")
      time.sleep(2)
      os.system ("clear")
      retomando_camino_1()

#las preguntas a los dueños barian dependiendo el numero del hostal 
def preguntas_dueño_del_hostal_1():
  Menu_de_preguntas_hostal = int(input("1)Preguntar sobre mi hermano\n 2)Preguntar sobre mi padre\n 3)Preguntar por un buen camino\n 4)Dejar de preguntar\n Elije una opcion: "))

  if Menu_de_preguntas_hostal == 1:
    os.system("clear")
    Menu_de_preguntas_hostal_1.preguntas_sobre_mi_hermano()

  elif Menu_de_preguntas_hostal == 4:
    os.system("clear")
    acciones_del_hostal_1()


#Aqui se pondran los caminos a retomar al salir de los hostales hay una gran variedad de caminos a tomar
def retomando_camino_1():
  print("bien ya que descansaste un poco vamoa a retomar el camino")