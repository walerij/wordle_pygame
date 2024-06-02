import pygame, pygame_widgets

from pygame_widgets.button import ButtonArray

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

#кнопки алфавита
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

textList = []
clickList = []

def get_b(s):
    print(s)


for i in alf:
    #print(i)
    textList.append(i)
    tmp=str(i)
    #clickList.append(lambda: get_b(tmp))





click_= (
lambda: get_b("a"),
lambda: get_b("б"),
lambda: get_b("в"),
lambda: get_b("г"),
lambda: get_b("д"),
lambda: get_b("е"),
lambda: get_b("ё"),
lambda: get_b("ж"),
lambda: get_b("з"),
lambda: get_b("и"),
lambda: get_b("й"),
lambda: get_b("к"),
lambda: get_b("л"),
lambda: get_b("м"),
lambda: get_b("н"),
lambda: get_b("о"),
lambda: get_b("п"),
lambda: get_b("р"),
lambda: get_b("с"),
lambda: get_b("т"),
lambda: get_b("у"),
lambda: get_b("ф"),
lambda: get_b("х"),
lambda: get_b("ц"),
lambda: get_b("ч"),
lambda: get_b("ш"),
lambda: get_b("щ"),
lambda: get_b("ъ"),
lambda: get_b("ы"),
lambda: get_b("ь"),
lambda: get_b("э"),
lambda: get_b("ю"),
lambda: get_b("я"),

)
text_ = tuple(textList)
#click_ = tuple(clickList)



buttonArray  = ButtonArray(
    sc,
    50,  # X-coordinate
    500,  # Y-coordinate
    400,  # Width
    200,  # Height
    (11, 3),  # Shape: 2 buttons wide, 2 buttons tall
    border=2,  # Distance between buttons and edge of array
    texts=text_,  # Sets the texts of each button (counts left to right then top to bottom)
    # When clicked, print number
    onClicks= click_


)



while True:

    events = pygame.event.get()
    for event in events:
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

    pygame_widgets.update(events)

    pygame.display.update()