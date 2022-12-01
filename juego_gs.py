import os
from os import system
from random import randint
import piedra_papel
import juego_mat
import adivinando
def juego_azar_puntos():
    nro_generado = 0
    puntos = 0
    cont_turnos = 0
    matriz_puntos = [str() for ind0 in range(2)]
    print("\n Bienvenido al Juego de azar de 2 jugadores \n En este juego el que llegue a 10 puntos gana \n")

    while matriz_puntos[1]<10 and matriz_puntos[2]<10:       #INICIO CICLO
        if matriz_puntos[1]<10 and matriz_puntos[2]<10:
            cont_turnos +=1

            if cont_turnos%2 != 0:                          #TURNO JUGADOR 1
                print("\n ------------- \n TURNO JUGADOR 1: \n")

                nro_generado = randint(0,8)                 #GENERAMOS NUMERO ALEATORIO
            
                if nro_generado==0 or nro_generado==1 or nro_generado==2:
                    piedra_papel.piedra_papel_tijera()
                    matriz_puntos[1] = matriz_puntos[1] + puntos
                elif nro_generado==3 or nro_generado==4 or nro_generado==5:
                    juego_mat.suma_mat()
                    matriz_puntos[1] = matriz_puntos[1] + puntos
                elif nro_generado==6 or nro_generado==7 or nro_generado==8:
                    adivinando.adivinandonro()
                    matriz_puntos[1] = matriz_puntos[1] + puntos
        
            if cont_turnos%2 == 0:                        #TURNO JUGADOR 2
                print("\n --------- \n TURNO JUGADOR 2 \n")

                nro_generado = randint(0,8)                 #GENERAMOS NUMERO ALEATORIO

                if nro_generado==0 or nro_generado==1 or nro_generado==2:
                    piedra_papel.piedra_papel_tijera()
                    matriz_puntos[2] = matriz_puntos[2] + puntos
                elif nro_generado==3 or nro_generado==4 or nro_generado==5:
                    juego_mat.suma_mat()
                    matriz_puntos[2] = matriz_puntos[2] + puntos
                elif nro_generado==6 or nro_generado==7 or nro_generado==8:
                    adivinando.adivinandonro()
                    matriz_puntos[2] = matriz_puntos[2] + puntos
    if matriz_puntos[1] >=10:
        print("FELICITACIONES JUGADOR 1 HAS GANADO \n")
    if matriz_puntos[2] >=10:
        print("FELICITACIONES JUGADOR 2 HAS GANADO! \n")
    return




