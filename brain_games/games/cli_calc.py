import random
import prompt


def brain_calc():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    while i <= 3:
        if i == 3:
            return print(f'Congratulations, {name}!')
        list_of_exp = ['+', '-', '*']
        random_exp = random.choice(list_of_exp)
        random_num1 = random.randint(1, 25)
        random_num2 = random.randint(1, 10)
        print(f'Question: {random_num1} {random_exp} {random_num2}')
        answer = prompt.string('Your answer: ')
        if random_exp == '+':
            result = random_num1 + random_num2
        if random_exp == '-':
            result = random_num1 - random_num2
        if random_exp == '*':
            result = random_num1 * random_num2
        if (str(result) == answer):
            print('Correct!')
            i += 1
        if (str(result) != answer):
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'.')
            return print(f'Let\'s try again, {name}!')
