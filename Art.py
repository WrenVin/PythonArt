import pygame
from random import randint
width=800
hight=600
pygame.init() #As necessary as import, initalizes pygame
gameDisplay = pygame.display.set_mode((width,hight))#Makes window
pygame.display.set_caption('Demo')#Titles window
clock = pygame.time.Clock()#Keeps time for pygame

end = False
gameDisplay.fill((0,0,255))

def drawShape():
    return pygame.draw.rect(gameDisplay, (randint(0,0),randint(0,0),randint(0,255)),
     (randint(0,0.75*width), randint(0,0.75*hight), randint(0,0.5*width), randint(0,0.5*width)))
  

while not end:
    #drawShape()
    #pygame.draw.rect(gameDisplay, (0,255,0), (10, 10, 4, 4))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            drawShape()
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameDisplay.fill((0,0,255))
        if event.type == pygame.QUIT:
            end = True

        print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
        





