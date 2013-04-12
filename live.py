import pygame, random
from copy import deepcopy
from time import sleep
n = 80
dot_width = 10
width = dot_width * n
dotcolor = (200, 200, 200)
fieldcolor = (0, 0, 0)
linecolor = (50, 50, 50)
linewidth = 2
condition = ((-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0), (-1, 1),
             (0, 1), (1, 1))


def makefield():
    p = []
    for i in xrange(0, n):
        p.append([0] * n)
    return p


def drawcircle(window, x, y):
    pygame.draw.circle(window, (dotcolor), (x, y), dot_width / 2)


def drawfield(window, p):
    pygame.draw.rect(window, (fieldcolor), (0, 0, width, width), 0)
    for x in xrange(dot_width / 2, width, dot_width):
        pygame.draw.aaline(window, (linecolor), (x, 0), (x, width), linewidth)
        pygame.draw.aaline(window, (linecolor), (0, x), (width, x), linewidth)
    for xd in xrange(1, n):
        for yd in xrange(1, n):
            if p[xd][yd] == 1:
                drawcircle(window, xd * dot_width, yd * dot_width)
    pygame.display.flip()


def s_count(pos, x, y):
    s = 0
    for dx, dy in condition:
        if pos[(x + dx) % n][(y + dy) % n] == 1:
            s += 1
    return s


def main():
    pygame.init()
    pygame.display.set_mode((width, width))
    pygame.display.set_caption('Life')
    window = pygame.display.get_surface()
    pos = makefield()
    empty_pos = deepcopy(pos)
    state = 0
    drawfield(window, pos)
    while True:
        if state == 1:
            if pos == empty_pos:
                for xd in xrange(0, n):
                    for yd in xrange(0, n):
                        pos[xd][yd] = random.randint(0, 1)
            events = pygame.event.get()
            new_pos = deepcopy(pos)
            for x in xrange(0, n):
                for y in xrange(0, n):
                    s = s_count(pos, x, y)
                    if s > 3 or s < 2:
                        new_pos[x][y] = 0
                    if s == 3:
                        new_pos[x][y] = 1
            pos = new_pos
            drawfield(window, pos)
            sleep(0.1)
        else:
            events = [pygame.event.wait()]
        for event in events:
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 1 - state
            if state == 0:
                if event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0]:
                        (x1, y1) = event.pos
                        pos[x1 / dot_width][y1 / dot_width] = 1
                        drawfield(window, pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = 0
                        pos = deepcopy(empty_pos)
                        drawfield(window, pos)

if __name__=='__main__':
    main()
