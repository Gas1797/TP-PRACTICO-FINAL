import sys
from sys import exit
import os
from os import system
opcion = 0

while opcion!=5:    #cuerpo principal
    if opcion!=5:
        system('cls')
        print("\n ---------- \n BIENVENIDO AL MENU ")
        print("Elige una opcion: (Solo ingrese numeros) ")
        print('''
        [1] - Juego 1
        [2] - Juego 2
        [3] - Juego 3
        [4] - Juego 4
        [5] - Salir del programa''')

        if opcion ==1:
            juego.funcionjuego1()
        elif opcion==2:
            juego.funcionjuego2()
        elif opcion==3:
            juego.funcionjuego3()
        elif opcion==4:
            juego.funcionjuego4()
        elif opcion==5:
            exit