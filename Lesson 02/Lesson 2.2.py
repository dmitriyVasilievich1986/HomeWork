# инициализация списка
list = []

# запускаем бесконечный цикл ввода новых данных в список
while 1:
    if len(list) > 0:
        print('Уже введенные данные:\n', list)
    print('\nДля завершения ввода данных введите \"end\"')
    new_data = input('Введите данные: ')
    if new_data == 'end':       # проверяем данные на выход из цикла
        break
    else:
        list.append(new_data)   # либо добавляем в список

# после выхода из цикла меняем данные в списке
print('\nВведенный список:\n', list)
for a in range(1, len(list), 2):
    temporary = list[a]     # создаем временную переменную
    list[a] = list[a - 1]
    list[a - 1] = temporary
print('\nИзмененный список:\n', list)
