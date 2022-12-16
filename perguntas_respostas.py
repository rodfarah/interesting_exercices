# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

question_num = 1  # Question Number
w_a_count = 0  # Wright Answer Counter

while question_num <= len(perguntas):
    for pergunta in perguntas:
        wright_ans = []
        print(pergunta['Pergunta'])
        print()
        print('Opções:')
        for num, option in enumerate(pergunta['Opções']):
            print(num, option, sep=') ')
            if option == pergunta['Resposta']:
                wright_ans.append(str(num))

        answer = input('Qual é o número da sua opção? ')
        if answer == wright_ans[0]:
            print(f'Acertou! \n')
            question_num += 1
            w_a_count += 1
            continue
        else:
            print(f'Errou!\n')
            question_num += 1
            continue

print(f'Você acertou {w_a_count} de {len(perguntas)} perguntas.')
