import pygame

class Balloon(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('Red_Balloon_1.png')
        self.image2 = pygame.image.load('Red_Balloon_2.png')
        self.image3 = pygame.image.load('Red_Balloon_3.png')
        self.image4 = pygame.image.load('Red_Balloon_4.png')
        self.animation_index = 0
        self.index = 0
        self.animation_list = []
        self.animation_list.append(self.image1)
        self.animation_list.append(self.image2)
        self.animation_list.append(self.image3)
        self.animation_list.append(self.image4)
        self.animation_list.append(self.image3)
        self.animation_list.append(self.image2)

        self.pos = [False, False]

        self.pos[0] = 40
        self.pos[1] = 120
        self.key_pressed = False
        self.key_blocked = []
        self.key_blocked.append(False)
        self.key_blocked.append(False)
        self.key_blocked.append(False)
        self.key_blocked.append(False)
        self.rect = pygame.image.load('Red_Balloon_1.png').get_rect()

    def animation(self):
        if self.animation_index == 10:
            self.animation_index = 0
            self.index += 1
            if self.index == 6:
                self.index = 0
        
        self.animation_index += 1

    def movement(self):
        if self.key_blocked[0] == True and pygame.key.get_pressed()[pygame.K_LEFT] == False:
            self.key_blocked[0] = False

        if self.key_blocked[1] == True and pygame.key.get_pressed()[pygame.K_RIGHT] == False: 
            self.key_blocked[1] = False

        if self.key_blocked[2] == True and pygame.key.get_pressed()[pygame.K_UP] == False:
            self.key_blocked[2] = False
        
        if self.key_blocked[3] == True and pygame.key.get_pressed()[pygame.K_DOWN] == False:
            self.key_blocked[3] = False
        
        if pygame.key.get_pressed()[pygame.K_LEFT] == True and self.pos[0] > 40 and self.key_blocked[0] == False:
            self.pos[0] -= 75
            self.key_blocked[0] = True

        if pygame.key.get_pressed()[pygame.K_RIGHT] == True and self.pos[0] < 1240 and self.key_blocked[1] == False:
            self.pos[0] += 75
            self.key_blocked[1] = True

        if pygame.key.get_pressed()[pygame.K_UP] == True and self.pos[1] > 120 and self.key_blocked[2] == False:
            self.pos[1] -= 103
            self.key_blocked[2] = True
            
        if pygame.key.get_pressed()[pygame.K_DOWN] == True and self.pos[1] < 635  and self.key_blocked[3] == False:
            self.pos[1] += 103
            self.key_blocked[3] = True
