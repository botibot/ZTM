#!DRY Do not repeat yourself

#! Positional Parameters and Arguments
# parameters
def say_hello(name, emoji):
    print(f'Helllooooo {name} {emoji}')


#! default parameters are set on the definition of the function
def say_hello2(name='Darth Vader', emoji='😈'):
    print(f'Helllooooo {name} {emoji}')


# arguments --> call or invoke
say_hello('Jorge', '🤪 💩')
print(say_hello)

#! keyword arguments
# * bad practice?
say_hello(emoji='💩', name='Bibi')
say_hello(name='Bibi', emoji='💩')

say_hello2()
say_hello2('Jorge', '✊')


#!Return
def suma(num1, num2):
    return num1 + num2


print(suma(4, 5))
