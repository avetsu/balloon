import pygame
import sys
from Balloon import Balloon
from Event import Event
from Pin_Event import PinEvent


class Game:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Balloon")
        self.screen = pygame.display.set_mode((1355, 865))
        self.clock = pygame.time.Clock()

        self.balloon = Balloon()

        self.event = Event()

        self.event_list = []
        self.event_list.append(PinEvent)

        self.running = True

        self.draw_rect = False

    def pygame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.draw_rect = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    self.draw_rect = False

    def game_loop(self):
        while self.running:
            self.pygame_events()

            self.screen.fill((0, 220, 255))
            
            self.event.level_calculation()
            self.event.event_selector(self.event_list, self.screen, self.draw_rect)

            self.balloon.update(self.screen, self.draw_rect, self.event.current_event)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
