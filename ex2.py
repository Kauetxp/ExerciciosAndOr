# 2 - Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) 
# e determine se o aluno passou ou não. Um aluno passa se a soma das notas for maior 
# ou igual a 60 e nenhuma nota é menor que 40.

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

sn = n1 + n2

if sn >= 60 and n1>=40 and n2 >=40:
    print("Parabéns, você passou!")
else: 
    print("Reprovado.")