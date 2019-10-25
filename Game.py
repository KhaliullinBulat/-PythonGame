import pygame
import random
import numpy as np

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Some_game '2048'")

class Krug:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    color = (255, 0, 0)
    value = 0
    state = 'unselected'


class Map:
    def __init__(self, width, height, elements):
        counter = 0
        self.field = []
        for x in range(width):
            for y in range(height):
                counter += 1
                self.field[x, y] = elements[counter]


rnd_values = [2, 4, 8, 16, 32, 64]
colors_by_value = {2: (0, 122, 122), 4: (122, 122, 0), 8: (122, 0, 122), 16: (188, 0, 188), 32: (188, 188, 0), 64: (0, 188, 188)}

x = 50
y = 50
width = 40
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    for x_coor in range(5):
        for y_coor in range(5):
            circ = Krug(x_coor*50 + 100, y_coor*50 + 100)
            circ.value = random.choice(rnd_values)
            circ.color = colors_by_value[circ.value]
            pygame.draw.circle(win, circ.color, (circ.x, circ.y), 20)
    pygame.display.update()

pygame.quit()
