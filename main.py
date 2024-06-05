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
gst = time.time()
Time = time.time() - gst

# options variable
judgeline_pos = 0 # positive value sets judgement line lower, and vice versa
keybomb_magnitude = 5 # max 7, set 1 or below to turn off keybombs
note_speed = 1

if keybomb_magnitude > 7:
    keybomb_magnitude = 7

t1 = []
t2 = []
t3 = []
t4 = []

def deploy_note(n): # function for summoning note
    ty = 0
    tst = Time + 2
    if n == 1:
        t1.append([ty, tst])
    if n == 2:
        t2.append([ty, tst])
    if n == 3:
        t3.append([ty, tst])
    if n == 4:
        t4.append([ty, tst])
    

while main:
    while ingame:

        fps = clock.get_fps() # set fps
        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():
            # key input detection
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    keyset[0] = 1
                    deploy_note(1)
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

        keys[0] += (keyset[0] - keys[0]) / (2*(maxframe/fps)) # scroll speed management depending on fps
        keys[1] += (keyset[1] - keys[1]) / (2*(maxframe/fps))
        keys[2] += (keyset[2] - keys[2]) / (2*(maxframe/fps))
        keys[3] += (keyset[3] - keys[3]) / (2*(maxframe/fps))

        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8, -int(w/100), w/4, h+int(w/50))) # gear background
        for i in range(1, keybomb_magnitude): # key effects
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/8 + w/32 - (w/32)*keys[0], (h/12)*9 - (h/30)*keys[0]*i, w/16 * keys[0], (h/35)/i))
        for i in range(1, keybomb_magnitude):
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/16 + w/32 - (w/32)*keys[1], (h/12)*9 - (h/30)*keys[1]*i, w/16*keys[1], (h/35)/i))
        for i in range(1, keybomb_magnitude):
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/32 - (w/32)*keys[2], (h/12)*9 - (h/30)*keys[2]*i, w/16*keys[2], (h/35)/i))
        for i in range(1, keybomb_magnitude):
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/16 + w/32 - (w/32)*keys[3], (h/12)*9 - (h/30)*keys[3]*i, w/16*keys[3], (h/35)/i))
        pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, -int(w/100), w/4, h+int(w/50)), int(w/100)) # gear line

        for tile_data in t1: # note placement
            tile_data[0] = h/12*9 + (Time - tile_data[1])*350*note_speed*(h/900) # set note to take 2 seconds before falling
            pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                t1.remove(tile_data)
        for tile_data in t2: 
            tile_data[0] = h/12*9 + (Time - tile_data[1])*350*note_speed*(h/900)
            pygame.draw.rect(screen, (255,255,255), (w/2 - w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                t2.remove(tile_data)
        for tile_data in t3: 
            tile_data[0] = h/12*9 + (Time - tile_data[1])*350*note_speed*(h/900)
            pygame.draw.rect(screen, (255,255,255), (w/2, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                t3.remove(tile_data)
        for tile_data in t4: 
            tile_data[0] = h/12*9 + (Time - tile_data[1])*350*note_speed*(h/900)
            pygame.draw.rect(screen, (255,255,255), (w/2 + w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                t4.remove(tile_data)

        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8, h/12*9 + judgeline_pos, w/4, h/2)) # visual judge line
        pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, h/12*9 + judgeline_pos, w/4, h/2), int(h/100))



        pygame.display.flip()

