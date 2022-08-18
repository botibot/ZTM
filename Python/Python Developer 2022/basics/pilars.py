# OOP Pilars
#
# Encapsulation: Paking up!
# Abstraction: Giving acces only to what it's necesary // _ means private, do not touch
# Inheritance:

class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        User.attack(self)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows, arrows left :{self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

print(wizard1.sign_in())
wizard1.attack()
archer1.attack()
wizard1.sign_in()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

# Polymorphism: Many Forms
