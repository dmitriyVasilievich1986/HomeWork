# ввод строки
stringa = input('Введите строку: ')

# разделение строки на данные из списка
new_list = stringa.split(' ')

# вывод данных из списка с их нумерацией
for a in enumerate(new_list, 1):
    print(a[0], '-', a[1][0:10])
