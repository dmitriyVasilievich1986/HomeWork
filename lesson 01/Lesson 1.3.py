# ввод числа
digit_n = input('введите число:')           # оставляем в формате string

# добавление новых переменных из введенной переменной
digit_nn = int(digit_n+digit_n)             # сразу переводим
digit_nnn = int(digit_n+digit_n+digit_n)    # в integer

# вывод результата
print(f'{digit_n}+{digit_nn}+{digit_nnn}={int(digit_n)+digit_nn+digit_nnn}')