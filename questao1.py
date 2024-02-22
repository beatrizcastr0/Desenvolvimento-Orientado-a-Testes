#1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

def verificar_paridade(numero):
    return numero % 2 == 0

numero_teste = 7
resultado = verificar_paridade(numero_teste)

if resultado:
    print(f"\nO número {numero_teste} é par.")
else:
    print(f"\nO número {numero_teste} é ímpar.")
