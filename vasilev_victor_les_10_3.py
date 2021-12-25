class Cell:
    def __init__(self, nuc):
        self.nuc = nuc

    def make_order(self, rows):
        return '\n'.join(['@' * rows for i in range(self.nuc // rows)]) + '\n' + '@' * (self.nuc % rows)

    def __str__(self):
        return f'{self.nuc}'

    def __add__(self, other):
        return Cell(self.nuc + other.nuc)

    def __sub__(self, other):
        return Cell(self.nuc - other.nuc) if self.nuc - other.nuc > 0 else 'Нельзя вычесть'

    def __mul__(self, other):
        return Cell(self.nuc * other.nuc)

    def __floordiv__(self, other):
        return Cell(self.nuc // other.nuc)


cell_1 = Cell(20)
cell_2 = Cell(13)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(5))
