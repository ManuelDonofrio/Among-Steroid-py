import pygame

ANCHO = 800
ALTO = 600

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)

ventana = pygame.display.set_mode((ANCHO, ALTO))
fondo_inicio = pygame.image.load("Pygame.py\parcial_game\galaxiapa.jpg").convert()
fondo_inicio = pygame.transform.scale(fondo_inicio, [800,600])
reloj = pygame.time.Clock()
puntaje = 0

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
	dibujar_texto(ventana, "Space Shooter", 65, ANCHO // 2, ALTO // 8)
	dibujar_texto(ventana, "Derriba la mayor cantidad de asteroides sin que te choquen", 24, ANCHO // 2, ALTO // 3)
	dibujar_texto(ventana,f"Puntaje obtenido: {puntaje}", 50, ANCHO // 2, ALTO * 2/4)
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
	
    ventana.fill(VERDE)
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
    dibujar_texto(ventana, "FIN DE PARTIDA", 32, ANCHO // 2, ALTO // 3)
    dibujar_texto(ventana, "Puntaje obtenido: " + str(puntaje), 20, ANCHO // 2, ALTO // 2 - 30)
    dibujar_texto(ventana, "¿Deseas volver a jugar?", 20, ANCHO // 2, ALTO // 2)
    dibujar_texto(ventana, "Presiona Y para volver a jugar", 20, ANCHO // 2, ALTO // 2 + 30)
    dibujar_texto(ventana, "Presiona N para salir", 20, ANCHO // 2, ALTO // 2 + 60)
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

