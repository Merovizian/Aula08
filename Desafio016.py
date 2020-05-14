import math
print (f"{'*'*10}Desafio 016 - Mostra a porção inteira de qualquer numero{'*'*10}")
num = float(input("Digite qualquer número: "))
print (f'O numero {num} tem como inteiro o valor: {int(num//1)}')
print (f'O numero {num} tem como inteiro o valor: {math.floor(num)}')
print (f'O numero {num} tem como inteiro o valor: {int(num)}')