# Rules of the game:
# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


from tdd_gol import Game, Matrix, a_dead_cell, a_live_cell

# Finding neighbours in a matrix:
# (at least) One position away from every edge, a cell has eight neighbours
# At the edges a cell has fewer neighbours (the matrix isn't a globe): 3 or 5


def neighbours_in(matrix: Matrix, at_row, at_column):
    return matrix.neighbours_for(at_row, at_column)


def a_3x3_matrix():
    return Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


class DescribeFindingNeighboursInAMatrix:
    def it_has_eight_neighbours_in_the_middle_of_matrix(self):
        matrix = a_3x3_matrix()

        assert neighbours_in(matrix, at_row=1, at_column=1) == [1, 2, 3, 4, 6, 7, 8, 9]

    def it_has_five_neighbours_in_the_middle_at_the_left_edge(self):
        matrix = a_3x3_matrix()
        assert neighbours_in(matrix, at_row=1, at_column=0) == [1, 2, 5, 7, 8]

    def it_has_five_neighbours_in_the_middle_at_the_right_edge(self):
        matrix = a_3x3_matrix()
        assert neighbours_in(matrix, at_row=1, at_column=2) == [2, 3, 5, 8, 9]

    def it_has_five_neighbours_at_the_top_in_the_middle_column(self):
        assert neighbours_in(a_3x3_matrix(), at_row=0, at_column=1) == [1, 3, 4, 5, 6]

    def it_has_five_neighbours_at_the_bottom_in_the_middle_column(self):
        assert neighbours_in(a_3x3_matrix(), at_row=2, at_column=1) == [4, 5, 6, 7, 9]


# Rules of the game:
# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


class DescribeCellLifecycle:
    def it_survives_with_two_live_neighbours(self):
        cell = a_live_cell()
        cell.next_generation([a_live_cell(), a_live_cell()])

        assert cell.is_alive()

    def it_dies_when_it_has_four_live_neighbours(self):
        cell = a_live_cell()
        cell.next_generation([a_live_cell() for _ in range(0, 4)])

        assert not cell.is_alive()

    def it_dies_with_one_living_and_one_dead_neighbour(self):
        cell = a_live_cell()
        cell.next_generation([a_live_cell(), a_dead_cell()])

        assert not cell.is_alive()

    def it_resurrects_when_it_has_three_live_neighbours(self):
        cell = a_dead_cell()
        cell.next_generation([a_live_cell() for _ in range(0, 3)])

        assert cell.is_alive()

    def it_remains_dead_without_live_neighbours(self):
        cell = a_dead_cell()
        cell.next_generation([])

        assert not cell.is_alive()


# Game:
# Produces the next generation for each cell
# Exits if no cells change on next generation


class DescribeRunningTheGame:
    def it_initializes_the_game(self):
        game = Game(width=2, height=2, life_at=[(0,0), (0,1), (1,0)])
        game_state = game.get_state()
        assert game_state['status'] == "Active" and game_state['board'] == [
            [a_live_cell(), a_live_cell()],
            [a_live_cell(), a_dead_cell()]
        ]

    def it_produces_the_next_generation(self):
        game = Game(width=2, height=2, life_at=[(0,0), (0,1), (1,0)])
        game.next_generation()
        assert game.get_board() == [
                [a_live_cell(), a_live_cell()],
                [a_live_cell(), a_live_cell()]
            ]
        
    def it_halts_when_the_next_generation_is_the_same_as_the_last_one(self):
        game = Game(width=2, height=2, life_at=[(0,0), (0,1), (1,0), (1,1)])
        game.next_generation()
        game.next_generation()
        game_state = game.get_state()
        assert game_state['status'] == "Halted" and game_state['board'] == [
                [a_live_cell(), a_live_cell()],
                [a_live_cell(), a_live_cell()]
            ]
