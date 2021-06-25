import pygame 
from pygame.locals import *

class Bala(pygame.sprite.Sprite): #Verificar si se toco un asteroide

    def __init__(self,x,y,direction):
        super().__init__()  #Constructor clase madre

        #Logica
        self.size = 10
        self.range = 30
        self.speed = 8
        self.direction = direction
        self.pos = pygame.Vector2(x,y)

        #Graficos
        self.color = (255,0,0)
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect(center=(x, y))
        

    def shoot(self):
        self.pos -= self.direction*self.speed
        self.rect.center = self.pos
        self.range -= 1
        if(self.range == 0):
            self.kill()

    def morir(self):
        self.kill()
