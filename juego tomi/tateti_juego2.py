from random import randint
def tateti():
    x = int()
    n = int()
    jugador = int()
    vector = str()
    vector = [str() for ind0 in range(9)]
    for x in range(1,10):
    	vector[x-1] = " "
	x = 1
	jugador = randint(0,1)+1
	while x<=9:
		print("Ingresa una posicion jugador: ",jugador)
		print("1,2,3","    ",vector[0],"|",vector[1],"|",vector[2])
		print("4,5,6","    ",vector[3],"|",vector[4],"|",vector[5])
		print("7,8,9","    ",vector[6],"|",vector[7],"|",vector[8])
		n = int(input())
		if n>0 and n<10:
			if jugador==1:
				if vector[n-1]==" ":
					vector[n-1] = "X"
					jugador = 2
					if vector[0]=="X" and vector[1]=="X" and vector[2]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
					if vector[3]=="X" and vector[4]=="X" and vector[5]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
					if vector[6]=="X" and vector[7]=="X" and vector[8]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
					if vector[0]=="X" and vector[3]=="X" and vector[6]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
					if vector[1]=="X" and vector[4]=="X" and vector[7]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
					if vector[2]=="X" and vector[5]=="X" and vector[8]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
					if vector[2]=="X" and vector[4]=="X" and vector[4]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
					if vector[0]=="X" and vector[4]=="X" and vector[8]=="X":
						print("EL jugador 1 ha ganado")
						x = 9
				else:
					print("Esa posicion esta ocupada")
			else:
				if vector[n-1]==" ":
					vector[n-1] = "O"
					jugador = 1
					if vector[0]=="O" and vector[1]=="O" and vector[2]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
					if vector[3]=="O" and vector[4]=="O" and vector[5]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
					if vector[6]=="O" and vector[7]=="O" and vector[8]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
					if vector[0]=="O" and vector[3]=="O" and vector[6]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
					if vector[1]=="O" and vector[4]=="O" and vector[7]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
					if vector[2]=="O" and vector[5]=="O" and vector[8]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
					if vector[2]=="O" and vector[4]=="O" and vector[6]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
					if vector[0]=="O" and vector[4]=="O" and vector[8]=="O":
						print("EL jugador 2 ha ganado")
						x = 9
				else:
					print("Esa posicion esta ocupada")
		else:
			print("posicion incorrecta")
		x = x+1
	print("1,2,3","    ",vector[0],"|",vector[1],"|",vector[2])
	print("4,5,6","    ",vector[3],"|",vector[4],"|",vector[5])
	print("7,8,9","    ",vector[6],"|",vector[7],"|",vector[8])
    return