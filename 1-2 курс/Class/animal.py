#создаем класс животного
import random
class Dondo:
    def __init__(self):
        self.name = 'Dondo'
        self.author = 'Bogdan'
        self.speed = 20
        self.attack = 20
        self.defense = 60

    def move(self, vicinity):          
        eatMove = self.eatMove(vicinity)       
        attack = self.attackEnemy(vicinity)
        back = self.back(vicinity)
        sMove = self.sMove(vicinity)
        if eatMove != None:
            return eatMove
        if sMove != None:
            return sMove
        if attack != None:
            return attack
        else: 
            return back

    def sMove(self, vicinity):
        for i in xrange(9):
            if vicinity[i][0] == 'fence':
                return ('move', 8 - i)
            else:
                way = random.choice(range(9))
                if vicinity[way][0] == 'desert':
                    return ('move', way) 

    def attackEnemy(self, vicinity):          
        for i, element in enumerate(vicinity):
            lvl = 60
            if element[0] == 'animal':
                supp = vicinity[i][1].attack
                if supp < lvl:
                    return ('attack', i)
            else:
                pass
                    
    def eatMove(self, vicinity):
            for i in xrange(9):
                if vicinity[i][0] == 'food' and i == 4:
                    return ('eat', 4)
                elif vicinity[i][0] == 'food':
                    return ('move', i)
            else:
                if vicinity[i][0] == 'desert':
                    return ('move', i)

    def back(self, vicinity):
        for i, element in enumerate(vicinity):
            if element[0] == 'animal' and (vicinity[i][1].attack > 60):
                if i in xrange(0, 3):
                    return ('move', 7)
                if i in xrange(6, 9):
                    return ('move', 1)
                else:
                    return ('move', 4)

    def give_birth(self):

        dondo = Dondo()
        dondo.attack = self.attack + 1
        dondo.defense = self.defense - 1
        dondo.speed = self.speed

        return dondo
