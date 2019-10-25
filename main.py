import pygame
from board import Board

pygame.init()
pygame.display.set_caption("Connect Pops")
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()

game_over = False

b = Board()
b.draw(screen)
pygame.display.update()

while not game_over:
    clock.tick(60)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()