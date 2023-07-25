'''
primeiro dígito
'''
while True:
    cpf_enviado = str(input('Digite seu CPF sem pontos e traços: '))
    '''
    primeiro dígito
    '''
    nove_digitos = cpf_enviado[:9]
    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    '''
    segundo dígito 
    '''
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito_2 in dez_digitos:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    '''
    Validar CPF
    '''
    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    if cpf_enviado == cpf_gerado:
        print('CPF:', cpf_enviado, 'é válido')
    else: 
        print('CPF inválido')
