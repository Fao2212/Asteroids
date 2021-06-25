# Se crea la pantalla

#Se carga el jugdor en el centro

#Crear asteroides en posiciones aleatorias desde los bordes

# Puntaje/Vidas...

from pygame import Vector2, math
from Asteroide import Asteroide
from Jugador import Jugador
import pygame
from pygame.locals import *
import random

#Clase creadora de textos
class TextGen(pygame.sprite.Sprite):
    white = (255,255,255) 
    orange = (255, 98, 0)
    def __init__(self,text,x,y,info):
        super().__init__()
        self.info = info
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.surface = self.font.render(self.text+" "+str(self.info()), True, self.white, self.orange)
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x,y)
    def show():
        pass
    def hide():
        pass
    def update(self):
        self.surface = self.font.render(self.text+" "+str(self.info()), True, self.white, self.orange)
    def changeColor(self,color):
        pass
    def changeFont(self,font):
        font

#Inicializa pygame
pygame.init()

#Frames
FramePerSec = pygame.time.Clock()
FPS = 60

#Crea la pantalla
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Clase que controla el juego
class GameManager:
    def __init__(self):
        self.asteroides = pygame.sprite.Group()
        self.jugadores = pygame.sprite.Group()
        self.text = pygame.sprite.Group()
        self.balas = pygame.sprite.Group()
        self.currentSecond = 0
        self.secondPassed = False
        self.currentLevel = 0
        self.gameOver = False
        self.tiempoDeSpawn = 4
        self.pause = False
        self.addPlayer()
        self.createText()    

    def addPlayer(self):
        self.jugador = Jugador()
        self.jugador.setPos(WIDTH/2,HEIGHT/2)
        self.jugadores.add(self.jugador)

    def playerDied(self):
        if not self.jugador.alive:
            print("Dead")
            if self.jugador.lives > 0:
                print("Lives left")
                self.addPlayer()
            else:
                game.gameOver = False
                print("Game Over")
            

    def countAsteroides(self):
        return len(self.asteroides)

    def createText(self):#Funcion que carga todos los textos
        asteroidCount = TextGen("Asteroides:",0,0,self.countAsteroides)
        self.text.add(asteroidCount)

    def getRandomPos(self): #Probabilidad del 50%
        prob = random.randint(0,100)
        if prob < 25:
            return Vector2(random.randint(0, WIDTH),0)
        if prob < 50:
            return Vector2(0,random.randint(0, HEIGHT))
        if prob < 75:
            return Vector2(random.randint(0, WIDTH),HEIGHT)
        else:
            return Vector2(WIDTH,random.randint(0, HEIGHT))

    def crearAsteroides(self,cantidad):
        for i in range(cantidad):
            ast = Asteroide(self.jugador)   #Si luego se quieren mas jugaores, podria seguir al vivo mas cercano
            ast.setPos(self.getRandomPos())
            self.asteroides.add(ast)

    def checkLimiteJugadores(self):
        for sprite in self.jugadores:
            if sprite.pos.x > WIDTH:
                sprite.pos.x  = 0
            if sprite.pos.x  < 0:
                sprite.pos.x  = WIDTH
            if sprite.pos.y  > HEIGHT:
                sprite.pos.y  = 0
            if sprite.pos.y  < 0:
                sprite.pos.y  = HEIGHT


    def getSeconds(self):
        ticks=pygame.time.get_ticks()
        return int(ticks/1000 % 60)



    def setSecond(self):  
        second = self.getSeconds()
        if self.currentSecond != second:
            self.currentSecond = second
            self.secondPassed = True

    def paused(self):
        self.pause = not self.pause

game = GameManager()

#Game Loop
while not game.gameOver:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

#Pintan en negro volver a cargar el fondo
    screen.fill((0,0,0))  

#Se cargan los estados de los sprites
    for asteroide in game.asteroides:
        asteroide.moverse()
        asteroide.bulletCollision(game.balas)
        screen.blit(asteroide.surface,asteroide.rect)
    for jugador in game.jugadores:
        jugador.moverse()
        jugador.rotar()
        bullet = jugador.disparar() 
        if bullet:
            game.balas.add(bullet)
        screen.blit(jugador.surface, jugador.rect)
    for bala in game.balas:
        bala.shoot()
        screen.blit(bala.surface, bala.rect)
    for a_text in game.text:
        game.text.update()
        screen.blit(a_text.surface,a_text.rect)

#Revisa estados del jugador    
    game.checkLimiteJugadores() #No deja que se salga del margen de la ventana
    game.playerDied()


    pygame.display.update()
    #Tiempo
    game.setSecond()
    if(game.currentSecond % game.tiempoDeSpawn == 0 and game.secondPassed):
        game.crearAsteroides(4)
        game.secondPassed = False
    FramePerSec.tick(FPS)



#Estado del juego
    #Los meteoros cambian el target porque creo un nuevo player(ARREGLAR)
    #Vida (Arreglar) Las vidas siguen siendo 3 porque al crear un nuevo jugador se resetean
    #Niveles
    #Division de meteoros
    #Puntaje
    #Tipos de balas
    #Imagenes
    #Centro con agujero negro
    #Fxs
    #Ajustar colliders