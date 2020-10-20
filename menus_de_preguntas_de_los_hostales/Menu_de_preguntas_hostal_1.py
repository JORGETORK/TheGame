#historia del juego

import os
import datetime 
import subprocess 
import sys 
import time
from io import open
from caminos_de_la_historia import camino_numero_1

def preguntas_sobre_mi_hermano():
	archivo = open("nombres_del_juego.txt","r")

	texto = archivo.readlines()

	archivo.close()

	Ahora = datetime.datetime.now()
	print(Ahora)
	print("Disculpe JA Silva le podria hacer unas prguntas sobre mi hermano si es que lo conose claro.\n")
	time.sleep(2)
	print("Claro " + texto[1].rstrip("\n") + " quien no conoseria a los famosos hijos de " + texto[4].rstrip("\n") + " por supuesto que conosco a " + texto[5].rstrip("\n") + " que quieres preguntarme hacerca de tu hermano")
	time.sleep(3)
	os.system("clear")
	preguntas_sobre_mi_hermano_1()


def preguntas_sobre_mi_hermano_1():
	Ahora = datetime.datetime.now()
	preguntas = int(input("1)Has visto a mi hermano por aqui?\n 2)Sabes algo serca de donde estubo la ultima ves?\n 3)Has escuchado algo sobre el?\n Elije una pregunta: "))


	if preguntas == 1 :
		print(Ahora)
		print("Que si e visto a tu hermano?\n")
		time.sleep(.5)
		print("la verdad no recuerdo averlo visto por estos rumbos hace mucho.")
		time.sleep(3)
		os.system("clear")

		salir = int(input("Quieres hacer otra pregunta sobre tu hermano?\n 1)si\n 2)no\n Elije una opcion: "))

		if salir == 1 :
			os.system("clear")
			preguntas_sobre_mi_hermano_1()

		elif salir == 2 :
			os.system("clear")
			camino_numero_1.preguntas_dueño_del_hostal_1()


	elif preguntas == 2 :
		print(Ahora)
		print("Que si se donde estubo tu hermano?")
		time.sleep(.5)
		print("¿?")