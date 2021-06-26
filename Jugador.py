from Bala import Bala
import pygame
from pygame import Vector2, surface
from pygame.locals import *
import math
import sys

class Jugador(pygame.sprite.Sprite):
    def __init__(self):#Ubicacion
       super().__init__() #Constructor clase madre

       #Logica
       self.lives = 3
       self.size = 30
       self.angle = 0
       self.rotationSpeed = 3
       self.speed = 5
       self.cooldown = 400 
       self.alive = True
       self.lastCooldown = -sys.maxsize

       #Grafica
       self.surface = pygame.Surface((30, 30))
       self.original = self.surface
       self.rect = pygame.draw.polygon(self.surface, (255,0,0), ((0, 30), (15, 0), (30, 30)))
       self.pos = pygame.Vector2(self.rect.x,self.rect.y)
       self.front = self.getFront()
       
    def getFront(self):#Calcula una tupla(x,y) con el seno y el coseno para marcar el frente de la nave 
        angle = math.radians(self.angle)
        x = math.cos(angle)
        y = math.sin(angle)
        return pygame.Vector2(y,x)#Los utiliza al contrario porque la nave apunta hacia arrina 90grados

    def getPos(self):
        return pygame.Vector2(self.rect.x,self.rect.y)

    def reaparecer(self):
        self.surface = pygame.Surface((30, 30))
        self.original = self.surface
        self.rect = pygame.draw.polygon(self.surface, (255,0,0), ((0, 30), (15, 0), (30, 30)))
        self.front = self.getFront()
        self.alive = True

    def moverse(self):#Aumenta la pos con el frente(direccion) y con la velocidad
        if self.alive:
            pressed_keys = pygame.key.get_pressed()
            if(pressed_keys[K_UP] or pressed_keys[K_w]):
                self.pos -= self.front*self.speed
            if(pressed_keys[K_DOWN] or pressed_keys[K_s]):
                self.pos += self.front*self.speed
            self.rect.center = self.pos
        
    
    def rotar(self):#Aumenta el valor del angulo, recalcula el frente y reposiciona el rect
        if self.alive:
            pressed_keys = pygame.key.get_pressed()
            if(pressed_keys[K_LEFT] or pressed_keys[K_a]):#Positivos
                self.angle += self.rotationSpeed
                self.surface = pygame.transform.rotate(self.original,self.angle)
                self.rect = self.surface.get_rect()
                self.rect.center = self.pos
                self.front = self.getFront()
            if(pressed_keys[K_RIGHT] or pressed_keys[K_d]):#Negativos
                self.angle -= self.rotationSpeed
                self.surface = pygame.transform.rotate(self.original,self.angle)
                self.rect = self.surface.get_rect()
                self.rect.center = self.pos
                self.front = self.getFront()
            

    def morir(self): #Sale de la lista, disminuye la vida y lo pone como muerto
        self.alive = False
        self.lives -= 1
        self.kill()

    def disparar(self):#A disparar cada vez que se toque espacio respetando el cooldown
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_SPACE] and self.cooldown < pygame.time.get_ticks() - self.lastCooldown and self.alive):
            x,y = self.rect.center
            self.lastCooldown = pygame.time.get_ticks()
            return Bala(x,y,self.front)

    def setPos(self,x,y):#Pone la nave en una posicion especifica(Usado para coloca en el centro)
        self.pos = pygame.Vector2(x,y)

