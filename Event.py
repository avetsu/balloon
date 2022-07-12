import pygame
import random


class Event:

    def __init__(self):
        self.level = 1
        self.event_finished = False
        self.random_selector = None
        self.current_event = None
        self.event = None
        self.event_start = True

    def level_calculation(self):
        if self.event_finished:
            self.level += 1
            self.event_finished = False

    def event_selector(self, event_list, screen, draw_rect):
        if self.event_start:
            self.random_selector = random.randint(0, len(event_list)-1)
            self.event = event_list[self.random_selector]
            self.current_event = self.event(self.level)
            self.current_event.spawn_projectiles()
            self.event_start = False

        self.current_event.update(screen, draw_rect)

        if len(self.current_event.projectiles_list) == 0:
            self.event_finished = True
            self.event_start = True
            print("level " + str(self.level) + " passed")



