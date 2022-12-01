import sys
from sys import exit
import os
from os import system
import mult_penales
import tateti_juego2
import adivinarnumerojuego
import juego_azar
opcion = 0

while opcion!=5:    #cuerpo principal
    if opcion!=5:
        system('cls')
        print("\n ---------- \n BIENVENIDO AL MENU ")
        print("Elige una opcion: (Solo ingrese numeros) ")
        print('''
        [1] - Juego Divisores por penales (Ariel)
        [2] - Juego Tateti (Tomas)
        [3] - Juego Adivina un numero (Santy) 
        [4] - Juego 4
        [5] - Salir del programa''')

        opcion = input(".")

        if opcion ==1:
            mult_penales.multiplospenales()
        elif opcion==2:
            tateti_juego2.tateti()
        elif opcion==3:
            adivinarnumerojuego.adivinarnro()
        elif opcion==4:
            juego_azar.minijuegos_azar()
        elif opcion==5:
            sys.exit