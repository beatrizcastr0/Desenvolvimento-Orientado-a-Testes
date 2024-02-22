#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

import math

def calcular_valor_S(N):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("\nO valor deve ser um inteiro positivo")

    valor_S = sum(1 / math.factorial(i) for i in range(N + 1))
    
    return valor_S

valor_N = 5
resultado_S = calcular_valor_S(valor_N)
print(f"\nO valor de S para N={valor_N} é {resultado_S}")

