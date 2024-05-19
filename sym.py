import pygame
class Sym(pygame.sprite.Sprite):
    def __init__(self, text,x,y):
        self.textcolor =(130, 207, 29)
        self.bgcolor = (0,0,0)
        self.font = pygame.font.Font(None, 72)
        self.text = self.font.render(text, True,  self.textcolor, self.bgcolor)
        self.rect = self.text.get_rect(center=(x, y))

    def update(self, *args):
        self.text = self.font.render(self.text, True, self.textcolor, self.bgcolor)