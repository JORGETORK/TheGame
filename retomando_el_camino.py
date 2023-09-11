import os
import datetime 
import subprocess 
import sys 
import time
from time import sleep
from io import open
from colorama import Cursor, init, Fore, Back, Style
from menus_de_preguntas_de_los_hostales import Menu_de_preguntas_hostal_1

def retomando_el_camino():
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