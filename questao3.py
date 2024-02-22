# Escreva um programa para ler uma temperatura em graus Fahrenheit.
# Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius.
# Fórmula: C= ((F-32)/9)*5

def celsius(F): #Definindo função chamada 'celsius' que recebe argumento 'F'

    C = ((F-32)/9)*5 # Dentro da função, calculamos a temperatura em celsius usando a formula de conversao

    return C #A funçao retorna o valor da temperatura em celsius

temperatura_fahrennheit = float(input('\ndigite a temperatura em Fahrenheit: '))

#Solicitamos ao usuário que digite a temperatura em Fahrenheit.
#A função 'input' é usada para obter a entrada do usuário
#'float' é usado para converter a entrada em um número de ponto flutuante
#Temperaturas podem incluir decimais.

temperatura_celsius = celsius(temperatura_fahrennheit)

#Chamamos a função celsius passando a temperatura em Fahrenheit como argumento. 
#O resultado é armazenado na variável 'temperatura_celsius'

print('a temperatura é de', temperatura_celsius, 'graus Celsius.')

#Imprimimos a temperatura convertida em Celsius na tela, junto com uma mensagem informativa. 
#A função print é usada para mostrar o resultado ao usuário.