# импортирование функции из библиотеки
from functools import reduce


# инициализация генератора факториала
def fibo_gen():
    for x in range(1, 16):
        yield reduce((lambda item1, item2: item1 * item2), [a for a in range(1, x + 1)])    # хмм получилось довольно сложно


# вызов функции через цикл
for el in enumerate(fibo_gen(), 1):
    print(el)
