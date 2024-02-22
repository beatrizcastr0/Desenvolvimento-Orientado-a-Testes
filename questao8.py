#Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
#caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
#programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
#números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def obter_caractere_valido():
    while True:
        resposta = input("\nDigite 'S' para continuar ou 'N' para parar: ").upper()
        if resposta == 'S' or resposta == 'N':
            return resposta
        else:
            print("\nCaractere inválido. Digite novamente.")

def calcular_cubo(numero):
    return numero ** 3

def main():
    continuar = 'S'

    while continuar == 'S':
        numero = float(input("\nDigite um número: "))
        resultado_cubo = calcular_cubo(numero)
        print(f"\nO cubo de {numero} é {resultado_cubo}")

        continuar = obter_caractere_valido()

    print("\nPrograma encerrado.")

if __name__ == "__main__":
    main()
