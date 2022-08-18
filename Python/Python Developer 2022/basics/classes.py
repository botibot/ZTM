# Object Oriented Program OOP

class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')
        return ('done')


player1 = PlayerCharacter('Cindy')
player2 = PlayerCharacter('Jorge')

print(player1.name, player2.name)
# ame220315053878
