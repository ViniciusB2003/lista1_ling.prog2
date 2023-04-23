pilha = [input("Digite a Url da página: ")]
t = str(input("Deseja Continuar? S/N")).upper()
while t == "S" and t != "N":
    pilha.append(input("Adicione a próxima URL da página: "))
    t = str(input("Deseja Continuar? S/N")).upper()
    if t != "S" and t != "N":
        print("Valor Inválido, Digite Novamente")
pilha.pop()
print(pilha)





