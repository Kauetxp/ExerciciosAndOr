#6 - Criar um programa que verifica se uma pessoa tem desconto em um produto,
# baseado na idade e sua categoria (estudante, aposentado, etc.) e no dia da semana.
# (Use quantas categorias desejar)

#idoso = 10%
#est = 25%
#apo = 20%
#funça = 5%
#seg a sex = 5%
#descontos são acumulativos

idade = int(input("Qual sua idade? "))
d = 0
if idade >= 60:
    d = 10
    cat = int(input("Qual sua categoria? \n1-Estudante\n2-Aposentado\n3-Funcionário Público\n4-Nenhuma\n"))
    if cat == 1:
        d = d + 25
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5
    elif cat ==2:
        d = d+20
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5
    elif cat ==3:
        d = d+5
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5
    else:
        d = d + 0
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5
else:
    cat = int(input("Qual sua categoria? \n1-Estudante\n2-Aposentado\n3-Funcionário Público\n4-Nenhuma\n"))
    if cat == 1:
        d = d + 25
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5
    elif cat ==2:
        d = d+20
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5
    elif cat ==3:
        d = d+5
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5
    else:
        d = d + 0
        dia = int(input("Dia de semana:\n1-Dom\n2-Seg\n3-Ter\n4-Qua\n5-Qui\n6-Sex\n7-Sab\n"))
        if dia == 1 or dia == 7:
            d= d+0
        else:
            d = d+5

print("Você ganhou",d,"por cento de desconto")
