#historia del juego

import os
import datetime 
import subprocess 
import sys 
import time
from time import sleep
from io import open
from colorama import Cursor, init, Fore, Back, Style
from acciones_de_hostales import hostal_1

def preguntas_sobre_mi_hermano():
	archivo = open(".nombres_del_juego.txt","r")

	texto = archivo.readlines()

	archivo.close()

	Ahora = datetime.datetime.now()
	print(Ahora)
	print("Disculpe JA Silva le podria hacer unas prguntas sobre mi hermano si es que lo conose claro.\n")
	time.sleep(2)
	print("Claro " + texto[1].rstrip("\n") + " quien no conoseria a los famosos hijos de " + texto[4].rstrip("\n") + " por supuesto que conosco a " + texto[5].rstrip("\n") + " que quieres preguntarme hacerca de tu hermano")
	time.sleep(10)
	os.system("clear")
	preguntas_sobre_mi_hermano_1()


def preguntas_sobre_mi_hermano_1():
	archivo = open(".nombres_del_juego.txt","r")

	texto = archivo.readlines()

	archivo.close()

	Ahora = datetime.datetime.now()
	preguntas = input("1)Has visto a mi hermano por aqui?\n 2)Sabes algo serca de donde estubo la ultima ves?\n 3)Has escuchado algo sobre el?\n 4)salir\n Elije una pregunta: ")

	if preguntas == "1" :
		os.system("clear")
		Has_visto_a_mi_hermano_por_aqui()

	elif preguntas == "2" :
		os.system("clear")
		Sabes_algo_serca_de_donde_estubo_la_ultima_ves()

	elif preguntas == "3" :
		os.system("clear")
		Has_escuchado_algo_sobre_el()

	elif preguntas == "4" :
		os.system("clear")
		hostal_1.preguntas_dueño_del_hostal_1()

	else:
		os.system("clear")
		print("Elije una opcion valida")
		preguntas_sobre_mi_hermano_1()




def Has_visto_a_mi_hermano_por_aqui():
	archivo = open(".nombres_del_juego.txt","r")

	texto = archivo.readlines()

	archivo.close()

	Ahora = datetime.datetime.now()

	os.system("clear")
	print(Ahora)
	print("JA Silva: ¿Que si e visto a tu hermano?\n")
	time.sleep(1)
	print("JA Silva: la verdad no recuerdo averlo visto por estos rumbos hace mucho.\n")
	time.sleep(5)

	salir = input("Quieres hacer otra pregunta sobre tu hermano?\n 1)si\n 2)no\n Elije una opcion: ")

	if salir == "1" :
		os.system("clear")
		preguntas_sobre_mi_hermano_1()

	elif salir == "2" :
		os.system("clear")
		hostal_1.preguntas_dueño_del_hostal_1()

	else:
		os.system("clear")
		print("Elije una opcion valida")
		Has_visto_a_mi_hermano_por_aqui()


def Sabes_algo_serca_de_donde_estubo_la_ultima_ves():
	archivo = open(".nombres_del_juego.txt","r")

	texto = archivo.readlines()

	archivo.close()

	Ahora = datetime.datetime.now()


	os.system("clear")
	print(Ahora)
	print("JA Silva: ¿Que si se donde estubo tu hermano?\n")
	time.sleep(1)
	print("JA Silva: La verdad no creo.\n")
	time.sleep(1)
	print(texto[1].rstrip("\n") + ": Claro disculpa por la pregunta tan tonta.\n")
	time.sleep(5)

	salir = input("Quieres hacer otra pregunta sobre tu hermano?\n 1)si\n 2)no\n Elije una opcion: ")

	if salir == "1" :
		os.system("clear")
		preguntas_sobre_mi_hermano_1()

	elif salir == "2" :
		os.system("clear")
		hostal_1.preguntas_dueño_del_hostal_1()

	else:
		os.system("clear")
		print("Elije una opcion valida")
		Sabes_algo_serca_de_donde_estubo_la_ultima_ves()


