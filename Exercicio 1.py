try:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 1:
        raise Exception("Numero impar")
except Exception as e:
    print(e)
else:
    print("O Número é par")

