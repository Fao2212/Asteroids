import pygame
from pygame.locals import *

class Asteroide(pygame.sprite.Sprite): #Collider pendiente
    def __init__(self,target,multiplier):
        super().__init__() #Constructor clase madre
        self.multiplier = multiplier

        #Graficos
        self.color = (82, 45, 17)
        self.size = 20
        self.surface = pygame.Surface((self.size*self.multiplier, self.size*self.multiplier))
        self.surface.fill(self.color)#Color

        #Logica
        self.speed = 1/self.multiplier
        self.rect = self.surface.get_rect()
        self.pos = pygame.Vector2(self.rect.x,self.rect.y)
        self.target = target
        self.direccion = pygame.Vector2(0,0)
        self.explosionForce = 8
        self.explosion = False
        self.explosionDistance = 60
        self.friccion = 1

    def dividirse(self):#Tamano aparece segun el nivel y se va encogiendo
        if self.multiplier > 1:
            grupos = self.groups()
            a1 = Asteroide(self.target,self.multiplier-1)
            a2 = Asteroide(self.target,self.multiplier-1)
            a1.setPos(self.pos)
            a2.setPos(self.pos)
            a1.explode(pygame.Vector2(-1,1))#Se puede aleatorizar la direccion de la explosion
            a2.explode(pygame.Vector2(1,-1))
            grupos[0].add(a1,a2)
        self.kill()
    
    def explode(self,direccion):
        self.explosion = True
        self.direccion = direccion

    def moverse(self): #El asteroide tiene que moverse hacia el centro/jugador
        
        if not self.explosion:
            if not self.rect.colliderect(self.target.rect):
                direction = (self.target.pos-self.pos).normalize() #Direccion de un vector
                self.pos += direction*self.speed
                self.rect.center = self.pos
            else:
                self.target.morir()
                self.kill()
        else:
            if self.explosionDistance > 0:
                self.pos =  self.pos + (self.direccion*self.explosionForce)/self.friccion   #Se puede aumentar la friccion para una mejor explosion
                self.rect.center = self.pos                                 
                self.explosionDistance -= self.explosionForce               
                self.friccion += 0.4
            else:
                self.explosion = False
        
    def bulletCollision(self,bullets):#Para balas que atraviesan meteoritos entonces se pasa una funcion que no destruye la bala        
        if(pygame.sprite.spritecollide(self,bullets,True)):
            self.dividirse()


    def setPos(self,vector):
        self.pos = vector

    
