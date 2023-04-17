
numeros = []
while(True):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
    t = input("Deseja continuar? S/N ")
    if t == "N":
        break
inicio = int(input("Qual número voce quer adicionar no começo? "))
fim = int(input("Qual número voce quer colocar no fim? "))
numeros.insert(0,inicio)
numeros.append(fim)

print(numeros)

