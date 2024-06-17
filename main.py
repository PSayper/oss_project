import pygame, math, time, os, random

# initializing pygame
pygame.init()
pygame.mixer.init()

w = 1280
h = w * (9/16)

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

pygame.display.set_caption("Loading...")

image = pygame.image.load("Shining_light.png").convert()
image = pygame.transform.scale(image, (w, h))
gif_mx = []
for filename in sorted(os.listdir("Max_combo"), key=lambda x: int(x.replace("frame", "").replace(".png", ""))):
    frame_image = pygame.image.load(os.path.join("Max_combo", filename)).convert()
    frame_image = pygame.transform.scale(frame_image, (w/4 - int(w/50), w/4 - int(w/50)))
    gif_mx.append(frame_image)

gif_pf = []
for filename in sorted(os.listdir("Perfect"), key=lambda x: int(x.replace("frame", "").replace(".png", ""))):
    frame_image = pygame.image.load(os.path.join("Perfect", filename)).convert()
    frame_image = pygame.transform.scale(frame_image, (w/4 - int(w/50), w/4 - int(w/50)))
    gif_pf.append(frame_image)

frame_index = 0

pygame.mixer.music.load("Shining_light.wav")
pygame.mixer.music.play(1)

pygame.key.set_repeat(200,100)

main = True
ingame = True
ingame_real = True

keys = [0,0,0,0]
keyset = [0,0,0,0]

maxframe = 60
fps = 0
gst = time.time()
Time = time.time() - gst

# options variable
judgeline_pos = 0 # positive value sets judgement line lower, and vice versa
keybomb_magnitude = 5 # max 7, set 1 or below to turn off keybombs
note_speed = 3.0

if keybomb_magnitude > 7:
    keybomb_magnitude = 7

t1 = []
t2 = []
t3 = []
t4 = []
note_deploy_time = 0
notedeployer_1 = 0
notedeployer_2 = 0

miss = 0
combo = 0
hp_max = 1300
hp = hp_max
rate = -1

Sum = 0
count = 0
average = 0

big_font = pygame.font.SysFont("arial", int(w/23), False, False)
middle_font = pygame.font.SysFont("arial", int(w/46), False, False)
small_font = pygame.font.SysFont("arial", int(w/69), False, False)

judgement_data = [0,0,0,0]
def judge_note(n): # note judgement (BREAK, 1% ~ 100%)
    global combo, miss, last_combo, rate, hp, average, Sum, count
    
    if abs(Time - judgement_data[n - 1]) < 0.5 and abs(Time - judgement_data[n - 1]) >= 0.18:
        last_combo = combo
        miss += 1
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

        count += 1
        Sum += rate

