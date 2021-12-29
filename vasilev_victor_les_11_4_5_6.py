class OfEqStock:  # склад
    def __init__(self):
        self.storage = {}

    def store(self, equip):
        self.storage.setdefault(equip.tip(), []).append(equip)


class OfficeEquipment:  # создание оргтехники
    def __init__(self, brand):
        self.tip = self.__class__.__name__
        self.brand = brand

    def tip(self, count=1):
        return f'{self.tip}'

    def __repr__(self):
        return f'{self.brand}'


class Printer(OfficeEquipment):  # создание принтера
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def __repr__(self):
        return f'{self.brand} {self.model}'


class Scanner(OfficeEquipment):  # создание сканера
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def __repr__(self):
        return f'{self.brand} {self.model}'


class Copier(OfficeEquipment):  # создание копера
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def __repr__(self):
        return f'{self.brand} {self.model}'


stock = OfEqStock()
printer = Printer('HP', 110)
stock.store(printer)
scanner = Scanner('Samsung', 2)
stock.store(scanner)
copier = Copier('Xerox', 100)
stock.store(copier)
print(stock.storage)
