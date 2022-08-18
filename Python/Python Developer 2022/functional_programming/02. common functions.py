
#!map. filter, zip and reduce

from functools import reduce

#! map(action, data) <- Easier way to think of map

my_list = [1,2,3]
def multiply_by2(i):
    return i * 2

print(map(multiply_by2, my_list))
print(list(map(multiply_by2, my_list)))
new_list = map(multiply_by2, [1,2,3,4])
print(list(new_list))
print(my_list)

#! filter <- Filters things

def only_odd(i):
    return i % 2 != 0 # <-evaluates to a boolean expresion

print(list(map(only_odd, my_list))) # <- returns all the results of the evaluation
print(list(filter(only_odd, my_list))) # <- returns the expected result


#! zip <- get's thing together from iterables
your_list = [10,20,30]
print(list(zip(my_list, your_list)))

their_list = (5,4,3)
print(list(zip(my_list, your_list, their_list)))

#! reduce <-- 

def accumulator(acc, i):
    print(acc, i)
    return acc + i

print(reduce(accumulator ,my_list, 10))