import pygame, math, time, os

# initializing pygame
pygame.init()

w = 1600
h = w * (9/16)

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption("EZ2OSS")

main = True
ingame = True

keys = [0,0,0,0]
keyset = [0,0,0,0]

maxframe = 60
fps = 0

while main:
    while ingame:

        fps = clock.get_fps()
        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():
            # key input detection
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    keyset[0] = 1
                if event.key == pygame.K_d:
                    keyset[1] = 1
                if event.key == pygame.K_l:
                    keyset[2] = 1
                if event.key == pygame.K_SEMICOLON:
                    keyset[3] = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    keyset[0] = 0
                if event.key == pygame.K_d:
                    keyset[1] = 0
                if event.key == pygame.K_l:
                    keyset[2] = 0
                if event.key == pygame.K_SEMICOLON:
                    keyset[3] = 0

        screen.fill((0,0,0))

        keys[0] += (keyset[0] - keys[0]) / (2*(maxframe/fps))
        keys[1] += (keyset[1] - keys[1]) / (2*(maxframe/fps))
        keys[2] += (keyset[2] - keys[2]) / (2*(maxframe/fps))
        keys[3] += (keyset[3] - keys[3]) / (2*(maxframe/fps))

        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8, -int(w/100), w/4, h+int(w/50))) # gear background
        for i in range(1, 7):
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/8 + w/32 - (w/32)*keys[0], (h/12)*9 - (h/30)*keys[0]*i, w/16 * keys[0], (h/35)/i))
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/16 + w/32 - (w/32)*keys[1], (h/12)*9 - (h/30) * keys[1] * i, w/16*keys[1], (h/35)*i))
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/32 - (w/32)*keys[2], (h/12)*9 - (h/30) * keys[2] * i, w/16*keys[2], (h/35)*i))
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/16 + w/32 - (w/32)*keys[3], (h/12)*9 - (h/30) * keys[3] * i, w/16*keys[3], (h/35)*i))
        pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, -int(w/100), w/4, h+int(w/50)), int(w/100)) # gear line

        pygame.display.flip()

