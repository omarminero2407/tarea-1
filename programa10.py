def area(radio):
	return 3.1416 * radio

def volumen(radio, altura):
	A = area(radio)
	return A * altura


r = int(input("Introduce el radio: "))
a = int(input("Introduce la altura: "))

vol = volumen(r,a)

print('El volumen del cilindro es: {v} unidades cubicas'.format(v = vol))
