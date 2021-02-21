#historia del juego

import os
import datetime 
import subprocess 
import sys 
import time
from time import sleep
from io import open
from colorama import Cursor, init, Fore, Back, Style
from caminos_de_la_historia import camino_numero_1

def inicio_del_juego():
  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()
  
  archivo.close()

  archivo_1 = open(".stats.txt","r")

  texto_1 = archivo_1.readlines()

  archivo_1.close()

  Ahora = datetime.datetime.now()
  print(Ahora)
  print("Inicias con los siguientes stats, pero el tomar caminos largos te cansara y te dara hambre al igual que todo tiene un costo")
  print("Dinero: $" + texto_1[0].rstrip("\n") + " Energia: " + texto_1[1].rstrip("\n") + "%" +" comida: " + texto_1[2].rstrip("\n") + "%")
  input("Enter para seguir ")
  os.system("clear")
  print(Ahora)
  print("Dinero: $" + texto_1[0].rstrip("\n") + " Energia: " + texto_1[1].rstrip("\n") + "%" +" comida: " + texto_1[2].rstrip("\n") + "%")
  print("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + texto[2].rstrip("\n") + " para ir en busca de tu hermano " + texto[5].rstrip("\n") + " que fue secuestrado por " + texto[3].rstrip("\n") + ".")
  print("Te han revelado que " + texto[3].rstrip("\n") +" y tu padre " + texto[4].rstrip("\n") + " tenian una fuerte rivalidad porque alguna ves fueron aprendices del guerrero mas grande de toda la historia, pero tu padre demostro ser mucho mas poderoso y tener mas corazon.\n Sin embargo tu padre fallecio hace ya 10 años por su gran corazon al proteger a este mundo de las mas grandes amenasas,\n amenasas que ahora estan a punto de ser liveradas y por eso necesitas rescatar a tu hermano para juntar su fragemnto del mapa con el tuyo para averiguar como tu padre salvo al mundo.\n")
  input("Enter para seguir ")
  os.system("clear")
  inicio_del_juego_1()
  
def inicio_del_juego_1():
  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()
  
  archivo.close()

  archivo_1 = open(".stats.txt","r")

  texto_1 = archivo_1.readlines()

  archivo_1.close()

  Ahora = datetime.datetime.now()
  print(Ahora)
  print("Dinero: $" + texto_1[0].rstrip("\n") + " Energia: " + texto_1[1].rstrip("\n") + "%" +" comida: " + texto_1[2].rstrip("\n") + "%")
  primer_movimiento = input("Bien ya que tienes todo listo y has salido del pueblo te encontraste dos caminos uno por la izquierda y otro por la derecha\n 1)izquierda\n 2)derecha\n ¿por cual camino quieres?: ")
  os.system ("clear")

  if primer_movimiento == "1" :
    suma = int(texto_1[0].rstrip("\n"))-0
    suma_2 = int(texto_1[1].rstrip("\n"))-50
    suma_3 = int(texto_1[2].rstrip("\n"))-50

    archivo_2 = open(".stats.txt","w")
    archivo_2.write(str(suma) + "\n")
    archivo_2.write(str(suma_2) + "\n")
    archivo_2.write(str(suma_3) + "\n")
    archivo_2.close()
    os.system("clear")
    camino_numero_1.camino()

  elif primer_movimiento == "2" :
    suma = int(texto_1[0].rstrip("\n"))-0
    suma_2 = int(texto_1[1].rstrip("\n"))-50
    suma_3 = int(texto_1[2].rstrip("\n"))-50

    archivo_2 = open(".stats.txt","w")
    archivo_2.write(str(suma) + "\n")
    archivo_2.write(str(suma_2) + "\n")
    archivo_2.write(str(suma_3) + "\n")
    archivo_2.close()
    os.system("clear")
    camino_numero_1.camino()

  
  else:
    os.system("clear")
    print("Elije una opcion valida")
    inicio_del_juego_1()