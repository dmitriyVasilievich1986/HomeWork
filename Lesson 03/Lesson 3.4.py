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


# инициализация функции возведения в степень
def multiplication(x, y):
    print(f'{x} в степени {y} равен {x**y}\n')
    result = x
    for a in range(y, 1):   # через цикл for
        result /= x
    print(f'Реализация через цикл: {result}')


# инициализация данных
x = 0
y = 0

# ввод данных от пользователя
while x <= 0:
    x = int_checkout("Введите целое положительное число: ")
print()
while y >= 0:
    y = int_checkout("Введите целое отрицательное число: ")

# вызов функции
multiplication(x, y)
