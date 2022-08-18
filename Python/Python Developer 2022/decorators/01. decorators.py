#! Func calling a func

def hello(func):
    func()

def greet():
    print('Still Here')

a = hello(greet)
print('Func calling a func', a)

#Higher order function HOC
def greet(func): #! <- Accepts a function
    func()

def greet2():
    def func():
        return 5
    return func  #! <- Returns a function

#Decorators
def my_decorator(func):
    def wrap_func(*args, **kwargs):        
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func

#Decorator Pattern
def _decorator(func):
    def wrap_func(*args, **kwargs):        
        func(*args, **kwargs)
    return wrap_func    
         
@my_decorator
def hello(greeting, emoji=":("):
    print(greeting, emoji)


@my_decorator
def bye():
    print ('  bye')

hello(' hello', ':)')
#bye()