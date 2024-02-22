#11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def contar_divisores(numero):
    if numero <= 0 or not isinstance(numero, int):
        raise ValueError("\nO valor deve ser um número inteiro positivo.")

    count_divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            count_divisores += 1

    return count_divisores

valor = int(input('\nDigite o valor inteiro e positivo para retornar o nº de divisores:'))
resultado = contar_divisores(valor)
print(f"\nO número {valor} possui {resultado} divisores.")
