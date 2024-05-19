import pygame


pygame.init()

W, H = 600, 800

sym_w, sym_h = 30,60

sc = pygame.display.set_mode((W,H) )
pygame.display.set_caption("Wordle")

from game import Game

curr_game=Game()

from sym import Sym

s1 = None
# Sym("ш", W/2,H/4 )

from matrix import Matrix

matrix = Matrix()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()




    sc.fill((0,0,0))
    pos_w = 0
    pos_h = 0
    for i in range(6):
        for j in range(5):
            s1 = Sym(matrix.text_matr[i][j], W / 3 + pos_w, H / 6+pos_h )
            sc.blit(s1.text, s1.rect)
            pos_w += sym_w
        pos_h += sym_h
        pos_w = 0


    """"
        for i in curr_game.quest:
        s1 = Sym(i, W/3+pos,H/4 )
        sc.blit(s1.text, s1.rect)
        pos += sym_w
    
    """

    #print(s1.rect.width, s1.rect.height)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        s = []
        for i in curr_game.quest:
            s.append(i)
        matrix.text_matr[0] = s



    pygame.display.update()