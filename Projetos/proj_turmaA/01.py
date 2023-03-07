import pygame as pg
from pygame.locals import *

tela = pg.display.set_mode((1080,720),pg.RESIZABLE)

perso = pg.Surface((80,240))
perso.fill((255,255,255))
px, py = (50,500)

vila = pg.Surface((300,300))
vila.fill((165,42,42))



while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
        '''
            if event.key == K_UP or event.key == K_w:
                py -= 25
                
            if event.key == K_DOWN or event.key == K_s:
                py += 25
                
            if event.key == K_LEFT or event.key == K_a:
                px -= 25
                
            if event.key == K_RIGHT or event.key == K_d:
                px += 25
        '''
        if pg.key.get_pressed()[K_w]:
            py -= 25
            
        if pg.key.get_pressed()[K_s]:
            py += 25
            
        if pg.key.get_pressed()[K_a]:
            px -= 25
            
        if pg.key.get_pressed()[K_d]:
            px += 25

        tela.fill((0,0,0))
        tela.blit(perso,(px,py))
        tela.blit(vila,(600,200))
    pg.display.update()