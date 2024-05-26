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
            #print(matrix.text_matr[i][j])
            s1 = Sym(matrix.text_matr[i][j][0], W / 3 + pos_w, H / 6+pos_h, matrix.text_matr[i][j][1] )
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



    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        print(curr_game.quest)
        s = []
        word = 'пират'
        s=curr_game.check(word)

        matrix.text_matr[0]= s

    pressed = pygame.key.get_pressed()



    pygame.display.update()