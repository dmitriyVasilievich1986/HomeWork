# инициализация списка чисел
just_a_list = [1, 10, 25, 48, 7, 0, 29]


# инициализация функции генератора списка
def generator(using_list):
    for a in range(1, len(using_list)):   # начало со 2 позиции
        if using_list[a] > using_list[a - 1]:
            yield using_list[a]


# инициализация списка через генератор
list_result = generator(just_a_list)
# вывод на экран получившегося списка
for a in list_result:
    print(a)
