# juego creado por JORGETORK

import os 
import datetime 
import subprocess 
import sys 
import time
import requests
from io import open

Ahora = datetime.datetime.now()

#esta es la primera toma de decicion en el juego 
def camino_1_retorno():
    print("muy bien " + Nombre_del_jugador + " has elejido ir por la izquierda")
    camino_1 = int(input("Tu historia comensó hace ya 3 dias has caminado mucho y descansado muy poco pero te encontraste un hostal\n ¿quieres entrar?\n 1=si 2=no: "))
    os.system ("clear")

    if camino_1 == 1 :
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
      print("Bien ya estas dentro del hostal ¿que quieres hacer?\n")
      acciones_del_hostal_1()
      

    elif camino_1 == 2 :
      print("que mal quien sabe cuando encontraras otro buen lugar para descansar")

#esta es la accion basica para los hostales dentro del juego
def acciones_del_hostal_1():
  Menu_de_opciones_del_hotal = int(input("Menu de opciones:\n 1)Dormir\n 2)Comer\n 3)Hacer una pregunta al dueño\n 4)salir\n Elije una opcion: "))
  os.system ("clear")

  if Menu_de_opciones_del_hotal == 1:
      print("muy bien " + Nombre_del_jugador + " que suerte te toco una cama muy comoda a dormir un poco")
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
      print("Bien " + Nombre_del_jugador + " vamos a sentarnos a comer")
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
      preguntas_dueño_del_hostal1()

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
  Menu_de_preguntas_hostal_1 = int(input("1)Preguntar sobre mi hermano\n 2)Preguntar sobre mi padre\n 3)Preguntar por un buen camino\n Elije una opcion: "))

#Aqui se pondran los caminos a retomar al salir de los hostales hay una gran variedad de caminos a tomar
def retomando_camino_1():
  print("bien ya que descansaste un poco vamoa a retomar el camino")

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
Archivo.write("Fecha: % s" %Ahora + "\n")
Archivo.write("Nombre del jugador: " + Nombre_del_jugador + "\n")
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

print("Introduccion")

print("Vamos a empesar " + Nombre_del_jugador + " Esta es tu historia, todas las deciciones las tomas tú.")

Nomre_del_pueblo = input("Ahora a personalisar tu historia primero dime de donde vienes para en futuras referencias saber de donde eres.\n ingresa el nombre de tu pueblo: ")
Archivo.write("Nombre del pueblo: " + Nomre_del_pueblo + "\n")
os.system ("clear")

Nombre_del_malo = input("Bien ahora que sabemos que tu historia comensara en " + Nomre_del_pueblo + " tenemos que saber tambien el nombre del villano de la historia\n porque toda buena historia tiene un villano.\n ingresa el nombre del villano: ")
Archivo.write("Nombre del malo: " + Nombre_del_malo + "\n")
os.system ("clear")

Nombre_del_padre = input("Ya casi esta solo fatan tu padre tu hermano y la doncella para comensar la historia.\n por favor ingresa el nombre de tu padre: ")
Archivo.write("Nombre del padre: " + Nombre_del_padre + "\n")
os.system ("clear")

Nombre_del_hermano = input("Ahora ingresa el nombre de tu hermano: ")
Archivo.write("Nombre del hermano: " + Nombre_del_hermano + "\n")
os.system ("clear")

Nombre_de_la_doncella = input("Ahora ingresa el nombre de la doncella: ")
Archivo.write("Nombre de la doncella: " + Nombre_de_la_doncella + "\n\n")
os.system ("clear")

Archivo.close()

input("Listo es hora de comenzar tu historia espero la disfrutes " + Nombre_del_jugador + " presiona enter cuando estes listo")
os.system ("clear")

print(Ahora)
print("")
primer_movimiento = int(input("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + Nomre_del_pueblo + " para ir en busca de tu hermano " + Nombre_del_hermano + " que fue secuestrado por " + Nombre_del_malo + ".\n Te han revelado que " + Nombre_del_malo +" y " + Nombre_del_padre + " tenian una fuerte rivalidad porque alguna ves fueron aprendices del guerrero mas grande de toda la historia pero tu padre demostro ser mucho mas poderoso y tener mas corazon.\n Sin embargo tu padre fallecio hace ya 10 años por su gran corazon al proteger a este mundo de las mas grandes amenasas,\n amenasas que ahora estan a punto de ser liveradas por eso necesitas rescatar a tu hermano para juntar su fragemnto del mapa con el tuyo,\n vien ya que tienes todo listo y has salido del pueblo te encontraste dos caminos uno por la 1)izquierda y otro por la 2)derecha\n\n ¿por cual camino quiere ir 1 o 2?: "))
os.system ("clear")

if primer_movimiento == 1 :
  camino_1_retorno()

elif primer_movimiento == 2 :
  print("muy bien " + Nombre_del_jugador + " has elejido ir por la derecha")
  camino_2 = int(input("Tu historia comensó hace ya 3 dias te estas quedando sin proviciones y no has descansado en un buen lugar, ¿quieres seguir por este camino?\n 1)quiero regresar y tomar el camino 1\n 2)seguire por aqui\n elije una opcion: "))

  if camino_2 == 1 :
    print("Muy bien " + Nombre_del_jugador + " regresemos al camino de la izquierda")
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

    camino_1_retorno()
    
  elif camino_2 == 2 :
    print("Deacuerdo seguiremos por este camino espero te queden fuersas porque a lo lejos se ve un pequeño pueblo")
