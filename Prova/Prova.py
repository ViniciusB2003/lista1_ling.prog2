
try:
    while(True):
        mesano = int(input("Informe o mes: " ))
        rendliq = input("Digite seu Rendimento Liquido Mensal: ")
        if not rendliq.isdigit():
            raise Exception ("O Valor deve ser um número")
        t = str(input("Deseja Continuar: "))
        if t == "N":
            break
except Exception as e:
    print(e)



