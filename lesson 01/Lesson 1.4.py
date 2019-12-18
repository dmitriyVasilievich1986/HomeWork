# ввод числа
digit = int(input('Введите целое число:'))

# инициализация переменных
curent_digit = 0        # временная переменная макс
save = digit            # переменная для вывода в конце

# цикл деления нашей цифры
while digit > 0:
    if curent_digit < (digit % 10):
        curent_digit = (digit % 10)
    if curent_digit == 9:               # больше 9 не может быть
        break                           # выход из цикла
    digit = int(digit/10)
    
# вывод полученной цифры
print(f'Из введенного числа {save}, самая болшая цифра: {curent_digit}')
