import enum


dictionary = {
    'a': 1,
    'b': 2,
}

print(dictionary['b'])

my_list = [1,2,3,4,5,6,7,8,9,10]

counter, x = 0, 0
for item in my_list:
    x += 1
    counter = counter + item

print(x, counter)

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print (f'index of 50 is: {char}')
        break


i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Done with the work')

while True:
    response = input('Say something: ')
    if response == 'bye':
        break