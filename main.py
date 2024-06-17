import pygame, math, time, os, random

# initializing pygame
pygame.init()

w = 1600
h = w * (9/16)

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption("EZ2MAX OSS")
pygame.key.set_repeat(200,100)
image = pygame.image.load("Shining_light.png").convert()
image = pygame.transform.scale(image, (w, h))

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
note_speed = 2.0

if keybomb_magnitude > 7:
    keybomb_magnitude = 7

t1 = []
t2 = []
t3 = []
t4 = []
note_deploy_time = 0
notedeployer_1 = 0
notedeployer_2 = 0

miss_anim = 0
combo = 0
hp_max = 1300
hp = hp_max
rate = -1

big_font = pygame.font.SysFont("arial", int(w/23), False, False)
middle_font = pygame.font.SysFont("arial", int(w/46), False, False)
small_font = pygame.font.SysFont("arial", int(w/69), False, False)

judgement_data = [0,0,0,0]
def judge_note(n): # note judgement (KOOL, COOL, GOOD, MISS, FAIL)
    global combo, miss_anim, last_combo, rate, hp
    
    if abs(Time - judgement_data[n - 1]) < 0.5 and abs(Time - judgement_data[n - 1]) >= 0.18:
        last_combo = combo
        miss_anim = 1
        combo = 0
        rate = 0
        hp -= 100
    if abs(Time - judgement_data[n - 1]) <= 0.18 and abs(Time - judgement_data[n - 1]) > 0.168:
        combo += 1
        rate = 1
        hp += 0
    if abs(Time - judgement_data[n - 1]) <= 0.168 and abs(Time - judgement_data[n - 1]) > 0.159:
        combo += 1
        rate = 10
        hp += 1
    if abs(Time - judgement_data[n - 1]) <= 0.159 and abs(Time - judgement_data[n - 1]) > 0.147:
        combo += 1
        rate = 20
        hp += 2
    if abs(Time - judgement_data[n - 1]) <= 0.147 and abs(Time - judgement_data[n - 1]) > 0.138:
        combo += 1
        rate = 30
        hp += 3
    if abs(Time - judgement_data[n - 1]) <= 0.138 and abs(Time - judgement_data[n - 1]) > 0.129:
        combo += 1
        rate = 40
        hp += 4
    if abs(Time - judgement_data[n - 1]) <= 0.129 and abs(Time - judgement_data[n - 1]) > 0.12:
        combo += 1
        rate = 50
        hp += 5
    if abs(Time - judgement_data[n - 1]) <= 0.12 and abs(Time - judgement_data[n - 1]) > 0.099:
        combo += 1
        rate = 60
        hp += 6
    if abs(Time - judgement_data[n - 1]) <= 0.099 and abs(Time - judgement_data[n - 1]) > 0.078:
        combo += 1
        rate = 70
        hp += 7
    if abs(Time - judgement_data[n - 1]) <= 0.078 and abs(Time - judgement_data[n - 1]) > 0.06:
        combo += 1
        rate = 80
        hp += 8
    if abs(Time - judgement_data[n - 1]) <= 0.06 and abs(Time - judgement_data[n - 1]) > 0.042:
        combo += 1
        rate = 90
        hp += 9
    if abs(Time - judgement_data[n - 1]) <= 0.042 and abs(Time - judgement_data[n - 1]) >= 0:
        combo += 1
        rate = 100
        hp += 10

    if(hp > hp_max):
        hp = hp_max


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
        screen.blit(image, (0, 0))

        pygame.display.set_caption("EZ2MAX OSS")
        if len(t1) > 0:
            judgement_data[0] = t1[0][1]
        if len(t2) > 0:
            judgement_data[1] = t2[0][1]
        if len(t3) > 0:
            judgement_data[2] = t3[0][1]
        if len(t4) > 0:
            judgement_data[3] = t4[0][1]

        if Time > 0.2 * note_deploy_time: # randomly deploy note over tick
            note_deploy_time += 1
            while notedeployer_1 == notedeployer_2:
                notedeployer_1 = random.randint(1,4)
            deploy_note(notedeployer_1)
            notedeployer_2 = notedeployer_1

        Time = time.time() - gst
        fps = clock.get_fps() # set fps
        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():
            # key input detection
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_1:
                    note_speed = round(note_speed - 0.1, 1)
                if event.key == pygame.K_2:
                    note_speed = round(note_speed + 0.1, 2)
                if event.key == pygame.K_s:
                    keyset[0] = 1
                    if len(t1) > 0:
                        if(abs(Time - t1[0][1]) < 0.5):
                            judge_note(1)
                            del t1[0]
                    
                if event.key == pygame.K_d:
                    keyset[1] = 1
                    if len(t2) > 0:
                        if(abs(Time - t2[0][1]) < 0.5):
                            judge_note(2)
                            del t2[0]
                    
                if event.key == pygame.K_l:
                    keyset[2] = 1
                    if len(t3) > 0:
                        if(abs(Time - t3[0][1]) < 0.5):
                            judge_note(3)
                            del t3[0]
                    
                if event.key == pygame.K_SEMICOLON:
                    keyset[3] = 1
                    if len(t4) > 0:
                        if(abs(Time - t4[0][1]) < 0.5):
                            judge_note(4)
                            del t4[0]
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    keyset[0] = 0
                if event.key == pygame.K_d:
                    keyset[1] = 0
                if event.key == pygame.K_l:
                    keyset[2] = 0
                if event.key == pygame.K_SEMICOLON:
                    keyset[3] = 0

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
        pygame.draw.rect(screen, (127,127,255), (w/2 - w/8 - w/64 - int(h/50), h*3/4 - h/2 - int(h/100), w/64 + int(h/50), h/2 + int(h/50)), int(h/100))
        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8 - w/64 - int(h/100), h*3/4 - h/2, w/64, h/2))
        pygame.draw.rect(screen, (0,255,255), (w/2 - w/8 - w/64 - int(h/100), h*3/4 - h/2*hp/hp_max, w/64, h/2*hp/hp_max))
        hp_text = middle_font.render("HP", False, (255,127,127))
        screen.blit(hp_text, (w/2 - w/8 - w/64 - int(h/100) + w/128 - hp_text.get_width()/2, h*3/4 - h/2 - h/32 - hp_text.get_height()/2))

        for tile_data in t1: # note placement
            tile_data[0] = (h/12)*9 + (Time - tile_data[1]) * 350 * note_speed * (h/900) # set note to take 2 seconds before falling
            pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                rate = 0
                hp -= 100
                t1.remove(tile_data)

        for tile_data in t2: 
            tile_data[0] = (h/12)*9 + (Time - tile_data[1]) * 350 * note_speed * (h/900)
            pygame.draw.rect(screen, (255,255,255), (w/2 - w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                rate = 0
                hp -= 100
                t2.remove(tile_data)

        for tile_data in t3: 
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*350*note_speed*(h/900)
            pygame.draw.rect(screen, (255,255,255), (w/2, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                rate = 0
                hp -= 100
                t3.remove(tile_data)

        for tile_data in t4: 
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*350*note_speed*(h/900)
            pygame.draw.rect(screen, (255,255,255), (w/2 + w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                rate = 0
                hp -= 100
                t4.remove(tile_data)

        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8, h/12*9 + judgeline_pos, w/4, h/2)) # visual judge line
        pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, h/12*9 + judgeline_pos, w/4, h/2), int(h/100))

        if(rate == -1):
            rate_text = big_font.render("", False, (255,0,0))
        elif(rate == 0):
            rate_text = big_font.render("BREAK", False, (255,0,0))
        else:
            rate_text = big_font.render("MAX "+str(rate)+"%", False, (55+rate*2,55+rate*2,255-rate*2))
        screen.blit(rate_text, (w/2 - rate_text.get_width()/2, (h/12)*8 - rate_text.get_height()/2))
        
        combo_text = big_font.render("COMBO", False, (255,255,0))
        screen.blit(combo_text, (w/2 - combo_text.get_width()/2, (h/12)*1 - combo_text.get_height()/2))
        combo_text = big_font.render(str(combo), False, (255,255,0))
        screen.blit(combo_text, (w/2 - combo_text.get_width()/2, (h/12)*2 - combo_text.get_height()/2))

        
        pygame.draw.rect(screen, (182, 44, 79), (w/2 - w/32, h - w/16 - w/64, w/16, w/16))
        pygame.draw.rect(screen, (206, 67, 102), (w/2 - w/32, h - w/16 - w/64, w/16, w/80))
        speed_text = small_font.render("SPEED", False, (255,255,255))
        screen.blit(speed_text, (w/2 - speed_text.get_width()/2, h - w/16 - w/64 - speed_text.get_height()/2 + w/160))
        speed_text = big_font.render(str(note_speed), False, (255,255,255))
        screen.blit(speed_text, (w/2 - speed_text.get_width()/2, h - w/16 - w/64 - speed_text.get_height()/2 + w/80 + w/40))

        if(combo >= 50 or hp <= 0):
            global end_time, clear
            end_time = Time
            ingame = False
            if(hp <= 0):
                clear = False
            else:
                clear = True

        pygame.display.flip()
        clock.tick(maxframe)

    if(clear == True):
        clear_text = big_font.render("CONGRATULATIONS! YOU CLEARED THE GAME!", False, (0,255,0))
    else:
        clear_text = big_font.render("Game Over", False, (255,0,0))
    screen.blit(clear_text, (w/2 - clear_text.get_width()/2, (h/12)*6 - clear_text.get_height()/2))
    pygame.display.flip()
    clock.tick(maxframe)
    Time = time.time() - gst
    if(Time - end_time > 5):
        main = False

