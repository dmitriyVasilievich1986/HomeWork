# инициализация функции проверки целого числа
def int_checkout(parameters):
    output = None
    while 1:
        try:
            output = int(input(parameters))
        except ValueError:
            print('Введите целое число')
        if output is not None:
            return output


# инициализация функции сложения максимальных чисел
def my_func(set_value):
    set_value.remove(min(set_value[0], set_value[1], set_value[2]))  # удаляем из списка минимальное число
    print(f'Сумма двух больших значений равна: {set_value[0]}+{set_value[1]}={set_value[0] + set_value[1]}')


# инициализация данных
my_set = []
cycle = 1

# ввод данных от пользователя
while cycle < 4:
    my_set.append(int_checkout(f'Введите {cycle} число: '))
    cycle += 1

# вызов нашей функции
my_func(my_set)
