import numpy as np
import random
import pygame

class Board:
    def __init__(self):
        self.font = pygame.font.Font(None, 25)
        self.matrix = np.zeros((5, 5))
        for i in range(0, 5):
            for j in range(0, 5):
                self.matrix[i][j] = self.get_number(0)

    def get_number(self, level):
        if level < 10:
            list = [2, 4, 8]
        if 10 <= level < 20:
            list = [2, 4, 8, 16]
        if 20 <= level < 30:
            list = [2, 4, 8, 16, 32]
        if 30 <= level < 40:
            list = [2, 4, 8, 16, 32, 64]
        if 40 <= level < 50:
            list = [2, 4, 8, 16, 32, 64, 128]
        if level >= 50:
            list = [2, 4, 8, 16, 32, 64, 128, 256]
        index = int(random.random() * 10)
        while index > len(list) - 1:
            index = int(random.random() * 10)
        return list[index]

    def draw(self, screen):
        screen.fill((255, 255, 255))
        x = 100
        y = 200
        for i in range (0, 5):
            for j in range (0, 5):
                text = self.font.render(str(int(self.matrix[i][j])), True, (0, 0, 0))
                screen.blit(text, [x, y])
                x += 75
                if j == 4:
                    y += 50
                    x = 100

