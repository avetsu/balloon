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

            self.image1 = pygame.image.load('Red_Balloon_1.png')
            self.image2 = pygame.image.load('Red_Balloon_2.png')
            self.image3 = pygame.image.load('Red_Balloon_3.png')
            self.image4 = pygame.image.load('Red_Balloon_4.png')
            self.image3 = pygame.image.load('Red_Balloon_3.png')
            self.image2 = pygame.image.load('Red_Balloon_2.png')
            self.animation_index = 0
            self.index = 0
            self.animation_list = []
            self.animation_list.append(self.image1)
            self.animation_list.append(self.image2)
            self.animation_list.append(self.image3)
            self.animation_list.append(self.image4)
            self.animation_list.append(self.image3)
            self.animation_list.append(self.image2)

            self.pos_x = 50
            self.pos_y = 50

        def animation(self):
            self.rect = self.animation_list[self.index].get_rect()
            if self.animation_index > 5.9:
                self.animation_index = 0
            self.animation_index += 0.08
            self.index = int(self.animation_index)
            print(int(self.animation_index))

    balloon = Balloon()

    running = True
    while running:
        quit_game()

        screen.fill((200, 200, 200))

        screen.blit(balloon.animation_list[balloon.index], (balloon.pos_x, balloon.pos_y))

        balloon.animation()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
