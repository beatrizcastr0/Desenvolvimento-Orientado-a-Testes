#Escreva uma função que recebe 2 números n1 e n2 como entrada e retorna a soma de todos os números inteiros
#Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.


def somar_numeros(n1, n2):

    soma = n1 + n2
    return soma

somanumero = int(input('\ndigite um numero: '))
somanumero2 = int(input('\ndigite um numero: '))
resultado = somar_numeros(somanumero, somanumero2)

print('\n o resultado da soma é', resultado)

