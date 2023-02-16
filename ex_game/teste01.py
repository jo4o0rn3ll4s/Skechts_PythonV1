import pygame as pg
from pygame.locals import *

pg.init()

tela = pg.display.set_mode((1080,720))
pg.display.set_caption('Teste')

obj = pg.Surface((100,100))
#obj.fill((255,255,255))

posX = posY = 50

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
            if event.key == K_UP:
                posY -= 50
            if event.key == K_DOWN:
                posY += 50
            if event.key == K_LEFT:
                posX -= 50
            if event.key == K_RIGHT:
                posX += 50
                
        tela.fill((255,255,255))
        tela.blit(obj, (posX,posY))
    pg.display.update()