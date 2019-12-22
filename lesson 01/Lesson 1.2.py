# ввод данных
seconds = int(input('Введите время в секундах: '))
# перевод в часы и минуты
hours = int(seconds/360)
minutes = int((seconds-hours*360)/60)
# вывод результата на экран
print(f'Введенные {seconds} секунд соответсвуют:')
print(int(seconds/360), int((seconds-hours*360)/60), int((seconds-hours*360)-(60*minutes)), sep=":")
