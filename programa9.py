def factorial(num):
	res = num
	for i in range(num, 1, -1):
		res = res * (i-1)
	return res


numero = int(input('Introduce un numero: '))

while numero <= 0:
	numero = int(input('El numero debe de ser positivo: '))

resultado = factorial(numero)

print('El factorial de {n} es: {r}'.format(n = numero, r = resultado))