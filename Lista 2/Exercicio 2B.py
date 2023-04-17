from collections import deque
fila = deque([int(input("Digite o primeiro número da lista: "))])
while(True):
    fila.append(int(input("Digite o próximo número da lista: ")))
    t = input("Deseja Continuar? S/N")
    if t == "N":
        break
fila.popleft()
print(fila)
