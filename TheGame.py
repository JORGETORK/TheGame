# juego creado por JORGETORK

import os
import datetime 
import subprocess 
import sys 
import time
from time import sleep
from io import open
from colorama import Cursor, init, Fore, Back, Style
from partes_de_la_historia import historia_del_juego_parte_1
from acciones_de_hostales import hostal_1

Ahora = datetime.datetime.now()

def main():
  Ahora = datetime.datetime.now()
  print(""" 
  ▄▄▄█████▓ ██░ ██ ▓█████   ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
  ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀  ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
  ▒ ▓██░ ▒░▒██▀▀██░▒███   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
  ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
    ▒██▒ ░ ░▓█▒░██▓░▒████▒░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
    ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
      ░     ▒ ░▒░ ░ ░ ░  ░  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
    ░       ░  ░░ ░   ░   ░ ░   ░   ░   ▒   ░      ░      ░   
            ░  ░  ░   ░  ░      ░       ░  ░       ░      ░  ░
                                           juego creado por JORGETORK          

  """)
  print(Ahora)

  Archivo = open(".nombres_del_juego.txt","w")
  print("Bienvenido\n")

  Nombre_del_jugador = input("ingresa tu nombre por favor: ")
  Archivo.write("% s" %Ahora + "\n")
  Archivo.write(Nombre_del_jugador + "\n")
  os.system ("clear")

  print(""" 

  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  MMMMMMMMMMMMMMMMMTHEGAMEMMMMMMMMMMMMMMMM
  MMMMMMMMMMMMMMWXOxooooxOXWMMMMMMMMMMMMMM
  MMMMMMMMMMMMNOc'..    ..'cOWMMMMMMMMMMMM
  MMMMMMMMMMMXl............ .lXMMMMMMMMMMM
  MMMMMMMMMMNo................oNMMMMMMMMMM
  MMMMMMMMMM0, .............. ,0MMMMMMMMMM
  MMMMMMMMMM0, .............. ,0MMMMMMMMMM
  MMMMMMMMMMX: .............. :XMMMMMMMMMM
  MMMMMMMMMMWx................xWMMMMMMMMMM
  MMMMMMMMMMMNl..............lNMMMMMMMMMMM
  MMMMMMMMMMMMNd.......... .dNMMMMMMMMMMMM
  MWWMMMMMMNX0KN0o,......,l0NK0XNMMMMMMWWM
  MMMMMWXxl;'.'dXWNKOOOOKNWXd'.';lxXWMMMMM
  MMMMXd,. .....':lodxxdol:'..... .,dXMMMM
  MMM0:..............................:0MMM
  MMXl''''''''''''''''''''''''''''''''lXMM
  MMWXKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXWMM
  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

  """)

  print("Vamos a empesar " + Nombre_del_jugador + " Esta es tu historia, todas las deciciones las tomas tú.")

  Nomre_del_pueblo = input("Ahora a personalisar tu historia primero dime de donde vienes para en futuras referencias saber de donde eres.\n ingresa el nombre de tu pueblo: ")
  Archivo.write(Nomre_del_pueblo + "\n")
  os.system ("clear")

  Nombre_del_malo = input("Bien ahora que sabemos que tu historia comensara en " + Nomre_del_pueblo + " tenemos que saber tambien el nombre del villano de la historia.\n Porque toda buena historia tiene un villano.\n ingresa el nombre del villano: ")
  Archivo.write(Nombre_del_malo + "\n")
  os.system ("clear")

  Nombre_del_padre = input("Ya casi esta solo fatan tu padre tu hermano y la doncella para comensar la historia.\n por favor ingresa el nombre de tu padre: ")
  Archivo.write(Nombre_del_padre + "\n")
  os.system ("clear")

  Nombre_del_hermano = input("Ahora ingresa el nombre de tu hermano: ")
  Archivo.write(Nombre_del_hermano + "\n")
  os.system ("clear")

  Nombre_de_la_doncella = input("Ahora ingresa el nombre de la doncella: ")
  Archivo.write(Nombre_de_la_doncella + "\n")
  os.system ("clear")

  Archivo.close()

  input("Listo es hora de comenzar tu historia espero la disfrutes " + Nombre_del_jugador + " presiona enter cuando estes listo")
  os.system ("clear")

  Archivo_1 = open(".stats.txt","w")
  Archivo_1.write("1000" + "\n")
  Archivo_1.write("100" + "\n")
  Archivo_1.write("100" + "\n")
  Archivo_1.close()
  historia_del_juego_parte_1.inicio_del_juego()

