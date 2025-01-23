ip = int(input("Informe o IP:"))
if ip<=127:
    print("Esse ip é de classe A.")
elif ip<=191:
    print("Esse ip é de classe B.")
elif ip<=223:
    print("Esse ip é de classe C.")
elif ip<=239:
    print("Esse ip é de classe D.")
else:
    print("Esse ip é de classe E.")