import pygame
import math

windowHeight = 400  
windowWidth = 500

screen = pygame.display.set_mode((windowWidth,windowHeight))

angle = 0
zasieg = 100
class Miecz:
    def __init__(self, x, y, angle, image = pygame.image.load("texture\miecz.png")) -> None:
        self.x = x
        self.y = y
        self.image = image
        self.image_rotated = image
        self.angle = angle
    
    def draw(self):
        screen.blit(self.image_rotated, (self.x  ,self.y))

    def obrot_miecza(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == True:
            self.angle = 0
        if key[pygame.K_d] == True:
            self.angle = 270
        if key[pygame.K_s] == True:
            self.angle = 180
        if key[pygame.K_a] == True:
            self.angle = 90

        self.image_rotated = pygame.transform.rotate(self.image, self.angle)

miecz = Miecz(100,100, 0)      
while True:
    screen.fill('white')
    pygame.draw.circle(screen, ("black"), (windowWidth/2 , windowHeight/2), 25)
    #pygame.draw.rect(screen, ("black"), pygame.Rect(windowWidth/2 - 25 , windowHeight/2 - 25, 50, 50))
    miecz.obrot_miecza()
    miecz.draw()  
    
    
    #mieczx = windowWidth//2 + math.cos(angle) * zasieg
    #mieczy = windowWidth//2 + math.sin(angle) * zasieg
    
    
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    pygame.time.Clock().tick(60)