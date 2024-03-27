class Matrix:
    def __init__(self, cells) -> None:
        self.cells = cells
        self._neigbour_offset = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

    def neighbours_for(self, row, column):
        result = []
        for (row_offset, column_offset) in self._neigbour_offset:
            if (row + row_offset) >= 0 and (row + row_offset) < len(self.cells):
                if (column + column_offset) >= 0 and (column + column_offset) < len(self.cells):
                    result.append(self._cell_at(row+row_offset, column+column_offset))
        return result


    def _cell_at(self, row, column):
        return self.cells[row][column]


def neighbours_in(matrix: Matrix, at_row, at_column):
    return matrix.neighbours_for(at_row, at_column)
