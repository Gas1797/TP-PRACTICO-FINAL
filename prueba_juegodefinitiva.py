import os
from os import system
from random import randint
import piedra_papel
from piedra_papel import piedra_papel_tijera
import juego_mat
from juego_mat import suma_mat
import adivinando
from adivinando import adivinandonro

nro_generado = 0
puntos = 0
cont_turnos = 0
puntos_j1 = 0
puntos_j2 = 0

print("\n Bienvenido al Juego de azar de 2 jugadores \n En este juego el que llegue a 10 puntos gana \n")

while puntos_j1<10 and puntos_j2<10:       #INICIO CICLO
    if puntos_j1<10 and puntos_j2<10:
        cont_turnos +=1

        if cont_turnos%2 != 0:                          #TURNO JUGADOR 1
            print("\n ------------- \n TURNO JUGADOR 1: \n")

            nro_generado = randint(0,8)                 #GENERAMOS NUMERO ALEATORIO
            
            if nro_generado==0 or nro_generado==1 or nro_generado==2:
            #    piedra_papel.piedra_papel_tijera()
                puntos_j1 = puntos_j1 + piedra_papel_tijera(puntos)
            elif nro_generado==3 or nro_generado==4 or nro_generado==5:
                puntos_j1 = puntos_j1 + suma_mat(puntos)

            elif nro_generado==6 or nro_generado==7 or nro_generado==8:
            #    adivinando.adivinandonro()
                puntos_j1 = puntos_j1 + adivinandonro(puntos)
            print("\n Puntos actuales: ",puntos_j1)

            
        
        if cont_turnos%2 == 0:                        #TURNO JUGADOR 2
            print("\n --------- \n TURNO JUGADOR 2 \n")

            nro_generado = randint(0,8)                 #GENERAMOS NUMERO ALEATORIO

            if nro_generado==0 or nro_generado==1 or nro_generado==2:
            #    piedra_papel.piedra_papel_tijera()
                puntos_j2 = puntos_j2 + piedra_papel_tijera(puntos)

            elif nro_generado==3 or nro_generado==4 or nro_generado==5:
                #juego_mat.suma_mat(puntos)
                puntos_j2 = puntos_j2 + suma_mat(puntos)

            elif nro_generado==6 or nro_generado==7 or nro_generado==8:
            #    adivinando.adivinandonro()
                puntos_j2 = puntos_j2 + adivinandonro(puntos)
            print("\n Puntos actuales: ",puntos_j2)

if puntos_j1 >=10:
    print("FELICITACIONES JUGADOR 1 HAS GANADO \n")
if puntos_j2 >=10:
    print("FELICITACIONES JUGADOR 2 HAS GANADO! \n")