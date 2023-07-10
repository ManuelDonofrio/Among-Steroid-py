import pygame, random


ANCHO = 800
ALTO = 600

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)

class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Pygame.py\parcial_game\meteorGrey_big3.png ").convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ANCHO - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.velocidady = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.velocidady
		if(self.rect.top > ALTO + 10 or self.rect.left < -25 or self.rect.right > ANCHO + 22):
			self.rect.x = random.randrange(ANCHO - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.velocidady = random.randrange(1, 8)