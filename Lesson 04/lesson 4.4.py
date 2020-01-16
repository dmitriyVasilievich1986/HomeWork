# инициализация списка чисел
my_list = [1, 103, 15, 22, 8, 0, 8, 15, 22, 103, 22, 17, 18]


# инициализация генератора на основе списка
def generator(using_list):
    for a in range(0, len(using_list)):
        if a == using_list.index(using_list[a]):    # если это первое вхождение в списке,
            yield using_list[a]                     # то добавляем значение


# инициализация списка через генератор
result_list = generator(my_list)
# вывод списка
for a in result_list:
    print(a)
