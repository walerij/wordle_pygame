import pygame


class Btp(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
