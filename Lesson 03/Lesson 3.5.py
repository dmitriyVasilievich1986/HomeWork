# инициализация функции подсчета суммы значений
def print_summ(numbers):
    all_numbers = numbers[0]
    count = f'Сумма всех значений: {numbers[0]}'
    if len(numbers) > 1:
        for a in range(1, len(numbers)):
            count += f' + {numbers[a]}'
            all_numbers += numbers[a]
    count += f' = {all_numbers}'
    print(count)
    print()


# инициализация данных
numbers = []
cycle = True


# вход в цикл ввода данных от полдьзователя
while cycle:
    print('Для завершения введите "q"')
    array_of_numbers = input('Введите числа через пробел: ')    # ввод чисел через пробел
    for a in array_of_numbers.split():
        if a == 'q':            # проверка на символ выхода
            cycle = False       # выход
            break
        try:
            numbers.append(int(a))      # проверка на соответствие чисел
        except ValueError:
            print(f'Недопустимое значение: {a}')    # если не число не добавляем
    if len(numbers) > 0:
        print_summ(numbers)     # вывод суммы чисел


