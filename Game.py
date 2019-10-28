#coding=utf-8
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Connect Pops")
font = pygame.font.Font(None, 30)
colors_by_value = {2: (248, 24, 148), 4: (237, 41, 57), 8: (255, 211, 0), 16: (249, 166, 2), 32: (76, 187, 23), 64: (63, 224, 208), 128: (0, 142, 204), 256: (0, 0, 128), 512: (186, 102, 255), 1024: (114, 0, 163), 2048: (248, 24, 148), 4096: (237, 41, 57)}
circles = []
level = 1
points = 0


def get_value(limit):
    k = 0
    while k < limit:
        k += 1
        if level < 10:
            rnd_values = [2, 4, 8]
        if 10 <= level < 20:
            rnd_values = [2, 4, 8, 16]
        if 20 <= level < 30:
            rnd_values = [2, 4, 8, 16, 32]
        if 30 <= level < 40:
            rnd_values = [2, 4, 8, 16, 32, 64]
        if 40 <= level < 50:
            rnd_values = [2, 4, 8, 16, 32, 64, 128]
        if level >= 50:
            rnd_values = [2, 4, 8, 16, 32, 64, 128, 256]
        yield random.choice(rnd_values)


def get_coefficient():
    global level
    coefficient = 1
    if level < 10:
        coefficient = 2
    if 10 <= level < 20:
        coefficient = 4
    if 20 <= level < 30:
        coefficient = 8
    if 30 <= level < 40:
        coefficient = 16
    if 40 <= level < 50:
        coefficient = 32
    if level >= 50:
        coefficient = 64
    return coefficient


def choise_sum(sum):
    k = 0
    i = sum
    while i > 1:
        i /= 2
        k += 1
    if 2**k == sum:
        return 2**k
    else:
        return 2**(k-1)


def check_level():
    global points
    if points - 1000 > 0:
        global level
        level += 1
        points -= 1000


def draw_progress_bar():
    points_percent = float(points) / float(1000)
    pygame.draw.rect(screen, (44, 117, 255), (100, 120, int(300 * points_percent), 10))
    text1 = font.render(str(level), True, (44, 117, 255))
    text2 = font.render(str(level + 1), True, (44, 117, 255))
    screen.blit(text1, [80, 115])
    screen.blit(text2, [420, 115])


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


screen.fill((255, 255, 255))
x = 110
y = 210
f = get_value(1000)
for i in range(5):
    for j in range(5):
        circle = Circle(x, y, next(f))
        circle.draw(screen)
        circles.append(circle)
        x += 70
    x = 110
    y += 70
draw_progress_bar()
pygame.draw.rect(screen, (44, 117, 255), (360, 50, 80, 40))
text3 = font.render('restart', True, (255, 255, 255))
screen.blit(text3, [368, 60])
pygame.display.update()

gameOver = False
previous_value = 0
previous_center = (0, 0)
last_circle_coors = (0, 0)
sum = 0
while not gameOver:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coors = event.pos
            if 360 <= coors[0] <= 440 and 50 <= coors[1] <= 90:
                screen.fill((255, 255, 255))
                previous_value = 0
                previous_center = (0, 0)
                last_circle_coors = (0, 0)
                sum = 0
                circles = []
                level = 1
                points = 0
                x = 110
                y = 210
                f = get_value(1000)
                for i in range(5):
                    for j in range(5):
                        circle = Circle(x, y, next(f))
                        circle.draw(screen)
                        value = font.render(str(circle.value), True, (255, 255, 255))
                        screen.blit(value, [circle.x - 15, circle.y - 8])
                        circles.append(circle)
                        x += 70
                    x = 110
                    y += 70

                #points_percent = float(points) / float(1000)
                pygame.draw.rect(screen, (44, 117, 255), (100, 120, 1, 10))
                text1 = font.render(str(level), True, (44, 117, 255))
                text2 = font.render(str(level + 1), True, (44, 117, 255))
                screen.blit(text1, [80, 115])
                screen.blit(text2, [420, 115])

                pygame.draw.rect(screen, (44, 117, 255), (360, 50, 80, 40))
                text3 = font.render('restart', True, (255, 255, 255))
                screen.blit(text3, [368, 60])

                pygame.display.update()
            for circle in circles:
                if (coors[0] - circle.x)**2 + (coors[1] - circle.y)**2 <= 30**2:
                    if previous_value == 0 and previous_center == (0, 0):
                        previous_value = circle.value
                        previous_center = (circle.x, circle.y)
                        last_circle_coors = (circle.x, circle.y)
                        sum += circle.value
                        circle.pressed = True
                    else:
                        if circle.value == previous_value and math.sqrt((circle.x - previous_center[0])**2 + (circle.y - previous_center[1])**2) <= 99:
                            pygame.draw.line(screen, colors_by_value[circle.value], [previous_center[0], previous_center[1]], [circle.x, circle.y], 3)
                            pygame.display.update()
                            previous_value = circle.value
                            previous_center = (circle.x, circle.y)
                            last_circle_coors = (circle.x, circle.y)
                            sum += circle.value
                            circle.pressed = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (44, 117, 255), (360, 50, 80, 40))
            text3 = font.render('restart', True, (255, 255, 255))
            screen.blit(text3, [368, 60])
            for circle in circles:
                if circle.pressed:
                    if (circle.x, circle.y) != last_circle_coors:
                        new_circle = Circle(circle.x, circle.y, next(f))
                        circles.remove(circle)
                        circles.append(new_circle)
                        new_circle.draw(screen)
                    else:
                        new_circle = Circle(circle.x, circle.y, choise_sum(sum))
                        circles.remove(circle)
                        circles.append(new_circle)
                        new_circle.draw(screen)
                else:
                    circle.draw(screen)
            points += sum * get_coefficient()
            previous_center = (0, 0)
            previous_value = 0
            last_circle_coors = (0, 0)
            sum = 0
            check_level()
            draw_progress_bar()
            pygame.display.update()
    pygame.display.update()
pygame.quit()
