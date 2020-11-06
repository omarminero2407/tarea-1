payaso = 1.5

juego_mesa = 1.7


def peso(p1, p2):
	total = p1*payaso + p2*juego_mesa 
	if total > 10:
		print('El pedido excede el peso perimitido de 10k por: {p}gr'.format(p=(total - 10)))
		return False
	else:
		return True

piezas_payaso = int(input('Numero de piezas payaso: '))
piezas_juego_mesa = int(input('NUmero de piezas juego de mesa: '))

if peso(piezas_payaso, piezas_juego_mesa):
	print('Pedido Exitoso!')
else:
	print('Pedido Rechazado!')
