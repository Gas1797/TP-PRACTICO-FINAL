import juego_gs
choice = 1
while choice!=0:
    if choice!=0:
        print("INICIO PRUEBA: \n")
        choice= input("HOLA \n")
        if choice==1:
            juego_gs.juego_azar_puntos()
        if choice==0:
            print("USTED HA SALIDO")
