import pygame
#from pygame.locals import *
import sys
import random
#maybe look into tkinter GUI

pygame.init()

vec = pygame.math.Vector2
HEIGHT = 480
WIDTH = 640
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Engineering RPG")

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

while True:
       
    for event in pygame.event.get():
        # Will run when the close window button is clicked    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
             
        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
 
        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
              pass