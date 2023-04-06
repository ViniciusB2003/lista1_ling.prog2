try:
    palavra = str(input("Escreva uma palavra somenter com letras maiúsculas: "))
    for x in palavra:
        if x != x.upper():
            raise Exception("Palavra com letra minuscula")
except Exception as e:
    print(e)
else:
    print("Possui apenas letras maiusuculas")

    
