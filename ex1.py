# 1 -Escreva um programa que peça ao usuário inserir três números e, em seguida, 
# determine se um dos três números é maior que a soma dos outros dois.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2+n3:
    print(n1, "é maior do que a soma de",n2,n3)
elif n2 > n1+n3:
    print(n2, "é maior do que a soma de",n1,n3)
elif n3 > n1+n2:
    print(n3, "é maior do que a soma de",n2,n1)
else:
    print("Nenhum número é maior do que a somas dos outros dois.")
    