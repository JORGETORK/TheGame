# juego creado por JORGETORK

import os, datetime, subprocess, sys

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
print("Bienvenido a TheGame.(por favor pon tu terminal en pantalla completa Gracias)")

Nombre_del_jugador = input("ingresa tu nombre por favor: ")
os.system ("clear")

print(""" 

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
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

Nomre_del_pueblo = input("Ahora a personalisar tu historia primero dime de donde vienes para en futuras referencias saber de donde eres, ingresa el nombre de tu pueblo: ")
os.system ("clear")

Nombre_del_malo = input("Bien ahora que sabemos que tu historia comensara en " + Nomre_del_pueblo + " tenemos que saber tambien el nombre del villano de la historia, ingresa el nombre del villano: ")
os.system ("clear")

Nombre_del_hermano = input("Ya casi esta solo fatan tu hermano y la doncella para comensar la historia,por favor ingresa el nombre de tu hermano: ")
os.system ("clear")

Nombre_de_la_doncella = input("Ahora ingresa el nombre de la doncella: ")
os.system ("clear")

input("Listo es hora de comenzar tu historia espero la disfrutes " + Nombre_del_jugador + " presiona enter cuando estes listo")
os.system ("clear")

print(Ahora)
primer_movimiento = int(input("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + Nomre_del_pueblo + " para ir en busca de tu hermano " + Nombre_del_hermano + " que fue secuestrado por " + Nombre_del_malo + "\n" + " ¿por cual camino quiere ir 1 o 2?: "))
os.system ("clear")

if primer_movimiento == 1 :
  print("muy bien " + Nombre_del_jugador + " has elejido ir por el camino 1")
  camino_1 = int(input("Tu historia comensó hace ya 3 dias has caminado mucho y te encontraste un hostal ¿quieres entrar? 1=si 2=no: "))
  if camino_1 == 1 :
        print("muy bien " + Nombre_del_jugador + " que suerte te toco una cama muy comoda")

  elif camino_1 == 2 :
        print("que mal quien sabe cuando encontraras otro buen lugar para descansar")

elif primer_movimiento == 2 :
  print("muy bien " + Nombre_del_jugador + " has elejido el camino 2")
  
  camino_2 = int(input("Tu historia comensó hace ya 3 dias te estas quedando sin proviciones y no has descansado en un buen lugar, ¿quieres seguir por este camino?\n 1)quiero regresar y tomar el camino 1\n 2)seguire por aqui\n elije una opcion: "))
  os.system ("clear")
  
  if camino_2 == 1 :
    print("Muy bien " + Nombre_del_jugador + " regresemos al camino 1")
    os.system ("clear")
    
  elif camino_2 == 2 :
    print("Deacuerdo seguiremos por este camino espero te queden fuersas porque a lo lejos se ve un pequeño pueblo")
