import pygame

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
                if postacy <= kafelek.y + 50 and postacy > kafelek.y  and postacx + 50 >= kafelek.x and postacx < kafelek.x + 50:
                    print(postacx, kafelek.x, postacy, kafelek.y)
                    print(postacy <= kafelek.y + 50, postacx + 50 >= kafelek.x, postacx < kafelek.x + 50)
                    return False
    return True
print(windowWidth/2 - 25 , windowHeight/2 - 25)
print(powierzchniazbior[0].x, powierzchniazbior[0].y)
while True:
    screen.fill('white')
    #Rysowanie podloza
    for x in powierzchniazbior:
        x.rysowanie()
    #print(powierzchniazbior[0].x, powierzchniazbior[0].y)
    #Rysowanie postaci
    pygame.draw.rect(screen, ("black"), pygame.Rect(windowWidth/2 - 25 , windowHeight/2 - 25, 50, 50))

    #Ruszanie się
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True and sprawdzenie_kolizji(True, False, False, False) == True:
        for x in powierzchniazbior:
            x.ruch_pion(szybkosc_ruchu)
    if key[pygame.K_s] == True:
        for x in powierzchniazbior:
            x.ruch_pion(-szybkosc_ruchu)
    if key[pygame.K_a] == True:
        for x in powierzchniazbior:
            x.ruch_poziom(szybkosc_ruchu)
    if key[pygame.K_d] == True:
        for x in powierzchniazbior:
            x.ruch_poziom(-szybkosc_ruchu)


    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    CLOCK.tick(60)
