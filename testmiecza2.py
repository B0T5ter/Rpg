import pygame
import math

# Inicjalizacja pygame
pygame.init()

# Parametry okna
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kwadrat krążący wokół innego kwadratu")

# Kolory
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Parametry kwadratów
square_size = 40  # rozmiar środkowego kwadratu
orbiter_size = 20  # rozmiar krążącego kwadratu

# Pozycja środkowego kwadratu
center_x = width // 2
center_y = height // 2

# Parametry orbity
orbit_radius = 100  # promień orbity
angle = 0  # początkowy kąt
speed = 0.05  # prędkość krążenia

# Główna pętla gry
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Czyszczenie ekranu
    screen.fill(black)

    # Rysowanie środkowego kwadratu
    pygame.draw.rect(screen, blue, (center_x - square_size // 2, center_y - square_size // 2, square_size, square_size))

    # Obliczanie pozycji krążącego kwadratu
    orbit_x = center_x + math.cos(angle) * orbit_radius
    orbit_y = center_y + math.sin(angle) * orbit_radius

    # Rysowanie krążącego kwadratu
    pygame.draw.rect(screen, red, (orbit_x - orbiter_size // 2, orbit_y - orbiter_size // 2, orbiter_size, orbiter_size))

    # Aktualizacja kąta dla krążącego kwadratu
    angle += speed

    # Aktualizacja ekranu
    pygame.display.flip()

    # Opóźnienie, aby ograniczyć liczbę FPS
    pygame.time.Clock().tick(60)

# Zakończenie pygame
pygame.quit()
