class Matrix:
    def __init__(self, cells) -> None:
        self.cells = cells

    def neighbours_for(self, row, column):
        return (
            [
                self._cell_at(row - 1, column - 1),
                self._cell_at(row - 1, column),
                self._cell_at(row - 1, column + 1),
                self._cell_at(row, column - 1),
                self._cell_at(row, column + 1),
                self._cell_at(row + 1, column - 1),
                self._cell_at(row + 1, column),
                self._cell_at(row + 1, column + 1),
            ]
            if column == 1
            else [
                self._cell_at(row - 1, column),
                self._cell_at(row - 1, column + 1),
                self._cell_at(row, column + 1),
                self._cell_at(row + 1, column),
                self._cell_at(row + 1, column + 1),
            ]
            if column == 0
            else [
                self._cell_at(row - 1, column - 1),
                self._cell_at(row - 1, column),
                self._cell_at(row, column - 1),
                self._cell_at(row + 1, column - 1),
                self._cell_at(row + 1, column),
            ]
        )

    def _cell_at(self, row, column):
        return self.cells[row][column]


def neighbours_in(matrix: Matrix, at_row, at_column):
    return matrix.neighbours_for(at_row, at_column)
