import pygame, re, math
import pygame.gfxdraw
pygame.init()

def draw_background():
    global radius
    if list(radius.values())[-1] == 40:
        if 'g' in list(radius.keys())[-1]:
            number = int((re.findall('[0-9]+', list(radius.keys())[-1]))[0])
            radius[f'p{number}'] = 1
        elif 'p' in list(radius.keys())[-1]:
            number = int((re.findall('[0-9]+', list(radius.keys())[-1]))[0]) + 1
            if number > 8: number = 1
            radius[f'g{number}'] = 1
    # draw circle
    for i in radius:
        if 'p' in i:
            pygame.gfxdraw.filled_circle(screen, mousex, mousey, radius[i], colour)
            pygame.gfxdraw.aacircle(screen, mousex, mousey, radius[i], colour) # use aacircle to anti-aliasing
        else:
            pygame.gfxdraw.filled_circle(screen, mousex, mousey, radius[i], colour2)
            pygame.gfxdraw.aacircle(screen, mousex, mousey, radius[i], colour2)
    # update radius
    poplist=[]
    for i in radius:
        radius[i] += 1
        if radius[i] >= 566:
            poplist.append(i)
    if len(poplist) != 0: radius.pop(poplist[0])

def draw_lines():
    pygame.draw.line(screen, (125, 38, 144), (0, 133), (400, 133), width=6)
    pygame.draw.line(screen, (125, 38, 144), (0, 266), (400, 266), width=6)
    pygame.draw.line(screen, (125, 38, 144), (133, 0), (133, 400), width=6)
    pygame.draw.line(screen, (125, 38, 144), (266, 0), (266, 400), width=6)

def draw_icons():
    for value in list(slots.values()):
        if value[0] == 'circle':
            screen.blit(circle, value[1])
        elif value[0] == 'cross':
            screen.blit(cross, value[1])

def game_logic():
    global winner
    if 0 < mousex < 133 and 0 < mousey < 133 and '1' not in slots:
        slots['1'] = (turn,(16,16))
    elif 133 < mousex < 266 and 0 < mousey < 133 and '2' not in slots:
        slots['2'] = (turn,(149,16))
    elif 266 < mousex < 400 and 0 < mousey < 133 and '3' not in slots:
        slots['3'] = (turn,(282,16))
    elif 0 < mousex < 133 and 133 < mousey < 266 and '4' not in slots:
        slots['4'] = (turn,(16,149))
    elif 133 < mousex < 266 and 133 < mousey < 266 and '5' not in slots:
        slots['5'] = (turn,(149,149))
    elif 266 < mousex < 400 and 133 < mousey < 266 and '6' not in slots:
        slots['6'] = (turn,(282,149))
    elif 0 < mousex < 133 and 266 < mousey < 400 and '7' not in slots:
        slots['7'] = (turn,(16,282))
    elif 133 < mousex < 266 and 266 < mousey < 400 and '8' not in slots:
        slots['8'] = (turn,(149,282))
    elif 266 < mousex < 400 and 266 < mousey < 400 and '9' not in slots:
        slots['9'] = (turn,(282,282))
    cross=[]
    circle=[]
    for key in slots:
        if slots[key][0] == 'circle':
            circle.append(int(key))
        elif slots[key][0] == 'cross':
            cross.append(int(key))
    print(cross, circle)

    win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in win:
        if set(i).issubset(set(cross)): winner = 'cross'
        elif set(i).issubset(set(circle)): winner = 'circle'
    if winner != None: print(f'The winner is {winner}')

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
radius = {}
slots = {}
radius['g1'] = 1
colour = (255, 160, 76)
colour2 = (255, 232, 76)
mousex=200
mousey=200
cross = pygame.image.load('cross.png').convert_alpha()
circle = pygame.image.load('circle.png').convert_alpha()
player = ('circle', 'cross')
round = 0
winner = None
while True:
    left, scroll, right = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, scroll, right = pygame.mouse.get_pressed()
            if left:
                mousex = pygame.mouse.get_pos()[0]
                mousey = pygame.mouse.get_pos()[1]

                if round % 2 == 0:
                    turn = 'circle'
                    game_logic()
                else: 
                    turn = 'cross'
                    game_logic()
                round += 1
    if right:
        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]
    draw_background()
    draw_lines()
    draw_icons()
    pygame.display.update()
    clock.tick(60)
