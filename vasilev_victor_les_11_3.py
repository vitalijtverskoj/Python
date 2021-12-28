class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


req_list = []
while True:
    try:
        req = input('Введите данные: ')
        if req.isdigit() is True:
            req_list.append(req)
        elif req == 'stop':
            break
        elif type(req) == str:
            raise MyException('Введите число!!!')
    except MyException as err:
        print(err)

print(req_list)
