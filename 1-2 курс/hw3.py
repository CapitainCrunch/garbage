import random
class Animal:
    def __init__(self):
        self.name = "Fox"
        self.author = "Nikita"
        self.speed = 40
        self.attack = 50
        self.defense = 10
    def move (self, vicinity):
        decision = ('move',4)
        cells = [0,1,2,3,5,6,7,8]
        random.shuffle(cells)
        
        if vicinity[4][0] == "food":
                animalsInSight = False
                for q4 in cells:
                    if vicinity[q4][0] == "animal":
                        animalsInSight = True
                        break
                if animalsInSight == False:
                    if self.food > 5:
                        decision = ('move', cells[0])
                    else:
                        decision = ('eat',4)
        print decision
        return decision 
    def give_birth (self):
        animal1 = Animal ()
        newSkills = [ -1, 1, 0]
        random.shuffle(newSkills)
        animal1.speed += newSkills[0]
        animal1.attack += newSkills[1]
        animal1.defense += newSkills[2]
        return animal1
                                
    
class animalFox(Animal):
    def move(self, vicinity, cells=None):
        Animal.move (self, vicinity)
        
        for q in cells:
            if vicinity[q][0] == "animal" and vicinity[q][1].attack >= 50:
                for q0 in cells:
                    if vicinity[q0][0] == "desert" or "food":
                        decision = ('move',q0)
                break
            elif vicinity[q][0] == "animal" and vicinity[q][1].attack < 50:
                if vicinity[q][1].name != "Fox":
                    decision = ('attack',0)
                else:
                    for q2 in cells:
                        if vicinity[q2][0] == "desert" or "food":
                            decision = ('move',q2)
        return decision 
        

            


