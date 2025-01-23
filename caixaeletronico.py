saque = int(input("Informe o valor do saque R$:"))
total = saque
cedula = 200
totalcedula = 0
while True:
    if total >=cedula:
        total -=cedula
        totalcedula +=1
    else:
        if totalcedula>0:
            print(f"Total de {totalcedula} cédulas de R${cedula}")
        if cedula ==200:
            cedula = 100
        elif cedula ==100:
            cedula=50
        elif cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=5
        elif cedula==5:
            cedula=2
        elif cedula==2:
            cedula=1
        totalcedula = 0
        if total==0:
            break