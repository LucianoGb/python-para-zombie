mercadoria = float(input('Entre com o valor da mercadoria\n'))
desconto = float(input('Entre com o valor do desconto\n')) / 100

valorMercadoriaComDesconto = mercadoria - (desconto * mercadoria)

print(f'O valor do desconto é {desconto * 100} e o valor novo da mercadoria é {valorMercadoriaComDesconto}')