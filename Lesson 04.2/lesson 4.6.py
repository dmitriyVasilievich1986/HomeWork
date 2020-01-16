# импортирование функций из библиотек
from itertools import count
from sys import argv

# инициализация переменных
name, start_position = argv

# вывод бесконечного списка через функцию каунт
for a in count(int(start_position)):
    print(a)
