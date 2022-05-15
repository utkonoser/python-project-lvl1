import random
import prompt


def brain_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 3:
        random_num = random.randint(1, 100)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')
        result = random_num % 2
        if (result == 0 and answer == 'yes') or (result != 0 and
                                                 answer == 'no'):
            print('Correct!')
            i += 1
        if (result == 0 and answer != 'yes'):
            print(f'\'{answer}\' is wrong answer ;(. \
            Correct answer was \'yes\'.')
            return f'Let\'s try again, {name}!'
        if (result != 0 and answer != 'no'):
            print(f'\'{answer}\' is wrong answer ;(. \
            Correct answer was \'no\'.')
            return f'Let\'s try again, {name}!'
        if i == 3:
            return print(f'Congratulations, {name}!')
