salario = float(input('Entre com salário: \n'))
valorBonus = float(input('Entre com a porcetagem do aumento: \n'))
salarioNovo = (salario * (valorBonus / 100)) + salario


print(f'O valor do seu aumento foi de {valorBonus}% e seu novo salário é de {salarioNovo}')
