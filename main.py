import pygame
import Balloon
import Projectiles
import Gameplay

pygame.init()

pygame.display.set_caption("Balloon")
screen = pygame.display.set_mode((1355, 865))
clock = pygame.time.Clock()

def quit_game():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

balloon = Balloon.Balloon()
gameplay = Gameplay.Gameplay()
level = gameplay.level
projectiles = Projectiles.Projectiles()
for x in range(1):
    projectiles.projectiles(level)
    projectiles.position()
    projectiles.projectiles_list.append([projectiles.image, projectiles.pos_x, projectiles.pos_y, projectiles.direction])

running = True

while running:
    quit_game()

    screen.fill((200, 200, 200))

    if gameplay.lives > 0:
        screen.blit(balloon.animation_list[balloon.index], (balloon.pos[0], balloon.pos[1]))
    else:
        balloon.pos = [False, False]

    for proj in projectiles.projectiles_list:
        screen.blit(proj[0], (proj[1], proj[2]))
        projectiles.movement(proj[1], proj[3])
        proj[1] = projectiles.pos_x

    balloon.movement()
    balloon.animation()
    projectiles.delete()
    gameplay.life(balloon.pos, projectiles.projectiles_list)
    gameplay.lvlf(projectiles.projectiles_list)
    clock.tick(45)

    pygame.display.flip()
print(gameplay.level)
print(gameplay.lives)
print(projectiles.projectiles_list)
pygame.quit()
