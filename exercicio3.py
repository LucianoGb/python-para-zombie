#Conversos para segundos#

dias = int(input('Entre com a quantidade de dias:\n'))
horas = int(input('Entre com a quantidade de horas:\n'))
segundos = int(input('Entre com a quantidade de segundos\n'))

qnthora = (dias * 24) + horas
qntSegundos = (qnthora * 3600) + segundos

print(f'A quantidade de total de segundos é {qntSegundos}')
