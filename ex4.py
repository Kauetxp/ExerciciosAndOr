#4 - Escreva um código que verifique se um número é par ou divisível por 3.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    if numero % 2 == 0 and numero % 3 == 0:
        print("Par e divisível por 3")
    else:
        print("Par")
elif numero % 3 == 0:
    print("Divisível por 3")

else:
    print("Impar")
