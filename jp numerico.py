import math
def calFactorial(numero):
    return math.factorial(numero)

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True
def es_perfecto(numero):
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

def convertir_a_binario(numero):
    return bin(numero)[2:]

numero = int(input("Ingrese un valor en base 10 (0-9): "))

if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

if es_perfecto(numero):
    print(f"El número {numero} es perfecto.")
else:
    print(f"El número {numero} no es perfecto.")

binario = convertir_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")


#Juan Pablo Zacarias Paiz
#201805637