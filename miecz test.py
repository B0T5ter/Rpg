import pygame
import math

windowHeight = 400  
windowWidth = 500

screen = pygame.display.set_mode((windowWidth,windowHeight))

angle = 0
zasieg = 100
class Miecz:
    def __init__(self, x, y, angle, image = pygame.image.load("texture\miecz.png")) -> None:
        self.x = 260
        self.y = 150
        self.image = image
        self.image_rotated = image
        self.angle = angle
        self.animacja = [pygame.image.load("texture\animacjamiecza1.png"), pygame.image.load("texture\animacjamiecza2.png"),pygame.image.load("texture\animacjamiecza3.png")]
        self.klatka_animacji = 0
    
    def draw(self):
        screen.blit(self.image_rotated, (self.x  ,self.y))

    def obrot_miecza(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == True:
            self.angle = 0
            self.x = 260  
            self.y = 150
        if key[pygame.K_d] == True:
            self.angle = 270
            self.x = 250  
            self.y = 205
        if key[pygame.K_s] == True:
            self.angle = 180
            self.x = 190
            self.y = 190
        if key[pygame.K_a] == True:
            self.angle = 90
            self.x = 200
            self.y = 140
        
        self.image_rotated = pygame.transform.rotate(self.image, self.angle)

miecz = Miecz(100,100, 0)      
while True:
    screen.fill('white')
    pygame.draw.circle(screen, ("black"), (windowWidth/2 , windowHeight/2), 25)
    miecz.obrot_miecza()
    miecz.draw()  
     
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    pygame.time.Clock().tick(60)