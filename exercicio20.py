numeros = []
numerosImpar = []
numerosPar = []
numerosPos = []
numerosNeg = []
zeros = []
for x in range(5):
    numero1 = float(input("Digite os números: "))
    numeros.append(numero1)
    if numero1 % 2 != 0:
        numerosImpar.append(numero1)
    else:
        numerosPar.append(numero1)
    if numero1 > 0:
        numerosPos.append(numero1)
    elif numero1 < 0:
        numerosNeg.append((numero1))
    elif numero1 == 0:
        zeros.append(numero1)
print(f"Os números que vc digitou foi: {numeros}")
print(f"Os pares são: {numerosPar}" "\n"
      f"Os impar são: {numerosImpar}" "\n"
      f"Os positivos são: {numerosPos}" "\n"
      f"Os negativos são: {numerosNeg}" "\n"
      f"Os zeros que apareceram foi: {zeros}")