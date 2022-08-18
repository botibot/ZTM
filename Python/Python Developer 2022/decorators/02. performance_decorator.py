from time import time

def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print (f'it took {t2-t1} s')
        return result
    return wrapper_func

@performance
def long_time():
    print('1')
    for i in range(100000000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i*5

long_time()
long_time2()