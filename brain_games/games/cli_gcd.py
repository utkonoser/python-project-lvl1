import random
import prompt


def brain_gcd():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i <= 3:
        if i == 3:
            return print(f'Congratulations, {name}!')
        random_num1 = random.randint(1, 50)
        random_num2 = random.randint(1, 50)
        print(f'Question: {random_num1} {random_num2}')
        answer = prompt.string('Your answer: ')
        divs1, divs2, fin_divs = [1], [1], [1]
        for j in range(1, random_num1 + 1):
            if random_num1 % j == 0:
                divs1.append(j)
        for j in range(1, random_num2 + 1):
            if random_num2 % j == 0:
                divs2.append(j)
        if random_num1 > random_num2:
            for j in divs1:
                if j in divs1 and j in divs2:
                    fin_divs.append(j)
        if random_num1 < random_num2:
            for j in divs2:
                if j in divs1 and j in divs2:
                    fin_divs.append(j)
        if random_num1 == random_num2:
            fin_divs.append(random_num1)
        if (str(max(fin_divs)) == answer):
            print('Correct!')
            i += 1
        if (str(max(fin_divs)) != answer):
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{str(max(fin_divs))}\'.')
            return print(f'Let\'s try again, {name}!')
