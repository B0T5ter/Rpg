import pygame

#Okienko 
windowHeight = 400  
windowWidth = 500
screen = pygame.display.set_mode((windowWidth,windowHeight))

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

class Powierzchnia:
    def __init__(self, x, y, image) -> None:
        self.x = x
        self.y = y
        self.w = self.h = 50
        self.image = image

    def rysowanie(self):
        screen.blit(self.image, (self.x, self.y))

    def __str__(self) -> str:
        return self.x, self.y
    
powierzchniazbior = []
for x in range(len(mapaUlozenie)):
    for y in range(len(mapaUlozenie[0]) - 1):
        if mapaUlozenie[x][y] == "0":
            powierzchniazbior.append(Powierzchnia(y*50, x*50, wodaPng))
        if mapaUlozenie[x][y] == "1":
            powierzchniazbior.append(Powierzchnia(y*50, x*50, ziemiaPng))   
        if mapaUlozenie[x][y] == "2":
            powierzchniazbior.append(Powierzchnia(y*50, x*50, sciezkaPng))




while True:
    for x in powierzchniazbior:
        x.rysowanie()
        
    

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