def partida_guardada():
  Ahora = datetime.datetime.now()

  archivo = open(".nombres_del_juego.txt","r")

  texto = archivo.readlines()

  archivo.close()

  verificar = bool(texto)

  if verificar == True:
    print("Se encontro una partida con el nombre: " + texto[1].rstrip("\n") + "\n")
    print("Fecha de creacion: " + texto[0].rstrip("\n") + "\n")
    contraseña = input("Ingrese la contraseña correspondiente: ")

    if contraseña == "posada de ja silva":
      os.system("clear")
      init()
      print(Ahora)
      print("CARGANDO... ")
      for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
        sleep(.5)
        print(Cursor.UP(1)+Cursor.FORWARD(11)+str(arch))
      os.system("clear")
      hostal_1.acciones_del_hostal_1()

    else:
      os.system ("clear")
      print("Ingrese una contraseña valida")
      partida_guardada()



  elif verificar == False:
    print("no se encontro ninguna partida\n")
    time.sleep(2)
    os.system("clear")
    init()
    print(Ahora)
    print("CREANDO NUEVA PARTIDA... ")
    for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
      sleep(1)
      print(Cursor.UP(1)+Cursor.FORWARD(24)+str(arch))
    os.system("clear")
    main()

def abc():
  Ahora = datetime.datetime.now()
  print(""" 
    ▄▄▄█████▓ ██░ ██ ▓█████   ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀  ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
    ▒ ▓██░ ▒░▒██▀▀██░▒███   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
    ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
      ▒██▒ ░ ░▓█▒░██▓░▒████▒░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
      ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
        ░     ▒ ░▒░ ░ ░ ░  ░  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
      ░       ░  ░░ ░   ░   ░ ░   ░   ░   ▒   ░      ░      ░   
              ░  ░  ░   ░  ░      ░       ░  ░       ░      ░  ░
                                             juego creado por JORGETORK          

    """)
  Inicio = input("Bienvenido, ¿quieres crear una nueva partida o cargar una ya guardada?\n 1)Crear nueva partida\n 2)Cargar partida\n Elije una opcion: ")

  if Inicio == "1":
    os.system("clear")
    init()
    print(Ahora)
    print("CREANDO PARTIDA ESPERE... ")
    for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
      sleep(1.5)
      print(Cursor.UP(1)+Cursor.FORWARD(25  )+Fore.YELLOW+str(arch)+Fore.RESET)
    os.system("clear")

    main()

  elif Inicio == "2":
    os.system("clear")
    init()
    print(Ahora)
    print("LEYENDO DATOS ESPERE... ")
    for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
      sleep(1.5)
      print(Cursor.UP(1)+Cursor.FORWARD(23)+Fore.YELLOW+str(arch)+Fore.RESET)
    os.system("clear")

    partida_guardada()

  else:
    os.system ("clear")
    print("Elije una opcion valida")
    abc()

#aqui empiesa el codigo del juego que se muestra en pantalla
init()
print("[VERSION]: 1.0\n\n")
time.sleep(0.5)
print(Fore.WHITE+Back.BLUE+"[juego creado por JORGETORK]\n\n"+Back.RESET)
time.sleep(0.5)
print("Bienvenido a TheGame.(por favor pon tu terminal en pantalla completa Gracias)\n\n")
time.sleep(3)
os.system('clear')

init()
print(Ahora)
print("CARGANDO... ")
for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
    sleep(1.5)
    print(Cursor.UP(1)+Cursor.FORWARD(11)+Fore.YELLOW+str(arch)+Fore.RESET)
os.system("clear")

init()
print(Ahora)
print("INICIANDO JUEGO... ")
for arch in ["[                    ] 0%", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]:
    sleep(0.5)
    print(Cursor.UP(1)+Cursor.FORWARD(18)+Fore.YELLOW+str(arch)+Fore.RESET)
os.system("clear")

abc()