my_list = [5,4,3]

print(list(map(lambda i: i ** 2, my_list)))

#List Sorting by the second item
a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)

#! hard to get used to the syntax