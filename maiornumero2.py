numero1 = int(input("Insira o primeiro número:"))
numero2 = int(input("Insira o segundo número:"))
numero3 = int(input("Insira o terceiro número:"))
if numero1>numero2 and numero1>numero3:
    print("O primeiro número é o maior número,que é",numero1)
elif numero2>numero3:
    print("O segundo número é o maior número,que é",numero2)
else:
    print("O terceiro número é o maior número,que é",numero3)