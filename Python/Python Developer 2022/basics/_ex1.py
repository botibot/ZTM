picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for line in picture:
    render = ''
    for pos in line:
        if pos == 0:
            rend = ' '
        if pos == 1:
            rend = '*'
        render = render + rend
    print(render)


for row in picture:
    for pixel in row:
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    print('')


some_list = ['a','b','c','b','d','m','n','n']
some_list.sort()
repeat_list = []

index = 0
while index < len(some_list) - 1:
    if some_list[index] == some_list[index + 1]:
        repeat_list.append(some_list[index])
    index += 1

print(repeat_list)

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)