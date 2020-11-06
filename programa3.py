def calculahoras(horas, costo = 150):
  pago = horas*costo
  print('Pago por día: {pago}'.format(pago = pago))
  pago = pago * 5
  print('Pago por semana: {pago}'.format(pago = pago))
  pago = pago * 4
  print('Pago por mes: {pago}'.format(pago = pago))
  
  
horas = int(input('Ingresa el numero de horas: '))

costo = int(input('Ingresa el costo por hora: '))
  
calculahoras(horas, costo)