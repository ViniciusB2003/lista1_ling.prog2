from collections import deque
fila = deque([input("Digite o nome da pessoa na fila: ")])
while(True):
    fila.append(input("Digite o nome da proxima pessoa na fila: "))
    t = str(input("Deseja Continuar? S/N"))
    if t == "N":
        break

fila.popleft()
print(fila)