def Has_escuchado_algo_sobre_el():
	archivo = open(".nombres_del_juego.txt","r")

	texto = archivo.readlines()

	archivo.close()

	Ahora = datetime.datetime.now()


	os.system("clear")
	print(Ahora)
	print("JA Silva: ¿Que si e escuchado algo sobre tu hermano?")
	time.sleep(1)
	print("JA Silva: Ahoa que lo pienso creo a ver escuchado a unos caza recompensas que pasaban por aqui decir algo sobre " + texto[5].rstrip("\n") + ",\n no estoy seguro pero creo que dijeron que unos guardias imperiales de " + texto[3].rstrip("\n") + " en el pueblo vecino se jactaban de tener capturado a uno se los hijos de la leyenda, aunque no lo crei posible.")
	time.sleep(5)
	print(texto[1].rstrip("\n") + ": ya veo, muchisimas gracias por esta valiosa imformacion")

	salir = input("Quieres hacer otra pregunta sobre tu hermano?\n 1)si\n 2)no\n Elije una opcion: ")

	if salir == "1" :
		os.system("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		time.sleep(1.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[                    ] 0% ")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[=====               ] 25%")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[==========          ] 50%")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[===============     ] 75%")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[====================] 100%")
		time.sleep(.5)
		os.system ("clear")
		Archivo = open("Tu Historia De TheGame.txt","w")

		Archivo.write("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + texto[2].rstrip("\n") + " para ir en busca de tu hermano " + texto[5].rstrip("\n") + " que fue secuestrado por " + texto[3].rstrip("\n") + ".\n")
		Archivo.write("Te han revelado que " + texto[3].rstrip("\n") +" y tu padre " + texto[4].rstrip("\n") + " tenian una fuerte rivalidad porque alguna ves fueron aprendices del guerrero mas grande de toda la historia, pero tu padre demostro ser mucho mas poderoso y tener mas corazon.\n Sin embargo tu padre fallecio hace ya 10 años por su gran corazon al proteger a este mundo de las mas grandes amenasas,\n amenasas que ahora estan a punto de ser liveradas y por eso necesitas rescatar a tu hermano para juntar su fragemnto del mapa con el tuyo para averiguar como tu padre salvo al mundo.\n")
		Archivo.write("Saliste de tu pueblo y llegaste al hostal de JA Silva done te revelo aver escuchado que unos guardias imperiales de " + texto[3].rstrip("\n") + " se jactaban de tener capturado a uno se los hijos de la leyenda aunque no lo creia posible.")

		Archivo.close()
		os.system("clear")
		preguntas_sobre_mi_hermano_1()

	elif salir == "2" :
		os.system("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		time.sleep(1.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[                    ] 0% ")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[=====               ] 25%")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[==========          ] 50%")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[===============     ] 75%")
		time.sleep(.5)
		os.system ("clear")
		print("Agregando informacion valiosa a tu historia espera un momento por favor.")
		print(Ahora)
		print("[====================] 100%")
		time.sleep(.5)
		os.system ("clear")
		Archivo = open("Tu Historia De TheGame.txt","w")

		Archivo.write("Todo comenzó como un juego cuando eras pequeño pero hoy sé ha tornado realidad, tienes que dejar tu pueblo " + texto[2].rstrip("\n") + " para ir en busca de tu hermano " + texto[5].rstrip("\n") + " que fue secuestrado por " + texto[3].rstrip("\n") + ".\n")
		Archivo.write("Te han revelado que " + texto[3].rstrip("\n") +" y tu padre " + texto[4].rstrip("\n") + " tenian una fuerte rivalidad porque alguna ves fueron aprendices del guerrero mas grande de toda la historia, pero tu padre demostro ser mucho mas poderoso y tener mas corazon.\n Sin embargo tu padre fallecio hace ya 10 años por su gran corazon al proteger a este mundo de las mas grandes amenasas,\n amenasas que ahora estan a punto de ser liveradas y por eso necesitas rescatar a tu hermano para juntar su fragemnto del mapa con el tuyo para averiguar como tu padre salvo al mundo.\n")
		Archivo.write("Saliste de tu pueblo y llegaste al hostal de JA Silva done te revelo aver escuchado que unos guardias imperiales de " + texto[3].rstrip("\n") + " se jactaban de tener capturado a uno se los hijos de la leyenda aunque no lo creia posible.")

		Archivo.close()

		hostal_1.preguntas_dueño_del_hostal_1()

	else:
		os.system("clear")
		print("Elije una opcion valida")
		Has_escuchado_algo_sobre_el()