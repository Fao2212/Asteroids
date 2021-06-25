import pygame
from pygame.locals import *

class Asteroide(pygame.sprite.Sprite): #Collider pendiente
    def __init__(self,target):
        super().__init__() #Constructor clase madre

        #Graficos
        self.color = (82, 45, 17)
        self.size = 20
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.color)#Color

        #Logica
        self.speed = 1
        self.rect = self.surface.get_rect()
        self.pos = pygame.Vector2(self.rect.x,self.rect.y)
        self.target = target
       
    def dividirse():#Tamano aparece segun el nivel y se va encogiendo
        pass

    def moverse(self): #El asteroide tiene que moverse hacia el centro/jugador  Puede usarse un LERP
        if not self.rect.colliderect(self.target.rect):#Creo que puede cambiar a un proceso mas simple
            if self.pos.x > self.target.pos.x:
                self.pos.x -= self.speed
            else:
                self.pos.x += self.speed
            if self.pos.y > self.target.pos.y:
                self.pos.y -= self.speed
            else:
                self.pos.y += self.speed
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            self.target.morir()
            self.kill()
        
    def bulletCollision(self,bullets):#Para balas que atraviesan meteoritos entonces se pasa una funcion que no destruye la bala        
        if(pygame.sprite.spritecollide(self,bullets,True)):
            self.kill()


    def setPos(self,vector):
        self.pos = vector
