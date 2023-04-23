pilha = []
pilha.append(int(input("Adicione um número inteiro: ")))
t = str(input("Deseja Continuar? S/N")).upper()
while t == "S" and t != "N":
    pilha.append(int(input("Adicione outro número inteiro: ")))
    t = str(input("Deseja Continuar? S/N")).upper()
    if t != "S" and t != "N":
        print("Valor Inválido, Digite Novamente")
pilha.pop()
print(pilha)
