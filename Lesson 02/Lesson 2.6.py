# инициализация объектов
item = {'Название': '', 'Цена': '', 'Количество': '', 'Ед. измерений': ''}
goods = []
count = 1

# старт бесконечного цикла ввода данных о товаре
while 1:
    print('\nДля завершения введите \"end\"')
    name = input('Введите название товара: ')
    if name.lower() == 'end':
        break
    else:
        item['Название'] = name.title()
    while 1:
        try:
            item['Цена'] = round(float(input('Введите цену товара: ')), 2)
            break
        except:
            print('Введено неверное значение\n')
    while 1:
        try:
            item['Количество'] = int(input('Введите количество товара: '))
            break
        except:
            print('Введено неверное значение\n')
    item['Ед. измерений'] = input('Введите еденицы измерения количества товара: ')
    goods.append((count, item.copy()))
    count += 1

# список введенных товаров
print('\nВведенные товары:')
for a in goods:
    print(a)

# инициализация словаря статистики товаров
goods_statistics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед. измерений': []}
for a in goods_statistics.keys():
    for b in goods:
        if a in b[1].keys():
            goods_statistics[a].append(b[1][a])

# вывод данных о товарах
print('\nСтатистика:')
for a in goods_statistics.keys():
    print(a, goods_statistics[a])
