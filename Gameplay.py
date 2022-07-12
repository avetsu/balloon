import pygame
import Projectiles

projectiles = Projectiles.Projectiles()

class Gameplay():

    def __init__(self):
        self.level = 30
        self.level_finished = False
        self.balloon_entity_position = [False, False, False, False]
        self.bep = self.balloon_entity_position
        self.lives = 1

    def gameplay(self):
        pass

    def life(self, bpos, ppos):
        self.bep[0] = bpos[0]
        self.bep[1] = bpos[1]
        self.bep[2] = bpos[0]+75
        self.bep[3] = bpos[1]+190

        for data in ppos:
            if self.bep[0] <= data[1] <= self.bep[2] and self.bep[1] <= data[2] <= self.bep[3]:
                self.lives -= 1
    
    def lvlf(self, plist):
        if self.lives > 0:
            if not len(plist):
                self.level_finished = True
            
            if self.level_finished:
                self.level += 1
                self.level_finished = False
                