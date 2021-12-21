class Stationery:
    def __init__(self, t='Канцелярская принадлежность'):
        self.title = t

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')


class Marker(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')


stat = Stationery()
pen = Pen('Erich Krause')
pencil = Pencil('KOH-I-NOOR')
marker = Marker('Markal')

stat_list = [stat, pen, pencil, marker]

for i in stat_list:
    i.draw()
