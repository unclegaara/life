import pygame
from copy import deepcopy
from time import sleep
from pygame.locals import *
import random
xd = 0
yd = 0
n = 160
dot_width = 5
width = dot_width * n
dotcolor = (255, 255, 255)
linecolor = (100, 100, 100)
linewidth = 2
condition = ((-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0), (-1, 1),
             (0, 1), (1, 1))

pygame.init()
pygame.display.set_mode((width, width))
pygame.display.set_caption('Life')
window = pygame.display.get_surface()




def makefield():
    p = []
    for i in range(0, n):
        p.append([0] * n)
    return p


def drawcircle(x, y):
    pygame.draw.circle(window, (dotcolor), (x, y), dot_width / 2)


def drawfield(p):
    pygame.draw.rect(window, (000, 000, 000), (0, 0, width, width), 0)
    #for x in range(dot_width / 2, width, dot_width):
    #    pygame.draw.aaline(window, (linecolor), (x, 0), (x, width), linewidth)
    #    pygame.draw.aaline(window, (linecolor), (0, x), (width, x), linewidth)
    for xd in range(1, n):
        for yd in range(1, n):
            if p[xd][yd] == 1:
                drawcircle(xd * dot_width, yd * dot_width)
    pygame.display.flip()

pos = makefield()

def s_count(x, y):
    s = 0
    for dx, dy in condition:
        if pos[(x + dx) % n][(y + dy) % n] == 1:
            s += 1
    return s

for xd in range(0, n):
    for yd in range(0, n):
        pos[xd][yd] = random.randint(0, 1)
drawfield(pos)

while 1:
    new_pos = deepcopy(pos)
    for x in range(0, n):
        for y in range(0, n):
            s = s_count(x, y)
            if s > 3 or s < 2:
                new_pos[x][y] = 0
            if s == 3:
                new_pos[x][y] = 1
    pos = new_pos
    drawfield(pos)
    sleep(0.1)
