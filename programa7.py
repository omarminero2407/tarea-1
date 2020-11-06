def costo(edad, ocupacion):
	precio = 0
	if edad < 4:
		precio = 0
	elif edad < 16:
		precio = 50
	else:
		precio = 100

	if ocupacion == 'estudiante':
		precio = precio * .9
	elif ocupacion == 'docente':
		precio = precio * .7
	elif ocupacion == 'inapam':
		precio = precio * .5

	return precio

age = int(input('Introduce la edad: '))
job = str(input('Intruduce la ocupacion: '))

job = job.lower()

precio = costo(age, job)
print('El costo es de: {c}'.format(c = precio))

