salario = 1320.00
gerenten = salario * 0.10
gerentemv = salario * 0.15
opn = salario * 0.09
opmv = salario * 0.14
funcionarios = []

while(True):
    nome = input("Digite o nome do funcionário, ou digite encerrar para sair")
    if nome == "sair":
        break
    
    while (True):
        horas = float(input("Digite o valor de horas trabalhadas pelo funcionario, informe um valor inteiro"))
        break
    while (True):
        turno = (input("Digite o turno que o funcionario trabalha, sendo M para matutino, V para vespertino e N para noturno"))
        if (turno == "M" or turno == "V" or turno == "N"):
            break
        else:
            print("Valor inválido, digite novamente")
    while (True):
        categoria = input("Digite a categoria do funcionário, sendo G para Gerente e O para operário")
        if (categoria == "G" or categoria == "O"):
            break
        else:
            print("Valor inválido, digite novamente")
            
    if (categoria == "G" and turno == "N"):
        salariof = gerenten * horas
    if (categoria == "G" and turno == "M" or turno == "V"):
        salariof = gerentemv * horas
    if (categoria == "O" and turno == "N"):
        salariof = opn * horas
    if (categoria == "O" and turno == "M" or turno == "V"):
        salariof = opmv * horas
    
    funcionario = [nome, horas, turno, categoria, salariof, "Reais"]
    funcionarios.append(funcionario)

for funcionario in funcionarios:
    print(funcionario)
    
        
    