# инициализация функции для преобразования текста в заголовок
def int_func(text):
    return str(text).title()


# инициалзация функции для разбития текста на слова, вызов основной функции
def split_text(text):
    array_text = str(text).split()
    output = ''
    for a in range(0, len(array_text)):
        output += int_func(array_text[a]) + ' '
    return output


# инициалзация бесконечного цикла ввода строки слов
while 1:
    print(split_text(input('Введите через пробел слова: ')) + '\n')
