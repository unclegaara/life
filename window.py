import pygame, random
from copy import deepcopy
from time import sleep
n = 133
dot_width = 6
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


def drawfield(window, p):
    pygame.draw.rect(window, (fieldcolor), (0, 0, width, width), 0)
    for x in xrange(dot_width / 2, width, dot_width):
        pygame.draw.aaline(window, (linecolor), (x, 0), (x, width), linewidth)
        pygame.draw.aaline(window, (linecolor), (0, x), (width, x), linewidth)
    for xd in xrange(1, n):
        for yd in xrange(1, n):
            if p[xd][yd] == 1:
                pygame.draw.circle(window, (dotcolor),
                (xd * dot_width, yd * dot_width), dot_width / 2)
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
    state = 0
    for xd in xrange(0, n):
        for yd in xrange(0, n):
            pos[xd][yd] = random.randint(0, 1)
    drawfield(window, pos)
    while True:
        if state == 1:
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    state = 1 - state
if __name__=='__main__':
    main()
