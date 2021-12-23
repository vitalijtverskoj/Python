class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join([f'{j}' for j in i]) for i in self.matrix)

    def __add__(self, other):
        m = []
        for i in range(len(self.matrix)):
            m.append([])
            for j in range(len(self.matrix[0])):
                m[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(m)


matrix_1 = Matrix([[3, 4, 1, 6, 7], [4, 8, 7, 5, 8], [9, 1, 4, 9, 2]])
matrix_2 = Matrix([[6, 5, 8, 3, 2], [2, 1, 6, 3, 2], [4, 2, 4, 2, 1]])
print(matrix_1)
print('-' * 10)
print(matrix_2)
print('-' * 10)
print(matrix_1 + matrix_2)
