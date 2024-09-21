import pygame
pygame.mixer.init()
#Okienko 
windowHeight = 400  
windowWidth = 500
screen = pygame.display.set_mode((windowWidth,windowHeight))
CLOCK = pygame.time.Clock()
szybkosc_ruchu = 3.5

#Czytanie mapy
f = open('mapa.txt', 'r').read()
f = f.split("\n")
mapaUlozenie = []
for x in f:
    mapaUlozenie.append(x.split(' '))

#Wczytywanie textur
wodaPng = pygame.image.load("texture\woda.png")
sciezkaPng = pygame.image.load("texture\sciezka.png")
ziemiaPng = pygame.image.load("texture\ziemia.png")

# Klasa powierzchni i czytanie jej
class Powierzchnia:
    def __init__(self, x, y, image, kolizja) -> None:
        self.x = x
        self.y = y
        self.w = self.h = 50
        self.image = image
        self.kolizja = kolizja

    def rysowanie(self):
        screen.blit(self.image, (self.x, self.y))

    def ruch_pion(self, ruch):
        self.y += ruch
    
    def ruch_poziom(self, ruch):
        self.x += ruch

    def return_pozycji(self):
        return self.x, self.y
    
powierzchniazbior = []
for x in range(len(mapaUlozenie)):
    for y in range(len(mapaUlozenie[0]) - 1):
        if mapaUlozenie[x][y] == "0":
            powierzchniazbior.append(Powierzchnia(y*50, x*50, wodaPng, True))
        if mapaUlozenie[x][y] == "1":
            powierzchniazbior.append(Powierzchnia(y*50, x*50, ziemiaPng, False))   
        if mapaUlozenie[x][y] == "2":
            powierzchniazbior.append(Powierzchnia(y*50, x*50, sciezkaPng, False))

# Klasa postaci
class Postac:
    def __init__(self) -> None:
        pass

    def rysowanie(self):
        p = pygame.Rect(50,50, 100, 100)
        screen.blit(p, (0,0,0))

postac = Postac()

# Sprawdzanie kolizji
def sprawdzenie_kolizji(gora, dol, lewo, prawo):
    postacx, postacy = windowWidth/2 - 25 , windowHeight/2 - 25
    if gora == True:
        for kafelek in powierzchniazbior:
            if kafelek.kolizja == True:
                if postacy <= kafelek.y + 50 + szybkosc_ruchu and postacy > kafelek.y  and postacx + 50 >= kafelek.x and postacx < kafelek.x + 50:
                    return False
    if dol == True:
        for kafelek in powierzchniazbior:
            if kafelek.kolizja == True:
                if postacy + 50 + szybkosc_ruchu >= kafelek.y and postacy < kafelek.y  and postacx + 50 >= kafelek.x and postacx < kafelek.x + 50:
                    return False
    if lewo == True:
        for kafelek in powierzchniazbior:
            if kafelek.kolizja == True:
                if postacx <= kafelek.x + 50 + szybkosc_ruchu and postacx > kafelek.x  and postacy + 50 >= kafelek.y and postacy < kafelek.y + 50:
                    return False
    if prawo == True:
        for kafelek in powierzchniazbior:
            if kafelek.kolizja == True:
                if postacx + 50 + szybkosc_ruchu >= kafelek.x  and postacx < kafelek.x  and postacy + 50 >= kafelek.y and postacy < kafelek.y + 50:
                    return False
    return True
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
    #Rysowanie podloza
    for x in powierzchniazbior:
        x.rysowanie()
    #print(powierzchniazbior[0].x, powierzchniazbior[0].y)
    #Rysowanie postaci
    pygame.draw.circle(screen, ("black"), (windowWidth/2 , windowHeight/2), 25)
    miecz.obrot_miecza()
      
    miecz.sword_swing()
    miecz.draw()
    #Ruszanie się
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True and sprawdzenie_kolizji(True, False, False, False) == True:
        for x in powierzchniazbior:
            x.ruch_pion(szybkosc_ruchu)
    if key[pygame.K_s] == True and sprawdzenie_kolizji(False, True, False, False) == True:
        for x in powierzchniazbior:
            x.ruch_pion(-szybkosc_ruchu)
    if key[pygame.K_a] == True and sprawdzenie_kolizji(False, False, True, False) == True:
        for x in powierzchniazbior:
            x.ruch_poziom(szybkosc_ruchu)
    if key[pygame.K_d] == True and sprawdzenie_kolizji(False, False, False, True) == True:
        for x in powierzchniazbior:
            x.ruch_poziom(-szybkosc_ruchu)


    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    CLOCK.tick(60)
