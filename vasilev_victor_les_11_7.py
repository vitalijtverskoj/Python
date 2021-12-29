class MyComplex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'{self.real} + {self.imag}j'

    def __add__(self, other):
        sum_real = self.real + other.real
        sum_imag = self.imag + other.imag
        return f'{sum_real} + {sum_imag}j'

    def __mul__(self, other):
        mul_real = self.real * other.real - self.imag * other.imag
        mul_imag = self.real * other.imag + other.real * self.imag
        return f'{mul_real} + {mul_imag}j'


z_1 = MyComplex(5, 6)
z_2 = MyComplex(1, 1)
print(z_1 + z_2)
print(z_1 * z_2)
