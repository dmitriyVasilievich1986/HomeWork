# инициализация функции проверки целого числа
def int_checkout(parameters):
    output = None
    while 1:
        try:
            output = int(input(parameters))
        except ValueError:
            print('Введите целое число')
        if output is not None:
            return output


# инициализация функции вывода данных пользователя
def user_parameters(user_name, user_surname, user_age, user_city, user_telephone, user_email):
    print(f'Имя: {user_name.title()} \tФамилия: {user_surname.title()} \tГод рождения: {user_age} \t'
          f'Город проживания: {user_city.title()} \tТелефон: {user_telephone} \t'
          f'Адрес электронной почты: {user_email}')


# запрос данных от пользователя
name = str(input('Введите имя пользователя: '))
surname = str(input('Введите фамилию пользователя: '))
age = int_checkout('Введите год рождения пользователя: ')
city = str(input('Введите город проживания пользователя: '))
telephone = int_checkout('Введите номер телефона пользователя: ')
email = str(input('Введите адрес электронной почты пользователя: '))

# вызов функции
user_parameters(user_age=age, user_name=name, user_surname=surname, user_city=city,
                user_email=email, user_telephone=telephone)
