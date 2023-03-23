def validar(msg, validos):
    valor = str(input(msg)).upper()
    while not valor in validos:
        print("Digitou errado")
        valor = str(input(msg)).upper()
    return valor
def buscamaiorquantidade(opcoes):
    itens = [0,0,0]
    for resposta in respostas:
        for opcao in opcoes:
            itens[opcoes.index(opcao)] += 1
    return opcoes[itens.index(max(itens))]
 
elevadores = ["A", "B", "C"]
turnos = ["M", "V", "N"]
respostas = []

while(true):
    elevador = validar("informe o elevador mais utilizado", elevadores)
    turno = validar("Informe o turno mais utilizado: ", turnos)

    respostas.append([elevador, turno])

    if input("Deseja continuar? S/N").upper() != "S":
        break

print("O Elevador mais usado é o elevador: ", buscamaiorquantidade(elevadores))
print("O turno  mais usado é o elevador", buscamaiorquantidade(turnos))




