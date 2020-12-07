import random
from app.enemy import *

class Game(object):

    def __init__(self, turn, dmg):
        self.turn = 0
        self.level = 0
        self.list_enemies = []
        self.list_characters = []

    def generate_enemy(self):
        l = [0, 1, 2, 3]
        for x in range(4):
            n = random.randint(1,4))
            if (n == 1):
                enemy = PartialExam()
            elif (n == 2):            
                enemy = FinalExam()                
            elif (n == 3):
                enemy = TheoreticalClass()
            elif (n == 4):
                enemy = Teacher()
        return enemy
    
    def next_turn(self):
        self.turn = self.turn + 1
        enemie1 = Enemy()
        self.list_enemies.append(enemie1)
        enemie2 = Enemy()
        self.list_enemies.append(enemie2)        
        enemie3 = Enemy()
        self.list_enemies.append(enemie3)        
        enemie4 = Enemy()
        self.list_enemies.append(enemie4)        
        return self.turn

    def next_level(self):
        self.level = self.level + 1
        return self.level

    
    
