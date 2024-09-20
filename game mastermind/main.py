FLAGNUM = 14
import pygame, sys, random
from pygame.locals import *
import time

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# tạo window
pygame.display.set_caption('Game master mind - LogN - mssv:24520019')
pygame.init()
DISPLAYSURF = pygame.display.set_mode((700, 500))
# vẽ ô
DISPLAYSURF.fill(BLACK)
for i in range(1, 10) :
    pygame.draw.line(DISPLAYSURF, BLACK, (0, i*50), (500, i*50), 1)
    pygame.draw.line(DISPLAYSURF, BLACK, (i*50, 0), (i*50, 500), 1)
pygame.draw.line(DISPLAYSURF, BLACK, (500, 0), (500, 500), 3)
pygame.display.update()

a = [[0 for j in range(10)] for i in range(10)] #a[0..9][0..9]

for z in range(FLAGNUM) :
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    while a[i][j] == 'X' :
        i = random.randint(0, 9)
        j = random.randint(0, 9)
    a[i][j] = 'X'
    #print(i, j)

def Print(St, Size, Font, Bold, Color, x, y) :
    # Ghi ra game nội dung St, kích thước Size,
    # phông chữ Font, độ dày nét Bold, màu Color, tại vị trí (x, y) 
    font = pygame.font.SysFont(Font, Size, Bold)
    commentSuface = font.render(St, True, Color)
    DISPLAYSURF.blit(commentSuface, (x, y))
    pygame.display.update()

# vẽ flags
Print('Flags:', 50, 'consolas', 1, BLUE, 510, 10)
Print(str(FLAGNUM), 50, 'consolas', 1, BLUE, 510, 60)
# vẽ thời gian
Print('Time:', 50, 'consolas', 1, BLUE, 510, 210)
Print('00:00', 50, 'consolas', 1, BLUE, 510, 260)
# vẽ count
Print('Count:', 50, 'consolas', 1, BLUE, 510, 400)
Print(str(100-FLAGNUM), 50, 'consolas', 1, BLUE, 510, 460)

def dembom(x, y) :
    d = 0
    if x > 0 and y > 0 and a[x-1][y-1] == 'X' : d += 1
    if x > 0 and a[x-1][y] == 'X' : d += 1
    if x > 0 and y < 9 and a[x-1][y+1] == 'X' : d += 1
    if y > 0 and a[x][y-1] == 'X' : d += 1
    if y < 9 and a[x][y+1] == 'X' : d += 1
    if x < 9 and y > 0 and a[x+1][y-1] == 'X' : d += 1
    if x < 9 and a[x+1][y] == 'X' : d += 1
    if x < 9 and y < 9 and a[x+1][y+1] == 'X' : d += 1
    return d

for i in range(10) :
    for j in range(10) :
        if a[i][j] == 0 :
            a[i][j] = dembom(i, j)

def inmang(xx) :
    # for i in range(10) :
    #     for j in range(10) :
    #         print(a[j][i], end = ' ')
    #     print()
    return

inmang(a)

xet = [[0 for i in range(10)] for i in range(10)]

def show(x, y) : # hiển thị số cho ô (x, y)
    font = pygame.font.SysFont('consolas', 60, 2)
    if a[x][y] == 'X' :
        commentSuface = font.render(str(a[x][y]), True, RED)
    else :
        commentSuface = font.render(str(a[x][y]), True, BLACK)
    commentSize = commentSuface.get_size()
    DISPLAYSURF.blit(commentSuface, (x*50+5, y*50))
    pygame.display.update()

demflag = FLAGNUM
demchon = 100-FLAGNUM

def showflag() :
    pygame.draw.rect(DISPLAYSURF, WHITE, (510, 60, 100, 60))
    Print(str(demflag), 50, 'consolas', 1, BLUE, 510, 60)
    pygame.draw.rect(DISPLAYSURF, WHITE, (510, 460, 100, 60))
    Print(str(demchon), 50, 'consolas', 1, BLUE, 510, 460)
    pygame.display.update()

def show2(x, y) :
    # vẽ cờ *
    font = pygame.font.SysFont('consolas', 60, 2)
    commentSuface = font.render('*', True, BLACK)
    commentSize = commentSuface.get_size()
    DISPLAYSURF.blit(commentSuface, (x*50+5, y*50+8))
    pygame.display.update()

firsttime = 0
def click(x, y) :
    global firsttime, a
    firsttime += 1
    if xet[x][y] == 2 :
        return

    if xet[x][y] == 1 :
        erase(x, y)
        global demflag
        demflag -= 1
        showflag()

    global demchon
    demchon -= 1
    xet[x][y] = 2
    show(x, y)
    showflag()

    if a[x][y] == 0 :
        if x > 0 and y > 0: click(x-1, y-1)
        if x > 0 : click(x-1, y)
        if x > 0 and y < 9: click(x-1, y+1)
        if y > 0 : click(x, y-1)
        if y < 9 : click(x, y+1)
        if x < 9 and y > 0 : click(x+1, y-1)
        if x < 9 : click(x+1, y)
        if x < 9 and y < 9 : click(x+1, y+1)

    if a[x][y] == 'X' :
        if firsttime == 1:
            a = [[0 for j in range(10)] for i in range(10)]
            for z in range(FLAGNUM) :
                i = random.randint(0, 9)
                j = random.randint(0, 9)
                while a[i][j] == 'X' :
                    i = random.randint(0, 9)
                    j = random.randint(0, 9)
                a[i][j] = 'X'
            click(x, y)
            return

        Print('YOU LOSE !!!', 100, 'consolas', 2, RED, 50, 200)
        pygame.display.update()
        time.sleep(5)
        exit(0)

    if demchon == 0:
        Print('YOU WIN !!!', 100, 'consolas', 2, RED, 50, 200)
        pygame.display.update()
        time.sleep(5)
        exit(0)

def erase(x, y) : # xóa ô (x, y)
    xet[x][y] = 0
    pygame.draw.rect(DISPLAYSURF, WHITE, (x*50+1, y*50+1, 49, 49))
    pygame.display.update()

def flag(x, y) :
    if xet[x][y] == 2 :
        return
    global demflag
    if xet[x][y] == 1 :
        erase(x, y)
        demflag += 1
        showflag()
        return
    if demflag > 0 :
        xet[x][y] = 1
        demflag -= 1
        show2(x, y)
        showflag()

def main() :
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit() 
                exit(0) 
            if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed()[0] :
                    vt = pygame.mouse.get_pos()
                    click(vt[0] // 50, vt[1] // 50)
                if pygame.mouse.get_pressed()[2] :
                    vt = pygame.mouse.get_pos()
                    flag(vt[0] // 50, vt[1] // 50)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    pygame.quit() 
                    exit(0)
        #print(time.time()%10)
        
if __name__ == '__main__' :
    main()