#Desenvolva um algoritmo que solicite ao usuário que digite duas strings e
#verifique se as strings têm o mesmo comprimento. Se as strings tiverem
#comprimentos diferentes, levante uma exceção personalizada com uma
#mensagem de erro apropriada. Em seguida, imprima uma mensagem informando
#que as strings têm o mesmo comprimento.
try:
    x = str(input("Digite uma palavra: "))
    y = str(input("Digite outra palavra do mesmo tamanho do anterior: "))
    if len(x) != len(y):
        raise Exception("Tamanhos Diferentes")
except Exception as e:
    print(e)
else:
    print("Tamanhos Iguais")
