#piedra papel tijera vs PC 1 PARA PIEDRA 2 PARA PAPEL 3 PARA TIJERA
from random import randint
def piedra_papel_tijera(puntos):
    oponente = 0
    eleccion = 0
    puntos = 0
    while oponente==eleccion:
        
        oponente = randint(1,3)
        eleccion = int(input("\n HAZ TU ELECCION (USA SOLO NUMEROS): \n 1 - PARA PIEDRA \n 2 - PARA PAPEL \n 3 - PARA TIJERA"))
        if eleccion==1 and oponente==3:
            print("\n TIJERA! \n ¡GANASTE!")
            puntos=2
        elif eleccion==1 and oponente==2:
            print("\n PAPEL! \n PERDISTE!")
            puntos=0

        if eleccion==2 and oponente==1:
            print("\n PIEDRA! \n GANASTE!")
            puntos=2
        elif eleccion==2 and oponente==3:
            print("\n TIJERA! \n ¡PERDISTE!")
            puntos=0
        
        if eleccion==3 and oponente==1:
            print("\n PIEDRA! \n PERDISTE!")
            puntos=0
        elif eleccion==3 and oponente==2:
            print("\n PAPEL! \n GANASTE!")
            puntos=2
        
        if eleccion==oponente:#EN CASO DE IGUALDAD
            if oponente==1:
                print("\n PIEDRA! \n EMPATE!!")
            elif oponente==2:
                print("\n PAPEL! \n EMPATE!!")
            elif oponente==3:
                print("\n TIJERA! \n EMPATE!!")
    return puntos

        

            


    
