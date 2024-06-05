import pygame, math, time, os

pygame.init()

w = 1600
h = w * (9/16)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("")

main = True
ingame = True

while main:
    while ingame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0,0,0))

        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8, -int(w/100), w/4, h+int(w/50))) # gear background
        pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, -int(w/100), w/4, h+int(w/50)), int(w/100)) # gear line

        pygame.display.flip()

