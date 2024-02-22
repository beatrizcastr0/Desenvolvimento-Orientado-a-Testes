def peso_ideal(altura, sexo):
    if sexo == 1:
        peso_ideal_mulher = (62.1 * altura) - 44.7
        return peso_ideal_mulher
    elif sexo == 2:
        peso_ideal_homem = (72.7 * altura) - 58
        return peso_ideal_homem
    else:
        print('\nCódigo do sexo inválido. Use 1 para feminino e 2 para masculino.')

altura = float(input('\nDigite a altura em metros: '))
sexo = int(input('\nDigite o código do sexo (1 para feminino, 2 para masculino): ')) 

peso_ideal_resultado = peso_ideal(altura, sexo)

if peso_ideal_resultado is not None:
    print('\nPeso ideal: ', peso_ideal_resultado)