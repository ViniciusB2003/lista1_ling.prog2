
palfabetico = []
while(True):
    paises = []
    x = str(input("Digite um nome de um país: "))
    paises.append(x)
    T = input("Deseja Continuar?, S/N ")
    if T == "N":
        break

palfabetico = sorted(paises)

pos = input("Qual o país que você quer saber a posição? ")
print(palfabetico.index(pos))







