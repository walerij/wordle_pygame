from sym import Sym

class Matrix():
    def __init__(self):
        self.x = 6 #попытки
        self.y = 5 #буквы
        self.text_matr = []

        self.i=0
        while self.i < self.x:
            self.text_matr.append([[' ',''],[' ',''],[' ',''],[' ',''],[' ','']])

            self.i=self.i+1



