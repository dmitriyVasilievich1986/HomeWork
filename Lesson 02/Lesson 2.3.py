# инициализация списка и словаря
seasons_list = list(range(0, 12))
seasons_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

# теперь словарь элегантно преращается в список)
for a in seasons_dict.keys():
    for b in seasons_dict[a]:
        seasons_list[b - 1] = a

# старт бесконечного цикла ввода данных пользователя
while 1:
    try:
        month = int(input('Введите месяц от 1 до 12: '))
        if month >= 1 and month <= 12:      # если все хорошо выходим из цикла
            break
        else:
            print('Введите число от 1 до 12\n')     # обработка
    except:                                         # исключений
        print('Введите целое число\n')

# перебор словаря на совпадение. может не совсем как в задании но так Сильно проще)
print('\nРеализация через словарь:')
for a in seasons_dict.keys():
    for b in seasons_dict[a]:
        if month == b:
            print(month, '-', a)

# просто вывод значения из списка по индексу
print('\nРеализация через список:')
print(month, '-', seasons_list[month])

