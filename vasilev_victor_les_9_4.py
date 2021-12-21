from random import choice, randint


class Car:
    direction = ['север', 'запад', 'восток', 'юг']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p

    def show_speed(self):
        return f'Скорость автомобиля: {self.name} - {self.speed}.'

    def go(self):
        print(f'Автомобиль: {self.name} поехал.')

    def stop(self):
        print(f'Автомобиль: {self.name} остановился.')

    def turn(self):
        print(f'Автомобиль: {self.name} повернул на {choice(self.direction)}.')


class TownCar(Car):
    def show_speed(self):
        return f'У автомобиля: {self.name} скорость превышена! ' \
               f'({self.speed}!!!)' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f'У автомобиля: {self.name} скорость превышена! ' \
               f'({self.speed}!!!)' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)


police_car = PoliceCar('"Полиция!"', 'белый', randint(0, 120))
work_car = WorkCar('"Фура"', 'синий', randint(0, 120))
sport_car = SportCar('"ЛАМБА"', 'ораньжевый', randint(0, 120))
town_car = TownCar('"Матиз"', 'красный', randint(0, 120))

cars = [police_car, work_car, sport_car, town_car]


for i in cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
