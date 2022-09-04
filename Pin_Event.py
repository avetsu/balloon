# import pygame
from Pin_projectiles import Pin
from random import randint


class PinEvent:

    def __init__(self, level):
        self.level = level

        self.projectiles_speed = self.level * 1
        self.projectiles_number = self.level + 10 * self.level

        self.space_projectiles = 0

        self.spawned = False

        self.x_spawns = [-66, 1355]
        self.y_spawns = [148, 251, 354, 457, 560, 663]
        self.pos = []

        self.projectiles_list = []
        self.delete_list = []

    def spawn_projectiles(self):
        for i in range(self.projectiles_number):
            rand_x = randint(0, 1)
            rand_y = randint(0, 5)
            pin = Pin((self.x_spawns[rand_x], self.y_spawns[rand_y]), self.projectiles_speed, self.level)
            if pin.direction == "gauche":
                pin.pos_x += self.space_projectiles
            else:
                pin.pos_x -= self.space_projectiles
            self.projectiles_list.append(pin)
            self.space_projectiles += 300

        self.spawned = True

    def delete(self, projectile):
        """delete the pin instance"""
        self.projectiles_list.remove(projectile)
        self.delete_list.append(projectile)
        if len(self.delete_list) > 0:
            for d in self.delete_list:
                try:
                    del projectile
                except:
                    print("error: can not delete")
                print("deleted")
                self.delete_list.remove(d)

    def update(self, screen, draw_rect):
        """update the rect and position of the pins"""
        if self.spawned:
            for pin in self.projectiles_list:
                pin.update(screen, draw_rect)
        for pin in self.projectiles_list:
            if pin.pos_x < -67 and pin.direction == "gauche" or pin.pos_x > 1356 and pin.direction == "droite":
                self.delete(pin)
