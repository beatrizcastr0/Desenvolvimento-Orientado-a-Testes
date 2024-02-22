#Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

def calcular_somatorio(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("\nO valor deve ser um inteiro positivo")

    somatorio = sum(range(1, n + 1))
    
    return somatorio

valor = 5
resultado = calcular_somatorio(valor)
print(f"\nO somatório de 1 até {valor} é {resultado}")
