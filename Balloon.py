import time

import pygame


class Balloon(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # loading and appending to animation_list all the images for the animation of Balloon
        self.image1 = pygame.image.load('sprites/Red_Balloon_1.png')
        self.image2 = pygame.image.load('sprites/Red_Balloon_2.png')
        self.image3 = pygame.image.load('sprites/Red_Balloon_3.png')
        self.image4 = pygame.image.load('sprites/Red_Balloon_4.png')
        self.animation_list = []
        self.animation_list.append(self.image1)
        self.animation_list.append(self.image2)
        self.animation_list.append(self.image3)
        self.animation_list.append(self.image4)
        self.animation_list.append(self.image3)
        self.animation_list.append(self.image2)

        # make an invisible square around the sprite that is used to detect collision
        self.rect = self.image2.get_rect()
        # make the height of the balloon smaller so the rope of the balloon is not in the rect
        self.rect.h -= 87

        # index that scroll through the animation_list animation_index is a float and index is the int value of
        # animation_index
        self.animation_index = 0
        self.index = 0

        self.pos_x = 40
        self.pos_y = 120
        self.key_pressed = False
        self.key_blocked = []
        self.key_blocked.append(False)
        self.key_blocked.append(False)
        self.key_blocked.append(False)
        self.key_blocked.append(False)

        self.max_health = 10
        self.health = 10
        self.damage_timer = 0

    def animation(self):
        """
        Animate the sprite using an index that scroll through a list of images
        """
        if self.animation_index > 5.9:
            self.animation_index = 0
        self.animation_index += 0.08
        self.index = int(self.animation_index)

    def movement(self):
        """
        Detect the inputs for the movement of the Balloon
        """
        if self.key_blocked[0] and not pygame.key.get_pressed()[pygame.K_LEFT]:
            self.key_blocked[0] = False

        if self.key_blocked[1] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.key_blocked[1] = False

        if self.key_blocked[2] and not pygame.key.get_pressed()[pygame.K_UP]:
            self.key_blocked[2] = False

        if self.key_blocked[3] and not pygame.key.get_pressed()[pygame.K_DOWN]:
            self.key_blocked[3] = False

        if pygame.key.get_pressed()[pygame.K_LEFT] and self.pos_x > 40 and not self.key_blocked[0]:
            self.pos_x -= 75
            self.key_blocked[0] = True

        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.pos_x < 1240 and not self.key_blocked[1]:
            self.pos_x += 75
            self.key_blocked[1] = True

        if pygame.key.get_pressed()[pygame.K_UP] and self.pos_y > 120 and not self.key_blocked[2]:
            self.pos_y -= 103
            self.key_blocked[2] = True

        if pygame.key.get_pressed()[pygame.K_DOWN] and self.pos_y < 635 and not self.key_blocked[3]:
            self.pos_y += 103
            self.key_blocked[3] = True

    def collision(self, event):
        self.damage_timer -= 1
        for projectile in event.projectiles_list:
            if self.rect.colliderect(projectile) and self.damage_timer <= 0:
                self.health -= projectile.damage
                self.damage_timer = 10
                event.delete(projectile)
                print("collision" + str(self.health))

    def death(self):
        if self.health == 0:
            print(" ---------- Game Over ---------- ")

    def update(self, screen, draw_rect, projectile_rect):
        # make the rect follow the sprite by giving him the coordinate of the sprite
        self.rect.topleft = (self.pos_x, self.pos_y)

        if draw_rect:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 0)

        screen.blit(self.animation_list[self.index], self.rect)

        self.animation()
        self.movement()
        self.collision(projectile_rect)
        self.death()
