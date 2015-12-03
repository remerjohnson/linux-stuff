import pygame, sys
from pygame.locals import *

pygame.init()

# frames per second setting
FPS = 60
fpsClock = pygame.time.Clock()

#set up the window
DISPLAYSURF = pygame.display.set_mode((900,600), 0, 32)
pygame.display.set_caption('Dungeon of Ryan')

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# variables we'll have to call
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Welcome to the Dungeon!', True, GREEN, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400, 450)

bardImg = pygame.image.load('Gimble72.jpg')
bardx = 10
bardy = 10
direction = 'right'

# main game loop
while True: 
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    if direction == 'right':
        bardx += 5
        if bardx == 300:
            direction = 'halt'
    elif direction == 'halt':
        bardx += 0
    
    DISPLAYSURF.blit(bardImg, (bardx, bardy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
        