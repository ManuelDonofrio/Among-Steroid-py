import pygame


ANCHO = 800
ALTO = 600

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)

class Laser(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("Pygame.py\parcial_game\laser1.png")
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if(self.rect.bottom < 0):
			self.kill()