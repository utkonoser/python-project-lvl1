import random
import prompt


def brain_progression():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    i = 0
    while i <= 3:
        if i == 3:
            return print(f'Congratulations, {name}!')
        random_num = random.randint(1, 20)
        random_step = random.randint(1, 10)
        random_len = random.randint(5, 12)
        random_elem = random.randint(1, random_len)
        numbers = ''
        result = 0
        j = 1
        while j <= random_len:
            if j == random_elem:
                result = random_num + (random_step * j)
                numbers += '.. '
                j += 1
            numbers += str(random_num + (random_step * j)) + ' '
            j += 1
        print(f'Question: {numbers}')
        answer = prompt.string('Your answer: ')
        if (str(result) == answer):
            print('Correct!')
            i += 1
        if (str(result) != answer):
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{str(result)}\'.')
            return print(f'Let\'s try again, {name}!')
