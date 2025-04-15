#exercicio 01
nome_completo = input("Digite seu nome completo: ")
primeiro_nome = nome_completo.split()[0]
print(f"Bem-vindo(a) ao Python, {primeiro_nome}")

#exercicio 02
nota1 = int(input("Digite a nota do primeiro bimestre da disciplina: "))
nota2 = int(input("Digite a nota do segundo bimestre da disciplina: "))
media_parcial = (nota1 * 2 + nota2 * 3) / 5
print("Média parcial =", media_parcial)