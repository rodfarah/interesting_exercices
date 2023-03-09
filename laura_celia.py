# Levando em conta um número de dois algarismos, cuja soma deles, multiplicado por 3 é igual ao próprio número.



# (first_num + second_num) * 3 == (first_num*10) + second_num

def celia_laura():

    for num1 in range(1, 10):
        for num2 in range(1, 10):
            if (num1 + num2) * 3 == num1 * 10 + num2:
                return f'{num1}{num2}'


print(celia_laura())