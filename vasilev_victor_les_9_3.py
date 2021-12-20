class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_full_income(self):
        print(f'{sum(self._income.values())}')


worker_1 = Position(input('Введите имя сотрудника: '),
                    input('Введите фамилию сотрудника: '),
                    input('Введите должность сотрудника:'),
                    int(input('Введите оклад сотрудника: ')),
                    int(input('Введите премию сотрудника: ')))
worker_1.get_full_name()
worker_1.get_full_income()
