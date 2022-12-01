from random import randint
if __name__ == '__main__':
	#declaramos las variables
	num_ingresado = int()
	num_secreto = int()
	#
	while True:
		dos = 2
		intentos = 10
		num_secreto = randint(0,99)+1

		print("-----Bienvenido-----")
		print("Adivine el numero (de 1 a 100):")
		num_ingresado = int(input())
		while num_secreto!=num_ingresado and intentos>1:
			if num_secreto>num_ingresado:
				print("Muy bajo")
			else:                   #dependiendo el numero aparecera la opcion como pista si es mas alto o mas bajo
				print("Muy alto")
			intentos = intentos-1       #se ira restando 1 vida
			print("Le quedan ",intentos," intentos:")
			num_ingresado = int(input())

		if num_secreto==num_ingresado:
			print("Exacto! adivinaste! en ",11-intentos," intentos.")
		else:
			print("Fallaste!! El numero era: ",num_secreto)
		print("Presione 1 si desea volver a jugar?")
		print("Presione 2 si desea volver al menú", end="")

		op = int(input())
		if op==dos:break
	print("¡¡¡Gracias por jugar.!!!")
