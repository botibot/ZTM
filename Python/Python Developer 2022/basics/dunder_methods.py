class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5

    def __del__(self):
        return print('deleted!')
    
    def __getitem__(self, i):
        return self.my_dict[i]
    
    def __call__(self):
        return print('yesss??')

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
action_figure()
print(action_figure['name'])
del(action_figure)