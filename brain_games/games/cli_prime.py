import random
import prompt


def brain_prime():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i <= 3:
        if i == 3:
            return print(f'Congratulations, {name}!')
        random_num = random.randint(1, 100)
        prime = 'yes'
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')
        if random_num == 2 or random_num == 3:
            prime = 'yes'
        if (random_num % 2 == 0 and random_num != 2)\
           or (random_num % 3 == 0 and random_num != 3)\
           or (random_num % 5 == 0 and random_num != 5)\
           or (random_num % 7 == 0 and random_num != 7) or (random_num == 1):
            prime = 'no'
        if (prime == answer):
            print('Correct!')
            i += 1
        if (prime != answer):
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{prime}\'.')
            return print(f'Let\'s try again, {name}!')
