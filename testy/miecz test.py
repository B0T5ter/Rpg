import pygame
import math
pygame.mixer.init()

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
        self.rotated_swing = image
        self.angle = angle
        self.animacja = [pygame.image.load("texture\\animacjamiecza1.png"), pygame.image.load("texture\\animacjamiecza2.png"),pygame.image.load("texture\\animacjamiecza3.png")]
        self.klatka_animacji = 0
        self.swing_time = 0
        self.kierunek = 1
        self.odglosy_miecza = [pygame.mixer.Sound("sounds\swordsound1.mp3"), pygame.mixer.Sound("sounds\swordsound2.mp3"), pygame.mixer.Sound("sounds\swordsound3.mp3")]
    def draw(self):
        screen.blit(self.image_rotated, (self.x  ,self.y))
    def sword_swing(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] == True:
            if self.swing_time <= 0:
                self.rotated_swing = self.animacja[self.klatka_animacji]
                pygame.mixer.Sound.play(self.odglosy_miecza[self.klatka_animacji])
                self.swing_time = 20
                self.klatka_animacji += 1
                if self.klatka_animacji == 3:
                    self.klatka_animacji = 0
        if self.swing_time > 0:
            if self.kierunek == 1:
                self.x = 200  
                self.y = 100
            if self.kierunek == 2:
                    self.x = 150
            if self.kierunek == 3:
                self.x = 190 
                self.y = 190
            if self.kierunek == 4:
                    self.y = 150
        self.swing_time -= 1
        if self.swing_time <= 0:
            self.rotated_swing = self.image
            if self.kierunek == 1:
                self.x = 260  
                self.y = 150
            if self.kierunek == 2:
                self.x = 200 
                self.y = 140
            if self.kierunek == 3:
                self.x = 190  
                self.y = 190
            if self.kierunek == 4:
                self.x = 250 
                self.y = 205
        print(self.kierunek)   

    def obrot_miecza(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == True:
            self.angle = 0
            self.x = 260  
            self.y = 150
            self.kierunek = 1
        if key[pygame.K_d] == True:
            self.angle = 270
            self.x = 250  
            self.y = 205
            self.kierunek = 4
        if key[pygame.K_s] == True:
            self.angle = 180
            self.x = 190
            self.y = 190
            self.kierunek = 3
        if key[pygame.K_a] == True:
            self.angle = 90
            self.x = 200
            self.y = 140
            self.kierunek = 2
        
        self.image_rotated = pygame.transform.rotate(self.rotated_swing, self.angle)

miecz = Miecz(100,100, 0)      
while True:
    screen.fill('white')
    pygame.draw.circle(screen, ("black"), (windowWidth/2 , windowHeight/2), 25)
    miecz.obrot_miecza()
    miecz.draw()  
    miecz.sword_swing()
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    pygame.time.Clock().tick(60)