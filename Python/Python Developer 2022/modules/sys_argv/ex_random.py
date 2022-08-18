from sys import argv #! <- Sends args from the terminal
from random import randint

start = int(argv[1])
end = int(argv[2])
random_number = randint(start, end)
print(random_number)

while True:
    try:
        number = int(input(f'try to guess the number between {start} ~ {end}: '))
        if start <= number <= end:
            if number == random_number:
                print('\n congratulations you are a genius')
                break
            else:
                print('\n not the correct number, keep trying')
        else:
            print(f'\n number between {start} ~ {end}')
    except(ValueError):
        print('\n please enter a number')
        continue