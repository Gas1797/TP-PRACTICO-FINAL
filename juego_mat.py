#Juego matematico consiste en generar numeros random para devolver una suma y multiplicacion de numeros variados
from random import randint

def suma_mat(puntos):
    suma1 = randint(90,999)
    suma2 = randint(89,999)
    multi1 = randint(2,5)
    cuenta = suma1+suma2*multi1
    resultado = int()
    puntos = 0

    print("\n Bienvenido AL JUEGO MATEMATICO \n Realiza el siguiente calculo SIN CALCULADORA\n")
    print(suma1," + ",suma2, " * " ,multi1)
    resultado = int(input("\n")) #INGRESO

    if resultado==cuenta:           #NUMERO CORRECTO
        print("\n CORRECTO SUMA 3 PUNTOS")
        puntos = 3
    #else:
    #    if (resultado > cuenta-10) or (resultado < cuenta+10):  #NUMERO APROX GANA 1 PUNTO
    #        print("\n SUMA 1 PUNTO")
    #        puntos = 1
    #    else:
    #        print("\n INCORRECTO \n")
    #        puntos = 0
    return puntos