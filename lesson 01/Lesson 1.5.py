# ввод данных
incom = float(input('Введите прибыль компании: '))
outcom = float(input('Введите убыток компании: '))

# определение прибыльности компании
if incom >= outcom:
    print('\nКомпания сработала в прибыль')
    print(f'Текущая прибыль составила: {incom - outcom:.2f}')
else:
    print('\nКомпания сработала в убыток')
    print(f'Текущий убыток составил: {outcom - incom:.2f}')

# ввод кол-ва сотрудников
employe_count = int(input('\nВведите количество сотрудников: '))

# расчет прибыли на сотрудника
print(f'В расчете на каждого сотрудника прибыль составляет: {incom / employe_count:.2f}')
