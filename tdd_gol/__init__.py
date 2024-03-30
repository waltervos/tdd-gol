class Matrix:
    def __init__(self, cells) -> None:
        self._cells = cells

    def neighbours_for(self, row, column):
        return [
            cell
            for cell in [
                self._cell_at(row - 1, column - 1),
                self._cell_at(row - 1, column),
                self._cell_at(row - 1, column + 1),
                self._cell_at(row, column - 1),
                self._cell_at(row, column + 1),
                self._cell_at(row + 1, column - 1),
                self._cell_at(row + 1, column),
                self._cell_at(row + 1, column + 1),
            ]
            if cell
        ]

    def _cell_at(self, row, column):
        if row < 0 or column < 0:
            return None
        try:
            return self._cells[row][column]
        except IndexError:
            return None

    def __eq__(self, other: "Matrix") -> bool:
        return self._cells == other._cells


class Cell:
    def __init__(self, alive):
        self._alive = alive

    def next_generation(self, neighbours):
        living_count = self._living_count(neighbours)
        if self.is_alive():
            if living_count in [2, 3]:
                return Cell(alive=True)
            else:
                return Cell(alive=False)
        else:
            if living_count == 3:
                return Cell(alive=True)
            else:
                return Cell(alive=False)

    def is_alive(self):
        return self._alive

    def is_dead(self):
        return not self.is_alive()

    def _living_count(self, cells: list["Cell"]):
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
    def __init__(self, width, height, living_cells_at=None) -> None:
        if not living_cells_at:
            living_cells_at = []

        self.board = self._create_board(
            of_width=width, of_height=height, with_living_cells_at=living_cells_at
        )

    def _create_board(self, of_width, of_height, with_living_cells_at):
        return [
            [
                (
                    a_live_cell()
                    if (row, column) in with_living_cells_at
                    else a_dead_cell()
                )
                for column in range(0, of_width)
            ]
            for row in range(0, of_height)
        ]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.board[0]) == 1:
            self.board = [[a_dead_cell()]]
        else:
            self.board = [[a_dead_cell(), a_live_cell(), a_dead_cell()] for row in self.board]
