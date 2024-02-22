#Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
#do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
#Área = PI * r2; Perímetro = PI * 2 * r;

def area(r): #Definindo função chamada 'area' que recebe argumento 'r'
    return 3.14 * r**2 #calcula e retorna a área do círculo

def perimetro(r): #Função chamada 'perímetro' que recebe argumento 'r', calcula e retorna o perímetro do círculo.
    return 3.14 * 2 * r

raio = int(input("\nDigite o raio do círculo: "))
print("\nA área do círculo é: %.2f" % area(raio))
print("\nO perímetro do círculo é %.2f: " % perimetro(raio))
