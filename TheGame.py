# juego creado por JORGETORK

import os
import datetime 
import subprocess 
import sys 
import time
from io import open
from partes_de_la_historia import historia_del_juego_parte_1

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

  Archivo = open("nombres_del_juego.txt","w")

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

  Nombre_del_malo = input("Bien ahora que sabemos que tu historia comensara en " + Nomre_del_pueblo + " tenemos que saber tambien el nombre del villano de la historia\n porque toda buena historia tiene un villano.\n ingresa el nombre del villano: ")
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
  historia_del_juego_parte_1.inicio_del_juego()


#aqui empiesa el codigo del juego que se muestra en pantalla
print("[VERSION]: 1.0\n\n")
time.sleep(0.5)
print("[juego creado por JORGETORK]\n\n")
time.sleep(0.5)
print("Bienvenido a TheGame.(por favor pon tu terminal en pantalla completa Gracias)\n\n")
time.sleep(3)
os.system('clear')

print("CARGANDO")
print(Ahora)
print("[                    ] 0% ")
time.sleep(3)
os.system ("clear")
print("CARGANDO")
print(Ahora)
print("[=====               ] 25%")
time.sleep(3)
os.system ("clear")
print("CARGANDO")
print(Ahora)
print("[==========          ] 50%")
time.sleep(3)
os.system ("clear")
print("CARGANDO")
print(Ahora)
print("[===============     ] 75%")
time.sleep(3)
os.system ("clear")
print("CARGANDO")
print(Ahora)
print("[====================] 100%")
time.sleep(3)
os.system ("clear")
print(Ahora)
print("COMPLETADO")
time.sleep(2)
os.system ("clear")
print("INICIANDO JUEGO")
print(Ahora)
print("[                    ] 0% ")
time.sleep(.5)
os.system ("clear")
print("INICIANDO JUEGO")
print(Ahora)
print("[=====               ] 25%")
time.sleep(.5)
os.system ("clear")
print("INICIANDO JUEGO")
print(Ahora)
print("[==========          ] 50%")
time.sleep(.5)
os.system ("clear")
print("INICIANDO JUEGO")
print(Ahora)
print("[===============     ] 75%")
time.sleep(.5)
os.system ("clear")
print("INICIANDO JUEGO")
print(Ahora)
print("[====================] 100%")
time.sleep(.5)
os.system ("clear")

main()