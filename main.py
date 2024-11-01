import re

def arithmetic_arranger(problems, show_answers=False):
    input_problems = input('Enter up to 4 problems, + or - only and\nup to 4 digits in length separated by a comma:')
    if input_problems == 'exit':
        exit()
    problems = input_problems.split(",")

    print(problems)
    return problems

spaces = '  '
dashes = '-----'
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{32:5}{spaces}{3801:5}{spaces}{45:5}')
print(f'+{688:4}{spaces}-{2:4}{spaces}+{43:4}')
print(f'{dashes}{spaces}{dashes}{spaces}{dashes}{spaces}')


if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
