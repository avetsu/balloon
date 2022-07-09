import pygame

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption("Simulation")
    screen = pygame.display.set_mode((960, 540))
    clock = pygame.time.Clock()

    def quit_game():
        global running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    class Balloon(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('Red_Ballon_1.png')
            self.rect = self.image.get_rect()
            self.pos_x = 50
            self.pos_y = 50

    balloon = Balloon()

    running = True
    while running:
        quit_game()

        screen.fill((200, 200, 200))

        screen.blit(balloon.image, (Balloon.pos_x, Balloon.pos_y))
        
        clock.tick(1000)

        pygame.display.flip()

    pygame.quit()
