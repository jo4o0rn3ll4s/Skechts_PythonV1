import pygame as pg
from pygame.locals import *

tela = pg.display.set_mode((1080,720),pg.RESIZABLE)

perso = pg.image.load('Projetos/proj_turmaA/sprites.png').conve
perso_ani = []
rec_perso = perso.get_rect()
rec_perso.x = 50
rec_perso.y = 500

vila = pg.Surface((300,300))
vila.fill((165,42,42))
rec_vila = vila.get_rect()
rec_vila.x = 600
rec_vila.y = 200

time = pg.time.Clock()

spt_x = 32
spt_y = 32

for line in range(perso.get_height()//spt_y):
    for col in range(perso.get_width()//spt_x):
        x = col * spt_x
        y = line * spt_y
        trans = perso.subsurface(pg.Rect(x, y, spt_x, spt_y))
        perso_ani.append(trans)

while True:

    time.tick(30)

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
        if pg.key.get_pressed()[K_w]:
            rec_perso.y -= 25
            
        if pg.key.get_pressed()[K_s]:
            rec_perso.y += 25
            
        if pg.key.get_pressed()[K_a]:
            rec_perso.x -= 25
            
        if pg.key.get_pressed()[K_d]:
            rec_perso.x += 25
            for i in range(8,12):
                tela.blit(perso_ani[i])

        if rec_perso.colliderect(rec_vila):
            print('colidiu')

        tela.fill((0,0,0))
        tela.blit(vila,rec_vila)
        tela.blit(perso_ani[0],rec_perso)
        
    pg.display.update()