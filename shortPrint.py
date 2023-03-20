from time import sleep
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

for i in range(0, 20):
    # print('\n\n\n')
    print(' ' * i + '.')
    sleep(0.1)
    clear()