distancia = int(input("Informe a distância do robô no momento do lançamento(mínimo:0,máximo:2000)):"))
if distancia<=800:
    print("Esse lançamento vale 1 ponto.")
elif distancia<=1400:
    print("Esse lançamento vale 2 pontos.")
else:
    print("Esse lançamento vale 3 pontos.")