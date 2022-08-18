# Create an @authenticated decorator that only allows the function to run if user1 has
#  'valid' set to True:

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrap_fn(*args, **kwargs):
        if args[0]['valid'] == True:
            fn(*args, **kwargs)
        else: print('User not authenticated')
    return wrap_fn

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)