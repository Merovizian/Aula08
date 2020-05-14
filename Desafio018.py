import math
print(f"{'*'*10}Desafio 018 - Seno, Cosseno e Tangente{'*'*10}")
angulo = float(input("Digite o valor do angulo: "))
angulo = angulo * 0.0174533
print(f"O valor do seno do angulo {angulo}º é:  {float(math.sin(angulo)):.3f}")
print(f"O valor do cosseno do angulo {angulo}º é:  {float(math.cos(angulo)):.3f}")
print(f"O valor da tangente do angulo {angulo}º é:  {float(math.tan(angulo)):.3f}")