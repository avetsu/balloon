import pygame
from random import randint


class Pin(pygame.sprite.Sprite):

    def __init__(self, spawn_pos, speed, level):
        super().__init__()

        self.red_pin = pygame.image.load('sprites/pin_red.png')
        self.black_pin = pygame.image.load('sprites/pin_blue.png')
        self.blue_pin = pygame.image.load('sprites/pin_green.png')
        self.green_pin = pygame.image.load('sprites/pin_pink.png')
        self.pink_pin = pygame.image.load('sprites/pin_black.png')
        self.skin_list = []
        self.skin_list.append(self.red_pin)
        self.skin_list.append(self.black_pin)
        self.skin_list.append(self.blue_pin)
        self.skin_list.append(self.green_pin)
        self.skin_list.append(self.pink_pin)

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
        elif level >= 40:
            self.color_index = randint(0, 4)

        self.image = self.skin_list[self.color_index]

        # make an invisible square around the sprite that is used to detect collision
        self.rect = self.image.get_rect()

        self.damage = 1

        self.speed = speed + randint(5, 10)

        self.pos_x = spawn_pos[0]
        self.pos_y = spawn_pos[1]
        self.can_move = True

        if spawn_pos[0] <= -66:
            self.direction = "droite"
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.direction = "gauche"

    def movement(self):
        if self.can_move:
            if self.direction == "gauche":
                self.pos_x -= self.speed
            else:
                self.pos_x += self.speed

    def update(self, screen, draw_rect):
        if draw_rect:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 0)

        self.rect.topleft = (self.pos_x, self.pos_y)

        screen.blit(self.image, self.rect)

        self.movement()
