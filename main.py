import pygame


pygame.init()

W, H = 600, 600

sc = pygame.display.set_mode((W,H) )
pygame.display.set_caption("Wordle")

from game import Game

curr_game=Game()

from sym import Sym

s1=Sym(curr_game.quest, 300,300 )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()




    sc.fill((0,0,0))
    sc.blit(s1.text, s1.rect)
    pygame.display.update()