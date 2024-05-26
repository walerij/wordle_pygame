import pygame
class Sym(pygame.sprite.Sprite):
    def __init__(self, text,x,y, color_):
        self.default_color = ((0,0,0),(196, 193, 192))
        self.correct_color = ((0,0,0),(45, 179, 39))
        self.wrong_color = ((0,0,0),(166, 28, 28))
        if (color_ == ''):
            self.textcolor = self.default_color[0]
            self.bgcolor = self.default_color[1]
        elif (color_ == 'green'):
            self.textcolor = self.correct_color[0]
            self.bgcolor = self.correct_color[1]
        elif (color_ == 'red'):
            self.textcolor = self.wrong_color[0]
            self.bgcolor = self.wrong_color[1]
        #self.textcolor =self.default_color[0]
        #self.bgcolor = self.default_color[1]
        self.font = pygame.font.SysFont("courier", 42)
        self.text = self.font.render(text, True,  self.textcolor, self.bgcolor)
        self.rect = self.text.get_rect(center=(x, y))

    def update(self, color_,  *args):
        if (color_==''):
            self.textcolor = self.default_color[0]
            self.bgcolor = self.default_color[1]
        elif  (color_=='green'):
            self.textcolor = self.correct_color[0]
            self.bgcolor = self.correct_color[1]
        elif  (color_=='red'):
            self.textcolor = self.wrong_color[0]
            self.bgcolor = self.wrong_color[1]

        self.text = self.font.render(self.text, True, self.textcolor, self.bgcolor)