
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, t=int(input('Введите толщину покрытия в см: '))):
        print(f'Масса асфальта - {self._length * self._width * 25 * t / 1000} т '
              f'(при 25 кг на 1 кв.м толщиной 1 см)')


road_1 = Road(int(input('Введите длину дорожного покрытия в м: ')),
              int(input('Введите ширину дорожного покрытия в м: ')))
road_1.asphalt_mass()
