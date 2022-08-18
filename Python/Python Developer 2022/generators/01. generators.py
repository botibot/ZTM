
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

def generator_func(num):
    for i in range(num):
        yield i*2   #! <- pauses the function

g = generator_func(100)
print(g)
next(g) 
next(g)
print(next(g))
print(next(g))

#! Structure
def gen_func(num):
    for i in range(num):
        yield i

for item in gen_func(1000):
    pass