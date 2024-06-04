# Игра Wordle

## написана на python с использованием pygame

### Итерация 1: создание игры и спрайта


Действия:

1. Создаем основной файл main.py, где импортируем pygame, прогружаем сцену и делаем бесконечный цикл 
2. Переносим из ранее созданной консольной игры wordle класс game и словарь wordle.txt
3. Создаем спрайт символа sym
4. В main создаем экземпляры game и sym и выводим в окно слово-квест Game().quest


### Итерация 2. Вывод слово-задание через спрайт по буквам

1. Получаем размер буквы (ширину и высоту ) в нашем примере условно 50
2. При помощи цикла for разбиваем слово по буквам и каждую букву выводим на экран
3. Меняем фон и выводим каждую букву с фоном (при необходимости удаляем лишние пробелы в words.txt)


### Итерация 3. Цветовые пары

1. В спрайте задаем цветовые пары (три кортежа, где цвет букв и фона для букв по умолчанию, для правильной буквы, для неправильной буквы)
2. Меняем шрифт выводимых букв на моноширный
3. Выводим все три варианта букв

### Итерация 4. Матрица игры

1. Создаем еще один класс - Matrix (матрица)
2. Задаем количество попыток и количество букв в слове
3. Создаем два списка, элементами которых будут списки: text_matr - матрица текста, color_matr - матрица цветов
4. Выводим текстовую матрицу в основном массиве через двойной for
5. По нажатию кнопки SPACE в первом (нулевом ) списке выводим слово-загадку

### Итерация 5. Переделка матрицы

1. color_matr - долой
2. у text_matr - структура, как у получаемого из game ответа (списка)
3. self.text_matr.append([[' ',' '],[' ',' '],[' ',' '],[' ',' '],[' ',' ']])


### Итерация 6. Проверка слова и вывод результата проверки по цветам

1. Добавить в __init__ класса Sym еще один параметр color_ - цветовая схема
2. Передавать в нее результат проверки из game, и в зависимости от результата выводить квадрат серым, красным или зеленым
3. В main по нажатию на Пробел реализуем проверку слова "Пират" (в консоль выводим задание)


### Итерация 7. создаем кнопки для работы с буквами

1. делаем pip install pygame_widgets
2. импортируем в проект ButtonArray из pygame_widgets.Button
3. создаем перебор букв через массив и заполняем текст каждой кнопки - это будет буква
4. реализуем функцию get_b(s) там будем манипулировать с буквами (пока делаем print(s))
5. создаем кортеж click_, где делаем обработчики для каждой из букв
6. этот обработчик выводим в onclick нашего buttonArray

### Итерация 8. пишем буквами слово в строке

1. Создаем переменные level (попытка), word (куда записываем слово) wordpos (позиция в слове), s
2. Переписываем функцию get_b, где букву пишем в word и в s
3. Записываем s в матрицу

### Итерация 9. Отправляем слово на проверку

1. Импортируем кнопку Button из pygame_widgets 
2. Создадим кнопку "Отправить", разместим ее чуть ниже алфавита
3. Создадим функцию Submit_check, где слово отправим на проверку
4. Исправим функцию набора букв - добавляться буква будет только если позиция <=4


### Итерация 10. удаление символа слева 
1. Создадим кнопку "Удалить символ слева", разместим ее чуть ниже алфавита
2. Создать ей функцию обработки
3. Протестировать ее