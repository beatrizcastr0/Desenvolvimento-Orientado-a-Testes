#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)

def calcular_valor_S(N):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("\nO valor deve ser um inteiro positivo")

    valor_S = 0

    for t in range(2, N + 2):
        numerador = t**2 + 1
        denominador = t + 3
        termo = numerador / denominador
        valor_S += termo

    return valor_S

valor_N = 5
resultado_S = calcular_valor_S(valor_N)
print(f"\nO valor de S para N={valor_N} é {resultado_S}")
