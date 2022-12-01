#JUEGO ADIVINANDONRO CONSISTE EN ADIVINAR EL NUMERO A BASE DE PISTAS
from random import randint
def adivinandonro(puntos):
    int_restantes = 0
    nro_estimado = 0
    nro_clave = randint(50,800)
    pista1 = nro_clave-randint(10,30)
    pista2 = nro_clave+randint(11,40)
    puntos = 0


    print("\n BIENVENIDO TE TOCO EL JUEGO DE ADIVINANDO NUMERO: \n TE DARE PISTAS Y TIENES 4 INTENTOS PARA ADIVINAR EL NUMERO \n")

    print("EL NUMERO ES MAYOR QUE: ",pista1,"\n EL NUMERO ES MENOR QUE: ",pista2)   #PISTAS 1 Y 2
    if nro_clave%2==0:  #ULTIMA PISTA
        print("\n Y EL NUMERO ES PAR")
    else:
        print("\n Y EL NUMERO NO ES PAR")

    while int_restantes < 4:    #INICIO CICLO DE INTENTOS
        nro_estimado = int(input("\n ¿QUE NUMERO ES? \n"))
        int_restantes +=1

        if nro_estimado!=nro_clave:
            print("\n Incorrecto \n")
        else:
            print("\n CORRECTO!! \n")
            break
    
    if nro_estimado!=nro_clave: #NRO INCORRECTO
        print("\n Lo siento no has podido adivinar :( \n EL NUMERO ERA: ",nro_clave)
        puntos=0            # 0 PUNTOS GANADOS
    if int_restantes==4:    #PUNTOS SEGUN INTENTOS:
        puntos=1
    elif int_restantes==3:
        puntos=2
    elif int_restantes==2:
        puntos=3
    elif int_restantes==1:
        puntos=4
    return puntos




