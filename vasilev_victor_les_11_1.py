class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod  # должен извлекать число, месяц, год и преобразовывыть в int
    def cm(cls, data):
        day, month, year = [int(n) for n in data.split('-')]
        return cls(day, month, year)

    @staticmethod  # должен проводить валидацию числа, месяца и года
    def sm(obj):
        if 0 < obj.day <= 31 and 0 < obj.month <= 12 and 0 <= obj.year <= 2022:
            return f'день - {obj.day}, месяц - {obj.month}, год - {obj.year}'
        else:
            return 'Некорректная дата'


data_1 = Date.cm('12-12-1995')
print(Date.sm(data_1))
