import pygame

width, height = 850, 530
pygame.init() #As necessary as import, initalizes pygame
gameDisplay = pygame.display.set_mode((width,height)) #Makes window
pygame.display.set_caption('Art') #Titles window
clock = pygame.time.Clock() #Keeps time for pygame
gameDisplay.fill((0,0,0))
#loadimg = pygame.image.load('test.png')
#gameDisplay.blit(loadimg, (0,0))

class Draw:
    def __init__(self):
        self.color = (255, 255, 255)

    def update(self, from_x, from_y, to_x, to_y):
        pygame.draw.circle(gameDisplay, self.color, (from_x, from_y), 4.9)
        pygame.draw.line(gameDisplay, self.color, (from_x, from_y), (to_x, to_y), 10)
        pygame.draw.circle(gameDisplay, self.color, (to_x, to_y), 4.9)

def SaveScreen(screen, name):
    img = pygame.Surface((850, 450))
    img.blit(screen, (0,0), (0,0, 850, 450))
    pygame.image.save(img, name)

end = False
down = False
line = Draw()
while not end:
    key = pygame.key.get_pressed()
    #if key[pygame.K_s]:
        #SaveScreen(gameDisplay, 'test.png')
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
    pygame.draw.rect(gameDisplay, (255,255,255), (0, 450, 850, 80))

    pygame.display.update()
    clock.tick(60)

pygame.quit()