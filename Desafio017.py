import math
print(f"{'*'*10}Desafio 017 - Calcular Hipotenusa{'*'*10}")
cat_a = int(input("Informe o valor do cateto adjacente: "))
cat_b = int(input("Informe o valor do cateto oposto: "))

print(f"O valor da hipotesuna desse triangulo é: {int(math.hypot(cat_a, cat_b))}")
