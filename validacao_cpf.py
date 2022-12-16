"""
Calculo do penúltimo dígito do CPF
CPF: 249.267.228-01
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  249.267.228-01 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O penúltimo dígito do CPF é 7

Calculo do último dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O último dígito do CPF é 0
"""


def CPF_1o_dig(CPF):

    # Vamos extrair apenas números do CPF e verificar se possui 11 dígitos:
    only_num = [int(num) for num in CPF if num.isdigit()]
    if len(only_num) != 11:
        raise ValueError('O CPF selecionado não possui 11 dígitos!')

    # Criar lista decrescente de 10 a 2
    multiplicadores_decrescentes = list(range(2, 11)[::-1])

    # Soma da multiplicação dos 9 primeiros dígitos do CPF pelos respectivos valores da lista decrescente:

    idx = 0
    lista_multiplicados = []
    while idx < 9:
        lista_multiplicados.append(
            only_num[idx] * multiplicadores_decrescentes[idx])
        idx += 1

    # Cálculo final antes da condição:
    resultado = (sum(lista_multiplicados) * 10) % 11

    digito_1 = 0 if resultado > 9 else resultado

    # Verificar se o penúltimo dígito do CPF informado confere com o calculado:
    if digito_1 == only_num[-2]:
        print("O penúltimo dígito do CPF informado é válido.")
        return True
    else:
        print("O penúltimo dígito do CPF informado NÃO é válido.")
        return False

def CPF_2o_dig(CPF):

    # Vamos extrair apenas números do CPF e verificar se possui 11 dígitos:
    only_num = [int(num) for num in CPF if num.isdigit()]
    if len(only_num) != 11:
        raise ValueError('O CPF selecionado não possui 11 dígitos!')

    # Criar lista decrescente de 10 a 2
    multiplicadores_decrescentes = list(range(2, 12)[::-1])
    # Soma da multiplicação dos 10 primeiros dígitos do CPF pelos respectivos valores da lista decrescente:

    idx = 0
    lista_multiplicados = []
    while idx < 10:
        lista_multiplicados.append(
            only_num[idx] * multiplicadores_decrescentes[idx])
        idx += 1
    # Cálculo final antes da condição:
    resultado = (sum(lista_multiplicados) * 10) % 11
    digito_2 = 0 if resultado > 9 else resultado

    # Verificar se o último dígito do CPF informado confere com o calculado:
    if digito_2 == only_num[-1]:
        print("O último dígito do CPF informado é válido.")
        return True
    else:
        print("O último dígito do CPF informado NÃO é válido.")
        return False
