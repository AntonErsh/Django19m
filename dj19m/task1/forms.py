from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, label="Повторите пароль")
    age = forms.CharField(max_length=3, label='Введите свой возраст')


def is_valid_data(username: str, password: str, repeat_password: str, age: str, users, info: dict) -> bool:
    """
    Проверка данных для регистрации пользователя
    :param username:
    :param password:
    :param repeat_password:
    :param age:
    :param users: Список объектов пользователей QuerySet из базы данных
    :param info: Словарь для записи сообщений об ошибках
    :return: True or False
    """
    def __is_in_users(users, username: str) -> bool:
        """
        Эта функция проверяет наличие в базе данных текущего username
        :param users: Список объектов пользователей QuerySet из базы данных
        :param username: Вводимое имя пользователя для проверки наличия его в базе данных
        :return: True - если username нет в базе данных. Иначе - False
        """
        for buyer in users:
            if buyer.name == username:
                return False
        return True

    if password == repeat_password and age >= '18' and __is_in_users(users, username):
        return True

    elif password != repeat_password:
        info.update({'error': 'Пароли не совпадают'})
        return False

    elif age < '18':
        info.update({'error': 'Вы должны быть старше 18'})
        return False

    elif not __is_in_users(users, username):
        info.update({'error': 'Пользователь уже существует'})
        return False
