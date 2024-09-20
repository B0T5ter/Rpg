import pygame
import math

windowHeight = 400  
windowWidth = 500

screen = pygame.display.set_mode((windowWidth,windowHeight))
mieczpng = pygame.image.load("texture\miecz.png")
angle = 0
zasieg = 100
while True:
    screen.fill('white')
    mieczpng = pygame.transform.rotate(mieczpng, angle)
    pygame.draw.rect(screen, ("black"), pygame.Rect(windowWidth/2 - 25 , windowHeight/2 - 25, 50, 50))
    
    mieczx = windowWidth//2 + math.cos(angle) * zasieg
    mieczy = windowWidth//2 + math.sin(angle) * zasieg
    print(mieczx ,mieczy)
    screen.blit(mieczpng, (200  ,200))
    
    angle += 0.05
    
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    pygame.time.Clock().tick(60)