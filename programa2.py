texto = input('Intruduce una cadena de texto: ')

repeticion = input('Intruduce el numero de veces que quieres que se repita el texto: ')

texto = str(texto)
repeticion = int(repeticion)


for i in range(repeticion):
	print(texto)
