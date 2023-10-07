a = []
while len(a) < 10:
    numero = int(input("Digite um número: "))
    if numero % 2 != 0:
        a.append(numero)
print(a)
