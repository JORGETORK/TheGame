import os
import datetime 
import subprocess 
import sys 
import time
from time import sleep
from io import open
from colorama import Cursor, init, Fore, Back, Style
from menus_de_preguntas_de_los_hostales import Menu_de_preguntas_hostal_1

def acciones_del_hostal_1():
  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()

  archivo.close()

  archivo_1 = open(".stats.txt","r")

  texto_1 = archivo_1.readlines()

  archivo_1.close()
  print("Dinero: $" + texto_1[0].rstrip("\n") + " Energia: " + texto_1[1].rstrip("\n") + "%" + " comida: " + texto_1[2].rstrip("\n") + "%")
  Ahora = datetime.datetime.now()
  Menu_de_opciones_del_hotal = input("Menu de opciones:\n 1)Dormir(costo $20)\n 2)Comer(costo $20)\n 3)Hacer una pregunta al dueño\n 4)salir\n Elije una opcion: ")
  os.system ("clear")

  if Menu_de_opciones_del_hotal == "1":

    verificar_1 = int(texto_1[1].rstrip("\n"))

    if verificar_1 == 100:
      os.system("clear")
      print("lo siento tienes la energia completa no puedes dormir")
      time.sleep(2)
      os.system("clear")
      print("Elije otra opcion\n")
      acciones_del_hostal_1()

    else:
      os.system("clear")
      print("muy bien " + texto[1].rstrip("\n") + " que suerte te toco una cama muy comoda a dormir un poco")
      time.sleep(2)
      os.system ("clear")
      init()
      print(Ahora)
      print("DURMIENDO... ")
      for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
        sleep(2)
        print(Cursor.UP(1)+Cursor.FORWARD(12)+str(arch))
      os.system("clear")
      print("Que increible descanso")
      time.sleep(1)
      os.system ("clear")
      suma = int(texto_1[0].rstrip("\n"))-20
      suma_2 = int(texto_1[1].rstrip("\n"))+25
      suma_3 = int(texto_1[2].rstrip("\n"))-3

      verificar = suma_2

      if verificar <=100:
        archivo_2 = open(".stats.txt","w")
        archivo_2.write(str(suma) + "\n")
        archivo_2.write(str(suma_2) + "\n")
        archivo_2.write(str(suma_3) + "\n")
        archivo_2.close()
        os.system("clear")

      elif verificar >=100:
        archivo_2 = open(".stats.txt","w")
        archivo_2.write(str(suma) + "\n")
        archivo_2.write(str(100) + "\n")
        archivo_2.write(str(suma_3) + "\n")
        archivo_2.close()
        os.system("clear")


      print("sigues dentro del hostal ¿que quieres hacer?\n")
      acciones_del_hostal_1()


  elif Menu_de_opciones_del_hotal == "2":

    verificar_1 = int(texto_1[2].rstrip("\n"))

    if verificar_1 == 100:
      os.system("clear")
      print("lo siento estas lleno no puedes comer mas")
      time.sleep(2)
      os.system("clear")
      print("Elije otra opcion\n")
      acciones_del_hostal_1()

    else:
      print("Bien " + texto[1].rstrip("\n") + " vamos a sentarnos a comer")
      time.sleep(2)
      os.system ("clear")
      init()
      print(Ahora)
      print("COMIENDO... ")
      for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
        sleep(2)
        print(Cursor.UP(1)+Cursor.FORWARD(11)+str(arch))
      os.system("clear")
      print("Que deliciosa comida")
      time.sleep(1)
      os.system ("clear")
      suma = int(texto_1[0].rstrip("\n"))-20
      suma_2 = int(texto_1[1].rstrip("\n"))-2
      suma_3 = int(texto_1[2].rstrip("\n"))+25

      verificar = suma_3

      if verificar <=100:
        archivo_2 = open(".stats.txt","w")
        archivo_2.write(str(suma) + "\n")
        archivo_2.write(str(suma_2) + "\n")
        archivo_2.write(str(suma_3) + "\n")
        archivo_2.close()
        os.system("clear")

      elif verificar >=100:
        archivo_2 = open(".stats.txt","w")
        archivo_2.write(str(suma) + "\n")
        archivo_2.write(str(suma_2) + "\n")
        archivo_2.write(str(100) + "\n")
        archivo_2.close()
        os.system("clear")

    
      print("sigues dentro del hostal ¿que quieres hacer?\n")
      acciones_del_hostal_1()

  elif Menu_de_opciones_del_hotal == "3":
    print("¿Que quieres preguntar?:\n")
    preguntas_dueño_del_hostal_1()

  elif Menu_de_opciones_del_hotal == "4":
      init()
      print(Ahora)
      print("SALIENDO DEL HOSTAL... ")
      for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
        sleep(2)
        print(Cursor.UP(1)+Cursor.FORWARD(22)+str(arch))
      os.system("clear")
      retomando_camino_1()

  else:
    os.system("clear")
    print("Elije una opcion valida")
    acciones_del_hostal_1()

#las preguntas a los dueños barian dependiendo el numero del hostal 
def preguntas_dueño_del_hostal_1():
  Menu_de_preguntas_hostal = input("1)Preguntar sobre mi hermano\n 2)Preguntar sobre mi padre\n 3)Preguntar por un buen camino\n 4)Dejar de preguntar\n Elije una opcion: ")

  if Menu_de_preguntas_hostal == "1":
    os.system("clear")
    Menu_de_preguntas_hostal_1.preguntas_sobre_mi_hermano()

  elif Menu_de_preguntas_hostal == "4":
    os.system("clear")
    acciones_del_hostal_1()

  else:
    os.system("clear")
    print("Elije una opcion valida")
    preguntas_dueño_del_hostal_1()


#Aqui se pondran los caminos a retomar al salir de los hostales hay una gran variedad de caminos a tomar
def retomando_camino_1():
  print("bien ya que descansaste un poco vamos a retomar el camino")