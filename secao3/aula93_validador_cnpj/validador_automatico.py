from cnpjs import cnpjs


for cnpjs in cnpjs:
    lista_dígitos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    produto = []
    
    # Setign CNPJ's and cnpj_temporario's values
    CNPJ = [int(num) for num in cnpjs[0]]
    cnpj_temporario = CNPJ[0:-2]

    # For to calculate last two digits
    for i in range(0, 2):

        # Seting numbers to multiply
        if len(cnpj_temporario) == 12:
            lista_dígitos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        else:
            lista_dígitos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # Fiding digit
        produto = [num1*num2 for num1, num2 in zip(cnpj_temporario, lista_dígitos)]
        digito = 11 - (sum(produto) % 11)

        # Verifying validity digit
        if digito > 9:
            digito = 0
        cnpj_temporario.append(digito)

    # Verify CNPJ's validity
    if CNPJ == cnpj_temporario:
        e_valido = 'VÁLIDO'
    else:
        e_valido = 'INVÁLIDO'
    cnpj_str = [str(num) for num in CNPJ]
    cnpj_final = ''.join(cnpj_str)

    print(f'CNPJ: {cnpj_final} é {e_valido} | Correção: {cnpjs[1]}')
