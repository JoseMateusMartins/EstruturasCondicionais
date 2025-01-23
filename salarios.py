salario = float(input("Informe seu salário:"))
if salario<=1000:
    aumento1=salario*0.3
    novosalario1=salario+aumento1
    print("Seu novo salário é:",novosalario1)
elif salario<=2000:
    aumento2=salario*0.25
    novosalario2=salario+aumento2
    print("Seu novo salário é:",novosalario2)
elif salario<=3000:
    aumento3=salario*0.2
    novosalario3=salario+aumento3
    print("Seu novo salário é:",novosalario3)
elif salario<=4000:
    aumento4=salario*0.15
    novosalario4=salario+aumento4
    print("Seu novo salário é:",novosalario4)
else:
    aumento5=salario*0.1
    novosalario5=salario+aumento5
    print("Seu novo salário é:",novosalario5)