def deploy_note(n): # function for summoning note
    ty = 0
    tst = Time + 178/60
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
        #배경 이미지 출력
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

        if Time > 60/178 * note_deploy_time: # randomly deploy note over tick
            note_deploy_time += 1
            notedeployer_1 = random.randint(1,4)
            #동치 노트 발생기
            rand = random.randint(1, 4)
            if(rand == 4):
                while(notedeployer_1 == notedeployer_2):
                    notedeployer_2 = random.randint(1, 4)
                deploy_note(notedeployer_2)

            deploy_note(notedeployer_1)
            notedeployer_2 = notedeployer_1

        Time = time.time() - gst
        fps = int(clock.get_fps()) # set fps
        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():
            #키 입력 감지
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                #ESC키 누르면 강제종료
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                #숫자키 1로 속도 감소, 2로 속도 증가
                if event.key == pygame.K_1:
                    note_speed = round(note_speed - 0.1, 1)
                    if(note_speed < 1.0):
                        note_speed = 1.0
                if event.key == pygame.K_2:
                    note_speed = round(note_speed + 0.1, 2)
                    if(note_speed > 9.9):
                        note_speed = 9.9
                #s, d, l, ; 키로 노트 처리
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
            #키를 뗐을때 처리
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
        
        #HP바 표시
        pygame.draw.rect(screen, (127,127,255), (w/2 - w/8 - w/64 - int(h/50), h*3/4 - h/2 - int(h/100), w/64 + int(h/50), h/2 + int(h/50)), int(h/100))
        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8 - w/64 - int(h/100), h*3/4 - h/2, w/64, h/2))
        pygame.draw.rect(screen, (0,255,255), (w/2 - w/8 - w/64 - int(h/100), h*3/4 - h/2*hp/hp_max, w/64, h/2*hp/hp_max))
        hp_text = middle_font.render("HP", False, (255,127,127))
        screen.blit(hp_text, (w/2 - w/8 - w/64 - int(h/100) + w/128 - hp_text.get_width()/2, h*3/4 - h/2 - h/32 - hp_text.get_height()/2))

        for tile_data in t1: # note placement
            tile_data[0] = (h/12)*9 + (Time - tile_data[1]) * 350 * note_speed * (h/900) # set note to take 2 seconds before falling
            pygame.draw.rect(screen, (255,192,0), (w/2 - w/8, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss += 1
                combo = 0
                rate = 0
                hp -= 100
                count += 1
                Sum += rate
                t1.remove(tile_data)

        for tile_data in t2: 
            tile_data[0] = (h/12)*9 + (Time - tile_data[1]) * 350 * note_speed * (h/900)
            pygame.draw.rect(screen, (192,0,255), (w/2 - w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss += 1
                combo = 0
                rate = 0
                hp -= 100
                count += 1
                Sum += rate
                t2.remove(tile_data)

        for tile_data in t3: 
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*350*note_speed*(h/900)
            pygame.draw.rect(screen, (192,0,255), (w/2, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss += 1
                combo = 0
                rate = 0
                hp -= 100
                count += 1
                Sum += rate
                t3.remove(tile_data)

        for tile_data in t4: 
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*350*note_speed*(h/900)
            pygame.draw.rect(screen, (255,192,0), (w/2 + w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss += 1
                combo = 0
                rate = 0
                hp -= 100
                count += 1
                Sum += rate
                t4.remove(tile_data)

        pygame.draw.rect(screen, (0,0,0), (w/2 - w/8, h/12*9 + judgeline_pos, w/4, h/2)) # visual judge line
        pygame.draw.rect(screen, (255,255,255), (w/2 - w/8, h/12*9 + judgeline_pos, w/4, h/2), int(h/100))

        #판정 표시
        if ingame_real:
            if(rate == -1):
                rate_text = big_font.render("", False, (255,0,0))
            elif(rate == 0):
                rate_text = big_font.render("BREAK", False, (255,0,0))
            else:
                rate_text = big_font.render("MAX "+str(rate)+"%", False, (55+rate*2,55+rate*2,255-rate*2))
            screen.blit(rate_text, (w/2 - rate_text.get_width()/2, (h/12)*8 - rate_text.get_height()/2))
        
        #콤보 표시
        if ingame_real:
            combo_text = big_font.render("COMBO", False, (255,255,0))
            screen.blit(combo_text, (w/2 - combo_text.get_width()/2, (h/12)*1 - combo_text.get_height()/2))
            combo_text = big_font.render(str(combo), False, (255,255,0))
            screen.blit(combo_text, (w/2 - combo_text.get_width()/2, (h/12)*2 - combo_text.get_height()/2))

        #속도 표시
        pygame.draw.rect(screen, (182, 44, 79), (w/2 - w/32, h - w/16 - w/64, w/16, w/16))
        pygame.draw.rect(screen, (206, 67, 102), (w/2 - w/32, h - w/16 - w/64, w/16, w/80))
        speed_text = small_font.render("SPEED", False, (255,255,255))
        screen.blit(speed_text, (w/2 - speed_text.get_width()/2, h - w/16 - w/64 - speed_text.get_height()/2 + w/160))
        speed_text = big_font.render(str(note_speed), False, (255,255,255))
        screen.blit(speed_text, (w/2 - speed_text.get_width()/2, h - w/16 - w/64 - speed_text.get_height()/2 + w/80 + w/40))

        #FPS 표시
        fps_text = middle_font.render("FPS: "+str(fps), False, (255, 255, 255))
        screen.blit(fps_text, (w - fps_text.get_width(), 0))

        #평균 정확도 표시
        if(count == 0):
            average = 0.00
        else:
            average = int(Sum * 100 / count) / float(100)
        average_text = small_font.render("RATE {:.2f}%".format(average), False, (255,255,255))
        screen.blit(average_text, (w/2 - average_text.get_width()/2, (h/12)*7 - average_text.get_height()/2))

        global end_time, clear
        #게임 종료 조건
        if(ingame_real == False):
            ingame = False
        elif(Time >= 139 or hp <= 0):
            end_time = Time
            ingame_real = False
            if(hp <= 0):
                clear = False
            else:
                clear = True
        
        #화면 갱신
        pygame.display.flip()
        clock.tick(maxframe)

    #성공 실패 여부 체크
    if(clear == True):
        #풀콤보, 퍼펙트 여부 체크
        if(average == 100):
            screen.blit(gif_pf[frame_index], (w/2 - gif_pf[frame_index].get_width()/2, h/3 - gif_pf[frame_index].get_height()/2))
        elif(miss == 0):
            screen.blit(gif_mx[frame_index], (w/2 - gif_mx[frame_index].get_width()/2, h/3 - gif_mx[frame_index].get_height()/2))
        else:
            clear_text = big_font.render("CLEAR!", False, (0,255,0))
            screen.blit(clear_text, (w/2 - clear_text.get_width()/2, h/3 - clear_text.get_height()/2))
    else:
        clear_text = big_font.render("Game Over", False, (255,0,0))
        screen.blit(clear_text, (w/2 - clear_text.get_width()/2, h/3 - clear_text.get_height()/2))
    frame_index += 1

    pygame.display.flip()
    clock.tick(33)

    Time = time.time() - gst
    if(Time - end_time > 5):
        main = False
        pygame.quit()
