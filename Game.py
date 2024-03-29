#coding=utf-8
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Connect Pops")
font = pygame.font.Font(None, 30)
colors_by_value = {
                    2: (248, 24, 148), 4: (237, 41, 57), 8: (255, 211, 0),
                    16: (249, 166, 2), 32: (76, 187, 23), 64: (63, 224, 208),
                    128: (0, 142, 204), 256: (0, 0, 128), 512: (186, 102, 255),
                    1024: (114, 0, 163), 2048: (248, 24, 148), 4096: (237, 41, 57)
}
circles = []
level = 1
points = 0
is_menu = True


def get_value(limit):
    k = 0
    while k < limit:
        k += 1
        rnd_values = []
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
    text1 = font.render("%s" % level, True, (44, 117, 255))
    text2 = font.render("%s" % (level + 1), True, (44, 117, 255))
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
        value = font.render("%s" % self.value, True, (255, 255, 255))
        screen.blit(value, [self.x - 15, self.y - 8])


gameOver = False
while not gameOver:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            file_r = open("players.txt", "r")
            file_w = open("players.txt", "a")

            stroka = file_r.readline()
            if stroka != "":
                number = 0
                while stroka != "":
                    number = int(stroka.split(" ")[1])
                    stroka = file_r.readline()

                number += 1
                score = (level - 1) * 1000 + points
                file_w.write("Player %s %s \n" % (number, score))
            else:
                score = (level - 1) * 1000 + points
                file_w.write("Player 1 %s \n" % score)
            file_r.close()
            file_w.close()
            gameOver = True

        if is_menu:
            screen.fill((255, 255, 255))
            pops = pygame.image.load("popes.jpg")
            pops_rect = pops.get_rect()
            img = pygame.transform.scale(pops, (500, 700))
            screen.blit(img, pops_rect)
            pygame.draw.rect(screen, (44, 117, 255), (175, 200, 150, 40))
            play_text = font.render('Play', True, (255, 255, 255))
            screen.blit(play_text, [225, 210])
            pygame.display.update()
            pygame.draw.rect(screen, (44, 117, 255), (175, 280, 150, 40))
            restart_text2 = font.render('Restart', True, (255, 255, 255))
            screen.blit(restart_text2, [215, 290])
            pygame.display.update()
            pygame.draw.rect(screen, (44, 117, 255), (175, 360, 150, 40))
            records_text = font.render('Records', True, (255, 255, 255))
            screen.blit(records_text, [210, 370])
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONUP:
                coors = event.pos
                if 175 <= coors[0] <= 325 and 360 <= coors[1] <= 400:

                    file_r = open("players.txt", 'r')
                    screen.fill((255, 255, 255))
                    x_cord = 205
                    y_cord = 60
                    pygame.draw.rect(screen, (44, 117, 255), (20, 20, 460, 660))
                    for line in file_r.readlines()[len(file_r.readlines()) - 15:]:
                        player_text = font.render(line[:len(line)-2], True, (255, 255, 255))
                        screen.blit(player_text, [x_cord, y_cord])
                        y_cord += 40

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coors = event.pos


                if 175 <= coors[0] <= 325 and 280 <= coors[1] <= 320:
                    file_r = open("players.txt", "r")
                    file_w = open("players.txt", "a")
                    stroka = file_r.readline()
                    if stroka != "":
                        number = 0
                        while stroka != "":
                            number = int(stroka.split(" ")[1])
                            stroka = file_r.readline()
                        number += 1
                        score = (level - 1) * 1000 + points
                        file_w.write("Player %s %s \n" % (number, score))
                    else:
                        score = (level - 1) * 1000 + points
                        file_w.write("Player 1 %s \n" % score)
                    file_r.close()
                    file_w.close()
                    is_menu = False
                    level = 1
                    points = 0
                    screen.fill((255, 255, 255))
                    x = 110
                    y = 210
                    f = get_value(1000)
                    circles = []
                    for i in range(5):
                        for j in range(5):
                            circle = Circle(x, y, next(f))
                            circle.draw(screen)
                            circles.append(circle)
                            x += 70
                        x = 110
                        y += 70
                    else:
                        for circle in circles:
                            circle.draw(screen)

                    draw_progress_bar()
                    pygame.draw.rect(screen, (44, 117, 255), (360, 50, 80, 40))
                    restart_text = font.render('restart', True, (255, 255, 255))
                    screen.blit(restart_text, [368, 60])
                    pygame.display.update()
                    pygame.draw.rect(screen, (44, 117, 255), (80, 50, 80, 40))
                    menu_text = font.render('menu', True, (255, 255, 255))
                    screen.blit(menu_text, [94, 60])
                    pygame.display.update()

                    previous_value = 0
                    previous_center = (0, 0)
                    last_circle_coors = (0, 0)
                    sum = 0
                if 175 <= coors[0] <= 325 and 200 <= coors[1] <= 240:
                    is_menu = False
                    screen.fill((255, 255, 255))
                    x = 110
                    y = 210
                    f = get_value(1000)
                    if len(circles) == 0:
                        for i in range(5):
                            for j in range(5):
                                circle = Circle(x, y, next(f))
                                circle.draw(screen)
                                circles.append(circle)
                                x += 70
                            x = 110
                            y += 70
                    else:
                        for circle in circles:
                            circle.draw(screen)

                    draw_progress_bar()
                    pygame.draw.rect(screen, (44, 117, 255), (360, 50, 80, 40))
                    restart_text = font.render('restart', True, (255, 255, 255))
                    screen.blit(restart_text, [368, 60])
                    pygame.display.update()
                    pygame.draw.rect(screen, (44, 117, 255), (80, 50, 80, 40))
                    menu_text = font.render('menu', True, (255, 255, 255))
                    screen.blit(menu_text, [94, 60])
                    pygame.display.update()

                    previous_value = 0
                    previous_center = (0, 0)
                    last_circle_coors = (0, 0)
                    sum = 0
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coors = event.pos

                pygame.draw.rect(screen, (44, 117, 255), (360, 50, 80, 40))
                restart_text = font.render('restart', True, (255, 255, 255))
                screen.blit(restart_text, [368, 60])
                pygame.draw.rect(screen, (44, 117, 255), (80, 50, 80, 40))
                menu_text = font.render('menu', True, (255, 255, 255))
                screen.blit(menu_text, [94, 60])

                if 360 <= coors[0] <= 440 and 50 <= coors[1] <= 90:
                    file_r = open("players.txt", "r")
                    file_w = open("players.txt", "a")
                    stroka = file_r.readline()
                    if stroka != "":
                        number = 0
                        while stroka != "":
                            number = int(stroka.split(" ")[1])
                            stroka = file_r.readline()
                        number += 1
                        score = (level - 1) * 1000 + points
                        file_w.write("Player %s %s \n" % (number, score))
                    else:
                        score = (level - 1) * 1000 + points
                        file_w.write("Player 1 %s \n" % score)
                    file_r.close()
                    file_w.close()
                    level = 1
                    points = 0
                    screen.fill((255, 255, 255))
                    x = 110
                    y = 210
                    f = get_value(1000)
                    circles = []
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
                    restart_text = font.render('restart', True, (255, 255, 255))
                    screen.blit(restart_text, [368, 60])
                    pygame.display.update()
                    pygame.draw.rect(screen, (44, 117, 255), (80, 50, 80, 40))
                    menu_text = font.render('menu', True, (255, 255, 255))
                    screen.blit(menu_text, [94, 60])
                    pygame.display.update()

                    previous_value = 0
                    previous_center = (0, 0)
                    last_circle_coors = (0, 0)
                    sum = 0

                if 80 <= coors[0] <= 160 and 50 <= coors[1] <= 90:
                    is_menu = True

                for circle in circles:
                    if (coors[0] - circle.x) ** 2 + (coors[1] - circle.y) ** 2 <= 30 ** 2:
                        if previous_value == 0 and previous_center == (0, 0):

                            previous_value = circle.value
                            previous_center = (circle.x, circle.y)
                            last_circle_coors = (circle.x, circle.y)
                            sum += circle.value
                            circle.pressed = True
                        else:
                            if circle.value == previous_value and math.sqrt(
                                    (circle.x - previous_center[0]) ** 2 + (circle.y - previous_center[1]) ** 2) <= 99:
                                pygame.draw.line(screen, colors_by_value[circle.value],
                                                 [previous_center[0], previous_center[1]], [circle.x, circle.y], 3)
                                pygame.display.update()
                                previous_value = circle.value
                                previous_center = (circle.x, circle.y)
                                last_circle_coors = (circle.x, circle.y)
                                sum += circle.value
                                circle.pressed = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                screen.fill((255, 255, 255))
                pygame.draw.rect(screen, (44, 117, 255), (360, 50, 80, 40))
                restart_text = font.render('restart', True, (255, 255, 255))
                screen.blit(restart_text, [368, 60])
                pygame.display.update()
                pygame.draw.rect(screen, (44, 117, 255), (80, 50, 80, 40))
                menu_text = font.render('menu', True, (255, 255, 255))
                screen.blit(menu_text, [94, 60])
                pygame.display.update()
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
