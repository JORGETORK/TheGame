# juego creado por JORGETORK

import os

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

print("Bienvenido a TheGame")

Nombre_del_jugador = input("ingresa tu nombre por favor: ")
os.system ("clear")

print("Vamos a empesar " + Nombre_del_jugador + " Esta es tu historia, todas las deciciones las tomas tú.")

Nomre_del_pueblo = input("Ahora a personalisar tu historia primero dime de donde vienes para en futuras referencias saber de que pueblo saliste a tu aventura, ingresa el nombre de tu pueblo: ")
os.system ("clear")

Nombre_del_malo = input("Bien ahora que sabemos que tu historia comensara en " + Nomre_del_pueblo + " tenemos que saber tambien el nombre del malo de la historia, ingresa el nombre del malo: ")
os.system ("clear")

Nombre_del_hermano = input("ya casi esta solo fatan tu hermano y a comensar la historia, por favor ingresa el nombre se tu hermano: ")
os.system ("clear")

input("Listo es hora de comenzar tu historia espero la disfrutes " + Nombre_del_jugador + " presiona enter cuando estes listo")
os.system ("clear")

primer_movimiento = int(input("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + Nomre_del_pueblo + " para ir en busca de tu hermano " + Nombre_del_hermano + " que fue secuestrado por " + Nombre_del_malo + " ¿por cual camino quiere ir 1 o 2?: "))
if primer_movimiento <= 1 :
    print("muy bien " + Nombre_del_jugador + " has elejido ir por el camino 1")
    camino_1 = int(input("Tu historia comensó hace ya 3 dias has caminado mucho y te encontraste un hostal ¿quieres entrar? 1=si 2=no: "))
    if camino_1 <= 1 :
        print("muy bien " + Nombre_del_jugador + " que suerte te toco una cama muy comoda")

    else:
        print("que mal quien sabe cuando encontraras otro buen lugar para descansar")

else:
    print("muy bien " + Nombre_del_jugador + " has elejido el camino 2")
    camino_2 = int(input("Tu historia comensó hace ya 3 dias te estas quedando sin proviciones y no has descansado en un buen lugar"))
