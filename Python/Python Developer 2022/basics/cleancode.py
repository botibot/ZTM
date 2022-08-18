
# * Clean Code

#!Example Code
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


print(is_odd_or_even(51))


#!Clean Code
def is_even(num):
    return num % 2 == 0


print(is_even(50))
