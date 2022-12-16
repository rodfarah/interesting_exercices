from validacao_cpf import CPF_1o_dig
from validacao_cpf import CPF_2o_dig
import random

n_cpfs_txt = input('Quantos CPFs você deseja gerar? ')
n_cpfs_int = int(n_cpfs_txt)

try_n = 1
valid_CPF_list = []
while try_n <= n_cpfs_int:
    random_cpf = ''
    for digit in range(11):
        random_cpf += (str(random.randint(0,9)))
    print(random_cpf)
    if CPF_1o_dig(random_cpf) == True and CPF_2o_dig(random_cpf) == True:
        print(f'O CPF {random_cpf} é válido.\n')
        valid_CPF_list.append(random_cpf)
        try_n += 1
    else:
        print()
        continue
        
print(f'Os CPF válidos gerados são: {valid_CPF_list}')