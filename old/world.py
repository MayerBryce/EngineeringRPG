import pygame
from pygame.locals import *
import sys
import random

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("background.png")
        self.bgY = 0
        self.bgX = 0

    def render(self,displaysurface):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ground.png")
        self.rect = self.image.get_rect(center = (350, 350))

    def render(self,displaysurface):
        displaysurface.blit(self.image, (self.rect.x,self.rect.y))