import pygame as pg
from pygame.locals import *

pg.init()

tela = pg.display.set_mode((1080,720), pg.RESIZABLE)
#pg.display.set_caption('Teste')
#back = pg.image.load('ex_game/long_backg.jpg').convert_alpha()

lasKy = 'r'
obj = pg.image.load('ex_game/buba_dir.png')

#obj = pg.Surface((100,100))
#obj.fill((0,0,0))

posX = -50
posY = 400

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
            if event.key == K_UP or event.key == K_w:
                posY -= 50
                obj = pg.transform.scale_by(obj, 0.5)
            if event.key == K_DOWN or event.key == K_s:
                posY += 50
                obj = pg.transform.scale_by(obj, 2.0)
            if event.key == K_LEFT or event.key == K_a:
                posX -= 50
                if lasKy == 'r':
                    obj = pg.transform.flip(obj,True, False)
                    lasKy = 'l'
            if event.key == K_RIGHT or event.key == K_d:
                posX += 50
                if lasKy == 'l':
                    obj = pg.transform.flip(obj,True, False)
                    lasKy = 'r'

        tela.fill((144, 224, 239))
        #tela.blit(back, (0,0))
        tela.blit(obj, (posX,posY))
        print(posX,posY)

    pg.display.update()