#list, set, dictionary


#List

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

my_second_list = [char for char in 'hello']
print("list1 \n", my_second_list)

my_list2 = [num for num in range(0,100)]
print ("list2 \n",my_list2)

my_list3 = [num*2 for num in range(0,100)]
print("list3 \n", my_list3)

my_list4 = [num ** 2 for num in range(0,100) if num % 2 == 0]
print("list4 \n", my_list4)

#set

my_second_set = {char for char in 'hello'}
print("set1" + "\n", my_second_set)

my_set2 = {num for num in range(0,100)}
print ("set2" + "\n", my_set2)

my_set3 = {num*2 for num in range(0,100)}
print("set3" + "\n", my_set3)

my_set4 = {num ** 2 for num in range(0,100) if num % 2 == 0}
print("set4" + "\n", my_set4)

#dictionary

simple_dict = {
    'a':1,
    'b':2,
}

my_dict = {k:v**2 for k,v in simple_dict.items()}

print("dictionary1 \n", my_dict)

my_dict2 = {k:v**2 for k,v in simple_dict.items() if v%2==0}

print("dictionary2 \n", my_dict2)

my_dict3 = {num:num*2 for num in [1,2,3]}

print("dictionary3 \n", my_dict3)

some_list = ['a','b','c','b','d','m','n','n']
duplicates = list(set([x for x in some_list if some_list.count(x) >= 2 ]))

print(duplicates)