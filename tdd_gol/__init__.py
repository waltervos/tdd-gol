from enum import Enum, auto


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
            if 0 <= neighbour_column_index < 3 and 0 <= neighbour_row_index < 3:
                result.append(
                    self._cell_at(neighbour_row_index, neighbour_column_index)
                )
        return result

    def _cell_at(self, row, column):
        return self.cells[row][column]

    def __eq__(self, other: "Matrix") -> bool:
        return self.cells == other.cells


class Cell:
    def __init__(self, alive):
        self._alive = alive

    def next_generation(self, neighbours):
        if self._living_count(neighbours) not in [2, 3]:
            self._die_if_alive()
        else:
            self._respawn_if_dead()

    def _die_if_alive(self):
        if self.is_alive():
            self._alive = False

    def _respawn_if_dead(self):
        if not self.is_alive():
            self._alive = True

    def is_alive(self):
        return self._alive

    def _living_count(self, cells):
        return len([c for c in cells if c.is_alive()])

    def __eq__(self, other: "Cell") -> bool:
        return self.is_alive() == other.is_alive()


def a_live_cell() -> Cell:
    return Cell(alive=True)


def a_dead_cell() -> Cell:
    return Cell(alive=False)


class GameStatus(Enum):
    ACTIVE = auto()
    ENDED = auto()


class GameState:
    def __init__(self, status, generation, board) -> None:
        self.status = status

    def __eq__(self, other: object) -> bool:
        return True


class Game:
    def __init__(
        self, width: int, height: int, live_cells_at: list[tuple[int, int]]
    ) -> None:
        self._live_cells_at = live_cells_at

    def iterate(self):
        pass

    def get_state(self) -> Matrix:
        return GameState(
            status=GameStatus.ACTIVE,
            generation=2,
            board=Matrix(
                [[a_live_cell(), a_dead_cell()], [a_dead_cell(), a_live_cell()]]
            ),
        ) if len(self._live_cells_at) == 3 else GameState(
            status=GameStatus.ENDED,
            generation=2,
            board=Matrix(
                []
            ),
        )
