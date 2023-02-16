import pygame as pg
from pygame.locals import *

pg.init()

tela = pg.display.set_mode((1080,720))
#pg.display.set_caption('Teste')
back = pg.image.load('ex_game/backg.jpg').convert_alpha()
back = pg.transform.scale(back, (1080,720))


obj = pg.image.load('ex_game/buba_dir.jpg')
#obj = pg.Surface((100,100))
#obj.fill((0,0,0))

posX = -50
posY = 450

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
                obj = pg.image.load('ex_game/buba_esq.png')
            if event.key == K_RIGHT:
                posX += 50
                obj = pg.image.load('ex_game/buba_dir.jpg')
       
        tela.blit(back, (0,0))
        tela.blit(obj, (posX,posY))
        print(posX,posY)

    pg.display.update()