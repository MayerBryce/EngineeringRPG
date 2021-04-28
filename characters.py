import pygame
from pygame.locals import *
import sys
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()

        #Position in the world
        self.vx = 0
        self.pos = vec((340,240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"

    def move(self):
        pass
    def update(self):
        pass
    def attack(self):
        pass
    def jump(self):
        pass

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()