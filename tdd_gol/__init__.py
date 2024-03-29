from enum import Enum, StrEnum, auto


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
            neighbour_column_index = column + column_offset
            neighbour_row_index = row + row_offset
            if 0 <= neighbour_column_index < len(
                self.cells[0]
            ) and 0 <= neighbour_row_index < len(self.cells):
                result.append(
                    self._cell_at(neighbour_row_index, neighbour_column_index)
                )
        return result

    def _cell_at(self, row, column):
        return self.cells[row][column]

    def __eq__(self, other: "Matrix") -> bool:
        return self.cells == other.cells

    def __repr__(self) -> str:
        return str([cell for cell in [row for row in self.cells]])


class Cell:
    def __init__(self, alive):
        self._alive = alive

    def next_generation(self, neighbours):
        if self._living_count(neighbours) not in [2, 3]:
            return Cell(alive=False)
        else:
            return Cell(alive=True)

    def is_alive(self):
        return self._alive

    def _living_count(self, cells):
        return len([c for c in cells if c.is_alive()])

    def __eq__(self, other: "Cell") -> bool:
        return self.is_alive() == other.is_alive()

    def __repr__(self) -> str:
        return "Alive" if self.is_alive() else "Dead"


def a_live_cell() -> Cell:
    return Cell(alive=True)


def a_dead_cell() -> Cell:
    return Cell(alive=False)


class Game:
    def __init__(self, board: Matrix) -> None:
        self._board = board

    def next(self):
        new_cells = []
        for row_index, row in enumerate(self._board.cells):
            new_cells.append([])
            for cell_index, cell in enumerate(row):
                neighbours = self._board.neighbours_for(row_index, cell_index)
                new_cell: Cell = cell.next_generation(neighbours)
                new_cells[row_index].append(new_cell)

        self._board = Matrix(new_cells)

    @property
    def board(self):
        return Matrix(
            [
                [a_dead_cell() for _ in range(0, len(self._board.cells[0]))]
                for _ in range(0, len(self._board.cells))
            ]
        )
