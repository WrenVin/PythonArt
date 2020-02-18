import pygame

width, height = 800, 600
pygame.init() #As necessary as import, initalizes pygame
gameDisplay = pygame.display.set_mode((width,height)) #Makes window
pygame.display.set_caption('Demo') #Titles window
clock = pygame.time.Clock() #Keeps time for pygame
gameDisplay.fill((0,0,255))

class Draw:
    def __init__(self):
        self.color = (255, 0, 0)

    def update(self, from_x, from_y, to_x, to_y):
        pygame.draw.circle(gameDisplay, self.color, (from_x, from_y), 5)
        pygame.draw.line(gameDisplay, self.color, (from_x, from_y), (to_x, to_y), 10)
        pygame.draw.circle(gameDisplay, self.color, (to_x, to_y), 5)

end = False
down = False
line = Draw()
while not end:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            lastx, lasty = event.pos
            down = True
        if event.type == pygame.MOUSEBUTTONUP:
            down = False
        if event.type == pygame.QUIT:
            end = True

    x, y = pygame.mouse.get_pos() 
    if down:
        line.update(lastx, lasty, x, y)
    lastx, lasty = x, y

    pygame.display.update()
    clock.tick(60)

pygame.quit()      





