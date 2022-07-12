import pygame
import random

class Projectiles(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('pin_black.png')
        self.image2 = pygame.image.load('pin_blue.png')
        self.image3 = pygame.image.load('pin_green.png')
        self.image4 = pygame.image.load('pin_pink.png')
        self.image5 = pygame.image.load('pin_red.png')
        
        self.projectiles_images = []
        self.projectiles_images.append(self.image1)
        self.projectiles_images.append(self.image2)
        self.projectiles_images.append(self.image3)
        self.projectiles_images.append(self.image4)
        self.projectiles_images.append(self.image5)

        self.color_index = 0
        
        self.rect = pygame.image.load('pin_black.png').get_rect()

        self.direction = str()
        self.projectiles_list = []

    def projectiles(self, level):

        if level < 5:
            self.color_index = 0
        elif level < 10:
            self.color_index = 1
        elif level < 20:
            self.color_index = 2
        elif level < 30:
            self.color_index = 3
        elif level < 40:
            self.color_index = 4
        elif level < 50:
            self.color_index = random.randint(0,4)

        self.image = self.projectiles_images[self.color_index]

    def position(self):
        possibility_x = [-66, 1355]
        possibility_y = [148, 251, 354, 457, 560, 663]

        rand = random.randint(0, 1)

        self.pos_x = possibility_x[rand]
        self.pos_y = possibility_y[random.randint(0, 5)]

        if rand == 0:
            self.direction = "droite"
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.direction = "gauche"


    def movement(self, pos_x, direction):
        if direction == "gauche":
            self.pos_x = pos_x - 10
        else:
            self.pos_x = pos_x + 10

    def delete(self):
        delete = []
        timer = 0

        if len(self.projectiles_list):
            for element in self.projectiles_list:
                if element[1] > 1356 or element[1] < -67:
                    delete.append(timer)
                timer += 1
        delete.sort(reverse = True)

        if len(delete):
            for lists in delete:
                if not lists < 0 :
                    del(self.projectiles_list[lists])

