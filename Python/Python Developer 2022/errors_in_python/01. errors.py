#Error Handling

while True:
    try:
        age = int(input('Whats is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')        
    else:
        print('thank you')
        break
    finally:
        print('ok, finally done')


def suma(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'error: {err}')

print(suma(1, '0'))