#Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
#- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
#- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
#- Se o número de lados for igual a 5, escrever PENTÁGONO.
#Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

def calcular_poligono(lados, medida_lado):
    if lados == 3:
        perimetro = 3 * medida_lado
        print('\nTRÂNGULO - Perímetro:', perimetro)
    elif lados == 4:
        area = medida_lado ** 2
        print('QUADRADO - Área:', area)
    elif lados == 5:
        print('PENTÁGONO')
    else:
        print('Número de lados inválido. Informe 3, 4 ou 5')

    num_lados = int(input('Digite o número de lados (3, 4 ou 5): '))
    medida_lado = float(input('Digite a medida do lado (em centímetros): '))

    calcular_poligono(num_lados, medida_lado) 