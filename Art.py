import pygame
from random import randint
width=800
height=600
pygame.init() #As necessary as import, initalizes pygame
gameDisplay = pygame.display.set_mode((width,height))#Makes window
pygame.display.set_caption('Demo')#Titles window
clock = pygame.time.Clock()#Keeps time for pygame


gameDisplay.fill((0,0,255))

class Draw:
    def __init__(self, x, y, lastx, lasty):
        self.x = x
        self.y = y
        self.lastx = lastx
        self.lasty = lasty



end = False
down = False
while not end:
    x, y = pygame.mouse.get_pos()
    #drawShape()
    #pygame.draw.rect(gameDisplay, (0,255,0), (10, 10, 4, 4))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            down = True

        if event.type == pygame.MOUSEBUTTONUP:
            down = False

        if down:
            pass

        if event.type == pygame.QUIT:
            end = True
    lastx, lasty = pygame.mouse.get_pos()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
        





