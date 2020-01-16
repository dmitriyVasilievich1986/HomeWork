# инициализация рейтинга
my_list = [7, 5, 3, 3, 2]

# ввод данных пользователя
my_list.append(int(input('Введите целое число от 0 до 10:')))

# сортировка списка и вывод данных
my_list.sort(reverse=True)
print(my_list)
