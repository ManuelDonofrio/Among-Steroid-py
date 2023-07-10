import pygame, random, re, sys
from records import *
from funciones import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame.py\parcial_game\jjugador.png").convert()
        self.image.set_colorkey(NEGRO)
        self.image = pygame.transform.scale(self.image, (114, 114))  
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
		
class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Pygame.py\parcial_game\menemy2.png").convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ANCHO - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.velocidady = random.randrange(5, 10)
		self.speedx = random.randrange(2, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.velocidady
		if(self.rect.top > ALTO + 10 or self.rect.left < -25 or self.rect.right > ANCHO + 22):
			self.rect.x = random.randrange(ANCHO - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.velocidady = random.randrange(1, 8)

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

class Explosion(pygame.sprite.Sprite):
      def __init__(self, center):
            super().__init__()
            self.image = explosion_anim[0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 50

      def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                  self.last_update = now
                  self.frame += 1
                  if self.frame == len(explosion_anim):
                        self.kill()
                  else:
                        center = self.rect.center
                        self.image = explosion_anim[self.frame]
                        self.rect = self.image.get_rect()
                        self.rect.center = center
                                                   				                    
def dibujar_texto(surface, text, size, x, y):
	fuente = pygame.font.SysFont("verdana", size) 
	text_surface = fuente.render(text, True, BLANCO)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surface.blit(text_surface, text_rect)

def dibujar_vida(surface, x, y, percentage):
	LARGO_BARRA = 100
	ALTURA_BARRA = 10
	fill = (percentage / 100) * LARGO_BARRA
	border = pygame.Rect(x, y, LARGO_BARRA, ALTURA_BARRA)
	fill = pygame.Rect(x, y, fill, ALTURA_BARRA)
	pygame.draw.rect(surface, VERDE, fill)
	pygame.draw.rect(surface, BLANCO, border, 2)
	
def mostrar_pantalla_go():
	ventana.blit(fondo_inicio, [0,0])
	dibujar_texto(ventana, "Among Asteroid", 75, ANCHO // 2, ALTO // 3)
	dibujar_texto(ventana, "Presiona cualquier tecla para continuar", 20, ANCHO // 2, ALTO * 3/4)
	pygame.display.flip()
	esperando = True
	while esperando:
		reloj.tick(60)
		for evento in pygame.event.get():
			if(evento.type == pygame.QUIT):
				pygame.quit()
			if(evento.type == pygame.KEYUP):
				esperando = False

def ingresar_nombre():
	
    ventana.fill(NEGRO)
    dibujar_texto(ventana, "Ingresa tu nombre", 32, ANCHO // 2, ALTO // 15)
    pygame.draw.rect(ventana, BLANCO, (ANCHO // 4, ALTO // 2, ANCHO // 2, 32))
    pygame.display.flip()

    nombre = ""
    ingresando = True
    while ingresando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if re.match("^[A-Za-z]+$", nombre):
                        ingresando = False
                    else:
                        nombre = ""
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        ventana.fill(NEGRO)
        dibujar_texto(ventana, "Ingresa tu nombre", 32, ANCHO // 2, ALTO // 4)
        pygame.draw.rect(ventana, BLANCO, (ANCHO // 4, ALTO // 2, ANCHO // 2, 32))

        nombre_texto = pygame.font.SysFont("verdana", 32).render(nombre, True, NEGRO)
        ventana.blit(nombre_texto, (ANCHO // 2 - nombre_texto.get_width() // 2, ALTO // 2 - nombre_texto.get_height() // 4))

        pygame.display.flip()

    return nombre
   
def mostrar_pantalla_final():
    ventana.blit(fondo_inicio, [0,0])
    dibujar_texto(ventana, "FIN DE PARTIDA", 50, ANCHO // 2, ALTO // 3 - 50)
    dibujar_texto(ventana, "Puntaje obtenido: " + str(puntaje), 35, ANCHO // 2, ALTO // 2 - 100)
    dibujar_texto(ventana, "¿Deseas volver a jugar?", 25, ANCHO // 2, ALTO // 2 - 50)
    dibujar_texto(ventana, "Presiona Y para volver a jugar", 20, ANCHO // 2, ALTO // 2)
    dibujar_texto(ventana, "Presiona N para salir", 20, ANCHO // 2, ALTO // 2 + 50)
    dibujar_texto(ventana, "TOP 3 PUNTUACIONES", 25, ANCHO // 2, ALTO // 2 + 150)

    mejores_puntuaciones = obtener_mejores_puntajes(3)
    
    y_offset = ALTO // 2 + 200
    for i, (nombre_puntuacion, score) in enumerate(mejores_puntuaciones):
        texto_puntuacion = f"{nombre_puntuacion}: {score}"
        dibujar_texto(ventana, texto_puntuacion, 25, ANCHO // 2, y_offset)
        y_offset += 35  # Aumentar el offset vertical para la siguiente puntuación

    pygame.display.flip()        
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_y:
                    esperando = False  # Volver a jugar
                elif evento.key == pygame.K_n:
                    pygame.quit()  # Salir del juego	

def terminar_juego():
    conexion.close()
    pygame.quit()
    sys.exit()	

# Constantes
ANCHO = 800
ALTO = 600
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Juego
pygame.init()
pygame.mixer.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("AMONG ASTEROID")
reloj = pygame.time.Clock()

# Cargar explosion.
explosion_anim = []
for i in range(9):
    archivo = "Pygame.py/parcial_game/explosion{:02d}.png".format(i)
    imagen = pygame.image.load(archivo).convert()
    imagen.set_colorkey(NEGRO)
    imagen_escala = pygame.transform.scale(imagen, (70, 70))
    explosion_anim.append(imagen_escala)

# Cargar fondo.
fondo = pygame.image.load("Pygame.py\parcial_game\galaxifondo.jpg").convert()
fondo_inicio = pygame.image.load("Pygame.py\parcial_game\galaxy_universe_space_138271_800x600.jpg").convert()
fondo_inicio = pygame.transform.scale(fondo_inicio, [800,600])

# Cargar sonidos.
sonido_laser = pygame.mixer.Sound("Pygame.py\parcial_game\sounds_shoot.wav")
sonido_colision = pygame.mixer.Sound("Pygame.py\parcial_game\_explosion.wav")
pygame.mixer.music.load("Pygame.py\parcial_game\_music.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1) #Loop infinto de la musica

# Bucle principal del juego
puntaje = 0
juego_terminado = True
nombre_usuario = ""
jugando = True

conexion = sqlite3.connect("records.db")
crear_tabla()

while jugando:
    if juego_terminado:    
        mostrar_pantalla_go()
        nombre_usuario = ingresar_nombre()
        juego_terminado = False
        puntaje = 0  # Reiniciar puntaje al iniciar un nuevo juego
        cantidad_asteroides = 0
        
        # Reiniciar juego
        sprites = pygame.sprite.Group()
        lista_enemigos = pygame.sprite.Group()
        balas = pygame.sprite.Group()
        jugador = Player()
        sprites.add(jugador)
        for i in range(4):
            enemigo = Enemigo()
            sprites.add(enemigo)
            lista_enemigos.add(enemigo)
    
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.disparar() 

    # Actualizar
    sprites.update()

    # Colisiones meteoro - laser
    colision = pygame.sprite.groupcollide(lista_enemigos, balas, True, True)
    for hit in colision:
        puntaje += 1
        if puntaje % 10 == 0:
             cantidad_asteroides += 1
             
        sonido_colision.play()
        explosion = Explosion(hit.rect.center)
        sprites.add(explosion)
        asteroide = Enemigo()
        sprites.add(asteroide)
        lista_enemigos.add(asteroide)
    
    # Colisiones jugador - meteoro
    colisiones = pygame.sprite.spritecollide(jugador, lista_enemigos, True)
    for colision in colisiones:
        jugador.vida -= 25
        asteroide = Enemigo()
        sprites.add(asteroide)
        lista_enemigos.add(asteroide)
        if jugador.vida <= 0:
            juego_terminado = True
            guardar_puntaje(nombre_usuario, puntaje)
            mostrar_pantalla_final()
            
    
    # Dibujar
    ventana.blit(fondo, [0, 0])
    sprites.draw(ventana)
    
    # Marcador
    dibujar_texto(ventana, str(puntaje), 25, ANCHO // 2, 10)

    # Vida
    dibujar_vida(ventana, 5, 5, jugador.vida)

    pygame.display.flip()

terminar_juego()