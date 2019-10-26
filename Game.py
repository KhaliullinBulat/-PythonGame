#coding=utf-8
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Connect Pops")
font = pygame.font.Font(None, 30)
rnd_values = [2, 4, 8, 16, 32, 64, 128, 256]
colors_by_value = {2: (248, 24, 148), 4: (237, 41, 57), 8: (255, 211, 0), 16: (249, 166, 2), 32: (76, 187, 23), 64: (63, 224, 208), 128: (0, 142, 204), 256: (0, 0, 128)}
circles = []


class Circle:
    def __init__(self, x, y, value, pressed=False):
        self.x = x
        self.y = y
        self.value = value
        self.pressed = pressed

    def draw(self, screen):
        pygame.draw.circle(screen, colors_by_value[self.value], (self.x, self.y), 30)
        value = font.render(str(self.value), True, (255, 255, 255))
        screen.blit(value, [self.x - 15, self.y - 8])

class Map:
    def __init__(self, width, height, elements):
        counter = 0
        self.field = []
        for i in range(width):
            for j in range(height):
                counter += 1
                self.field[i, j] = elements[counter]


screen.fill((255, 255, 255))
x = 110
y = 210
for i in range(5):
    for j in range(5):
        circle = Circle(x, y, random.choice(rnd_values))
        circle.draw(screen)
        value = font.render(str(circle.value), True, (255, 255, 255))
        screen.blit(value, [circle.x - 15, circle.y - 8])
        circles.append(circle)
        x += 70
    x = 110
    y += 70
pygame.display.update()

gameOver = False
previous_value = 0
previous_center = (0, 0)
while not gameOver:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coors = event.pos
            for circle in circles:
                if (coors[0] - circle.x)**2 + (coors[1] - circle.y)**2 <= 30**2:
                    if previous_value == 0 and previous_center == (0, 0):
                        previous_value = circle.value
                        previous_center = (circle.x, circle.y)
                        circle.pressed = True
                    else:
                        if circle.value == previous_value and math.sqrt((circle.x - previous_center[0])**2 + (circle.y - previous_center[1])**2) <= 99:
                            pygame.draw.line(screen, colors_by_value[circle.value], [previous_center[0], previous_center[1]], [circle.x, circle.y], 3)
                            pygame.display.update()
                            previous_value = circle.value
                            previous_center = (circle.x, circle.y)
                            circle.pressed = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            previous_center = (0, 0)
            previous_value = 0
            screen.fill((255, 255, 255))
            for circle in circles:
                if circle.pressed:
                    #заменить здесь рандомное значение на сумму значений выбранных кружков
                    new_circle = Circle(circle.x, circle.y, random.choice(rnd_values))
                    circles.remove(circle)
                    circles.append(new_circle)
                    new_circle.draw(screen)
                else:
                    circle.draw(screen)
            pygame.display.update()

pygame.display.update()
pygame.quit()
