import sys
from sys import exit
import os
from os import system
import mult_penales
import tateti_juego2
import adivinarnumerojuego
import juego_azar
opcion = 0

def inicio():
    system('cls')
    print('*' * 5 + " Bienvenido a la presentación del TPI de laboratorio " + '*' * 5)
    print('\n')


    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print('''
        [1] - Juego Divisores por penales (Ariel)
        [2] - Juego Tateti (Tomas)
        [3] - Juego Adivina un numero (Santy) 
        [4] - Juegos de azar por puntos (Gabriel)
        [5] - Salir del programa''')
        eleccion_menu = input()

    return int(eleccion_menu)

juego=inicio()
if juego == 1:
    mult_penales.multiplospenales()
elif juego == 2:
    tateti_juego2.tateti()
elif juego == 3:
    adivinarnumerojuego.adivinarnro()
elif juego == 4:
    juego_azar.minijuegos_azar()
elif juego == 5:
    sys.exit
