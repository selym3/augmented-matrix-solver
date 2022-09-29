def is_number(x):
    return isinstance(x, (int, float))

class Row:

    def __init__(self, values):
        self.values = values
        self.data = [0 for _ in range(values)]


    def __str__(self):
        return str(self.data)

    def __getitem__(self, index):
        if index < 0 or index >= self.values:
            raise Exception("Index out of bounds error")

        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.values:
            raise Exception("Index out of bounds error")
        
        self.data[index] = value

    def __isub__(self, row):
        for i in range(self.values):
            self.data[i] -= row.data[i]
        return self

    def __itruediv__(self, num):
        for i in range(self.values):
            self.data[i] /= num
        return self

    def __mul__(self, num):
        out = Row(self.values)
        out.data = [x*num for x in self.data]
        return out


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.data = [Row(cols) for _ in range(rows)]

    def __getitem__(self, index):
        if index < 0 or index >= self.rows:
            raise Exception("Index out of bounds error")

        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.rows:
            raise Exception("Index out of bounds error")
        
        self.data[index] = value

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

def find_nonzero_row(matrix, col):
    for row in range(0, matrix.rows):
        if matrix[row][col] != 0:
            return row
    return -1

def rref(matrix):
    for j in range(0, min(matrix.rows, matrix.cols - 1)):

        # make row start with a non-zero value
        if matrix[j][j] == 0:
            nz = find_nonzero_row(matrix, j)
            if nz == -1: 
                print("handle edge case here")
                continue

            matrix[j], matrix[nz] = matrix[nz], matrix[j]

        # normalize row
        matrix[j] /= matrix[j][j]

        # zero all other rows for the column
        for row in range(0, matrix.rows):
            if row == j: continue

            matrix[row] -= matrix[j] * matrix[row][j]

def random_matrix(rows, cols):
    import random
    m = Matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            m[i][j] = random.randint(-128, +128)
    
    return m


if __name__ == "__main__":
    m = random_matrix(3, 12)
    print(m)
    rref(m)
    print(m)