def validar(msg, validos):
    valor = str(input(msg)).upper()
    while not valor in validos:
        print("Digitou errado")
        valor = str(input(msg)).upper()
    return valor
 
elevadores = ["A", "B", "C"]
turnos = ["M", "V", "N"]
respostas = []

while(true):
    elevador = validar("informe o elevador mais utilizado", elevadores)
    turno = validar("Informe o turno mais utilizado: ", turnos)

    respostas.append([elevador, turno])

    if input("Deseja continuar? S/N").upper() != "S":
        break

elevadoresutilizados = [0,0,0]
for resposta in respostas:
    if resposta[0] == "A":
        elevadoresutilizados[0] +=1
    if resposta[0] == "B":
        elevadoresutilizados[1] += 1
    if resposta[0] == "C":
        elevadoresutilizados[2] += 1

maiorindice = elevadoresutilizados.index(max(elevadoresutilizados))
print("O Elevador mais usado é o elevador", elevadores[maiorindice])

turnosutilizados = [0,0,0]
for resposta in respostas:
    if resposta[0] == elevadores[maiorindice]:
        if resposta[0] == "M":
            turnosutilizados[0] +=1
        if resposta[0] == "V":
            turnosutilizados[1] += 1
        if resposta[0] == "N":
            turnosutilizados[2] += 1

indiceturno = turnosutilizados.index(max(turnosutilizados))
print("O Elevador mais utilizado", elevadores[maiorindice], "Sendo mais utilizado no turno", turnos[indiceturno])





