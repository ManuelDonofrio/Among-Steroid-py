import pygame
from laser import Laser
import pygame.mixer

ANCHO = 800
ALTO = 600

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)

sprites = pygame.sprite.Group()
lista_enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()
pygame.mixer.init()
sonido_laser = pygame.mixer.Sound("Pygame.py\parcial_game\_laser5.ogg")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame.py/parcial_game/player.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad_x = 0
        self.vida = 100

    def update(self):
        self.velocidad_x = 0
        keystate = pygame.key.get_pressed()
        if(keystate[pygame.K_LEFT]):
            self.velocidad_x = -5
        if(keystate[pygame.K_RIGHT]):
            self.velocidad_x = 5
        self.rect.x += self.velocidad_x
        if(self.rect.right > ANCHO):
            self.rect.right = ANCHO
        if(self.rect.left < 0):
            self.rect.left = 0

    def disparar(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        sprites.add(laser)
        balas.add(laser)
        sonido_laser.play()