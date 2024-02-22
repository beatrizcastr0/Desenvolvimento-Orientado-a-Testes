#Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. 
#Faça um procedimento que receba as duas notas por parâmetro
#calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
#foi aprovado (considere 6.0 a média mínima para aprovação).

def calcular_media_semestral(av1, av2):

    mediaSemestral = (av1 + av2) / 2
    return mediaSemestral

def verificar_aprovacao(media):

    if media >=6.00:
        print('\nPARABÉNS! Você foi aprovado!')
    else: 
        print('\nNão aprovado')    

av1 = int(input('\nDigite a nota da AV1: '))
av2 = int(input('\nDigite a nota da AV2: '))

mediaSemestral = calcular_media_semestral(av1, av2)
verificar_aprovacao (mediaSemestral)
print(f"\nA média semestral é: {mediaSemestral:.2f}")
