def impuesto(salario):
	if salario > 0:
		if salario < 10000:
			print('Menos de 10 mil.....5%')
			salario = salario * .95
		elif salario < 15000:
			print('Entre 10 mil y 15 mil.....10%')
			salario = salario * .9
		elif salario < 20000:
			print('Entre 15 mil y 20 mil.....15%')
			salario = salario * .85
		else:
			print('Mas de 20 mil.....18%')
			salario = salario * .88
	else:
		return False

	print('Salario: {s}'.format(s = salario))
	return True


sal = float(input('Ingresa el salario: '))
if impuesto(sal):
	print('Salario calculado con exito!')
else:
	print('El salario es erroneo')
