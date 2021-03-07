class Matrix:
    def __init__(self, rows):
        if len(set(len(row) for row in rows)) > 1:
            raise ValueError("All matrix rows must be the same length")

        self.rows = rows

    def __add__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrix dimensions don't match")

        return Matrix(
            [
                [a + b for a, b in zip(a_row, b_row)]
                for a_row, b_row in zip(self.rows, other.rows)
            ]
        )

    def __sub__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrix dimensions don't match")

        return Matrix(
            [
                [a - b for a, b in zip(a_row, b_row)]
                for a_row, b_row in zip(self.rows, other.rows)
            ]
        )

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Don't know how to multiply {type(other)} with Matrix")

        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Matrix dimensions don't match")

        rows = [[0 for _ in other.rows[0]] for _ in self.rows]

        for i in range(len(self.rows)):
            for j in range(len(other.rows[0])):
                for k in range(len(other.rows)):
                    rows[i][j] += self.rows[i][k] * other.rows[k][j]

        return Matrix(rows)

    def __repr__(self):
        return "\n".join(str(row) for row in self.rows)


if __name__ == "__main__":
    m0 = Matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
    m1 = Matrix(
        [
            [1, 2, 3],
            [4, 1, 4],
            [5, 7, 9],
        ]
    )
    assert (m1 * m0).rows == m1.rows

    m2 = Matrix(
        [
            [1, 2, 3],
            [1, 4, 3],
            [1, 0, 5],
        ]
    )
    assert (m2 * m0).rows == m2.rows

    m3 = m1 + m2
    m4 = m1 - m2
    m5 = m1 * m2

    m6 = Matrix(
        [
            [1, 2, 4, 3],
            [3, 4, 1, 5],
            [1, 6, 1, 3],
        ]
    )
