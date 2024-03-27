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
        for row_offset, column_offset in self._neigbour_offset:
            column_index = column + column_offset
            row_index = row + row_offset
            if (column_index) >= 0 and (column_index) < 3 and row_index >= 0 and row_index < 3: 
                result.append(
                    self._cell_at(row_index, column_index)
                )
        return result

    def _cell_at(self, row, column):
        return self.cells[row][column]


def neighbours_in(matrix: Matrix, at_row, at_column):
    return matrix.neighbours_for(at_row, at_column)
