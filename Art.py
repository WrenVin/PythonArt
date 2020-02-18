import pygame
from random import randint
width=800
height=600
pygame.init() #As necessary as import, initalizes pygame
global gameDisplay 
gameDisplay = pygame.display.set_mode((width,height))#Makes window
pygame.display.set_caption('Demo')#Titles window
clock = pygame.time.Clock()#Keeps time for pygame


gameDisplay.fill((0,0,255))

class Draw:
    def __init__(self):
        self.color = (255, 0, 0)

    def update(self, x, y):
        self.x = x
        self.y = y
        pygame.draw.circle(gameDisplay, self.color, (self.x, self.y), (5))


end = False
down = False
Line = Draw()
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
            Line.update(x, y)

        if event.type == pygame.QUIT:
            end = True
    lastx, lasty = pygame.mouse.get_pos()
    pygame.display.update(Line)

    clock.tick(60)

pygame.quit()
        





