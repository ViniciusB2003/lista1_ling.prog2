try:
    num = int(input("Digite um número pra ser divido pelo 10: "))
    if num == 0:
        raise Exception ("Não é possivel dividir por zero")
except Exception as e:
    print(e)
else:
    print(10/num)
