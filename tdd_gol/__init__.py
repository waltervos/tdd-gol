class Matrix:
    def __init__(self, cells) -> None:
        self.cells = cells

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
            return self.cells[row][column]
        except IndexError:
            return None

    def __eq__(self, other: "Matrix") -> bool:
        return self.cells == other.cells


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

        self._board_matrix = self._create_board(
            of_width=width, of_height=height, with_living_cells_at=living_cells_at
        )

    def _create_board(self, of_width, of_height, with_living_cells_at) -> Matrix:
        return Matrix(
            [
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
        )

    def __iter__(self):
        return self

    def __next__(self):
        new_board_matrix = Matrix(
            [
                [
                    cell.next_generation(
                        self._board_matrix.neighbours_for(row_index, cell_index)
                    )
                    for cell_index, cell in enumerate(row)
                ]
                for row_index, row in enumerate(self.board)
            ]
        )

        if new_board_matrix == self._board_matrix:
            raise StopIteration
        
        self._board_matrix = new_board_matrix
        return self

    @property
    def board(self):
        return self._board_matrix.cells
    
    def __str__(self) -> str:
        game_string = ""
        for row in self.board:
            for cell in row:
                game_string += "██" if cell.is_alive() else "  "
            game_string += "\n"

        return game_string
