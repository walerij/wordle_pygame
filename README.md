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