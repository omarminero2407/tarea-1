continua = True
op = ''
a = 0
b = 0

def suma(a,b):
	return a + b

def resta(a,b):
	return a - b

def multi(a,b):
	return a * b

def div(a,b):
	return a / b


def decide(op, a ,b):
	if op == 'a':
		res = suma(a,b)
	elif op == 'b':
		res = resta(a,b)
	elif op == 'c':
		res = multi(a,b)
	elif op == 'd':
		res = div(a,b)
	else:
		print('Adios...')
		return False

	print('El resultado es: {resultado}'.format(resultado = res))
	return True


while continua:
	op = ''
	print("""			a. suma\n
			b. resta\n
			c. multiplicacion\n
			d. division\n
			Introduzca una opción:""")
	op = str(input(op))
	if op == 'a' or op == 'b' or op == 'c' or op =='d':
		a = float(input('Introduce el primer numero: '))
		b = float(input('Introduce el segundo numero: '))
		if op == 'd':
			while b == 0: 
				b = int(input('El segundo numero debe ser diferente de 0: '))
	continua = decide(op, a, b)
