import pygame


pygame.init()

W, H = 600, 600

sym_w, sym_h = 50,50

sc = pygame.display.set_mode((W,H) )
pygame.display.set_caption("Wordle")

from game import Game

curr_game=Game()

from sym import Sym

s1 = None
# Sym("ш", W/2,H/4 )

#50 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()




    sc.fill((0,0,0))
    pos = 0
    for i in curr_game.quest:
        s1 = Sym(i, W/3+pos,H/4 )
        sc.blit(s1.text, s1.rect)
        pos += sym_w
    #print(s1.rect.width, s1.rect.height)
    pygame.display.update()