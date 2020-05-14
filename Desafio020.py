import random
print(f"{'*'*10}Desafio 020 - Sorteio Apresentação{'*'*10}")
nome_a = input("Informe o nome do primeiro aluno: ")
nome_b = input("Informe o nome do segundo aluno: ")
nome_c = input("Informe o nome do terceiro aluno: ")
nome_d = input("Informe o nome do quarto aluno: ")
alunos = [nome_a, nome_b, nome_c, nome_d]
random.shuffle(alunos)
print(alunos)
