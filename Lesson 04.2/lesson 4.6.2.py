# импорт функции из библиотеки
from itertools import cycle

# инициализация списка
my_list = ['one', 'two', 'three']

# инициализация бесконечного формирования списка через функцию цикл
for a in cycle(my_list):
    print(a)
