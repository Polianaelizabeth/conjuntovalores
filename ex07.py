import math

valor = int(input("Digite um valor: "))

while valor > 0:
    quadrado = int(math.pow(valor, 2))
    cubo = int(math.pow(valor, 3))
    raiz = math.sqrt(valor)

    print("valor: ", valor, " quadrado: ", quadrado, " cubo: ", cubo, "raiz quadrada: ", raiz)
    valor = int(input(" digite um valor ( 0 ou número negativo para finalizar): "))

print("você digitou um valor <= 0, programa encerrado.")