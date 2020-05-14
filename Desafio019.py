import math,random
print(f"{'*'*10}Desafio 019 - Sorteio de aluno{'*'*10}")
nome_a = input("Informe o nome do primeiro aluno: ")
nome_b = input("Informe o nome do segundo aluno: ")
nome_c = input("Informe o nome do terceiro aluno: ")
nome_d = input("Informe o nome do quarto aluno: ")
escolhido = random.choice([nome_a,nome_b,nome_c,nome_d])
print(f"O escolhido para apagar o quadro é o alun@: {escolhido}")