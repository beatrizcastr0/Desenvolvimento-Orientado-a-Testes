#10. Escreva um programa composto de uma função Max e o programa principal como segue:
#a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
#b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função Max.

def Max (num1, num2):
    if num1 >= num2:
        return num1
    else: 
        return num2 

def main():
    for _ in range(4):
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = int(input("Digite o terceiro número: "))
        d = int(input("Digite o quarto número: "))

    
        maior_numero = Max(Max(Max(a, b), c), d)
    
        print("\nO maior número da série é:", maior_numero)
        print()

if __name__ == "__main__":
    
    main()