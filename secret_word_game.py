def Secret_Word_Game(word):
    """
    Faça um jogo para o usuário adivinhar qual
    a palavra secreta.
    - Você vai propor uma palavra secreta
    qualquer e vai dar a possibilidade para
    o usuário digitar apenas uma letra.
    - Quando o usuário digitar uma letra, você 
    vai conferir se a letra digitada está
    na palavra secreta.
        - Se a letra digitada estiver na
        palavra secreta; exiba a letra;
        - Se a letra digitada não estiver
        na palavra secreta; exiba *.
    Faça a contagem de tentativas do seu
    usuário.
    """

    print('*Secret Word Game*\n')

    # Let's ask the user to type how many tries he would like \
    # to have and let's check if it is really a number:
    word_lenght = len(word)
    print(
        f'The secret word has {word_lenght} letters and you must guess them, one by one, until you discover the whole word!')
    while True:

        try:
            hmtries_str = input(
                'How many tries you would like to have? ')
            print('')
            hmtries_int = int(hmtries_str)
            if hmtries_int < (word_lenght - 2):
                print(
                    f'The secret word has {word_lenght} letters! I\'d recommend you have at least {word_lenght - 2} tries! \n')
                continue
            break
        except:
            print('Please, enter a number!')
            continue

    # Let's proceed creating some variables:
    word = word.lower()

    correcting_word = word_lenght * '*'
    unique_letters = set([letter for letter in word])

    past_guesses = []

    sbs_list = []  # step-by-step list

    # Let's create a dict with hmtries_int:

    tries_dict = {}
    for shoot in range(1, hmtries_int+1):
        tries_dict[f'try_n_{shoot}'] = ''

    tries = 1
    while correcting_word != word:
        if tries > hmtries_int:
            break

        # Let's first check if the word is a valid entry:

        while True:
            print(
                f'This is TRY NUMBER {tries} ({hmtries_int - tries} more left to go)')
            if hmtries_int == tries:
                print('(This is your LAST TRY!) ',end='')
            guess = input('Pick a letter: ')

            if guess.isalpha() and len(guess) == 1:
                guess = guess.lower()
                break
            else:
                print('Please, type ONE WORD (a to z)\n')
                continue

        # Let's check if user had already picked this letter before:
        if guess in past_guesses:
            print(
                f'You have already choosen the letter "{guess}". Please, choose a different one and I won\'t charge you one try!')
            print(f'Until now you have found this:\n{correcting_word}\n')

            continue
        # Let's proceed to the principal validation:
        elif guess in unique_letters:
            print('NICE SHOT!!')
            past_guesses.append(guess)
            for letter in word:
                if guess == letter:
                    sbs_list.append(letter)
                else:
                    sbs_list.append('*')
            if tries == 1:
                tries_dict[f'try_n_{tries}'] = "".join(sbs_list)
                print('Until now you have found this:\n',
                      tries_dict[f'try_n_{tries}'], '\n', sep='')
                correcting_word = tries_dict[f'try_n_{tries}']
                sbs_list.clear()
                tries += 1
            elif tries > 1:
                idx = 0
                previous_dict = tries_dict.get(f'try_n_{tries - 1}')
                while idx < word_lenght:
                    if previous_dict[idx] == '*':
                        tries_dict[f'try_n_{tries}'] = tries_dict[f'try_n_{tries}'] + (
                            sbs_list[idx])
                        idx += 1
                    else:
                        tries_dict[f'try_n_{tries}'] = tries_dict[f'try_n_{tries}'] + (
                            tries_dict[f'try_n_{tries - 1}'][idx])
                        idx += 1
                sbs_list.clear()
                print(f'Until now you have found this:\n',
                      tries_dict[f'try_n_{tries}'], '\n', sep='')
                correcting_word = tries_dict[f'try_n_{tries}']
                tries += 1
        else:
            print(
                f'Sorry... There is no letter "{guess}" in the Secret Word.')
            print(f'Until now you have found this:\n{correcting_word}\n')
            past_guesses.append(guess)
            if tries == 1:
                tries_dict[f'try_n_{tries}'] = correcting_word
            else:
                tries_dict[f'try_n_{tries}'] = tries_dict[f'try_n_{tries - 1}']
            tries += 1
    else:
        print(
            f'CONGRATULATIONS!\nYou found out the Secret Word: "{word.capitalize()}"\nYou made it in {tries -1} (of {hmtries_int}) tries!')
        quit()
    print(
        'YOU FAILED because you\'ve reached the limit of tries...\n')

    while True:
        reveal = input('Do you want me to reveal the Secret Word?[Y/N]: ')
        if reveal.lower() == 'y':
            print(
                f'\nok! Here it goes: "{word.capitalize()}"\nThanks for playing!')
            break
        elif reveal.lower() == 'n':
            print('\nOk! Thanks for playing!')
            break
        else:
            print('Please, type only [Y/N]!')
            continue


print(Secret_Word_Game('Guitarra'))
