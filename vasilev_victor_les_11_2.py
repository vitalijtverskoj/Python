class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите делимое: '))
b = int(input('Введите делитель:'))

try:
    if b == 0:
        raise MyException('Деление на ноль недопустимо')
    res = a / b
except MyException as err:
    print('Деление на ноль не допустимо')
else:
    print(f'Результат - {res}')
