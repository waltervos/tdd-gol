# Rules of the game:
# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Finding neighbours in a matrix:
# (at least) One position away from every edge, a cell has eight neighbours
# At the edges a cell has fewer neighbours (the matrix isn't a globe): 3 or 5

# Game:
# Produces the next generation for each cell
# Exits if no cells change on next generation

class DescribeNeighboursInAMatrix:
    def it_has_eight_neighbours_in_the_center(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        neighbours = neighbours_in(matrix, at_row=1, at_column=1)
        assert neighbours == [1,2,3,4,6,7,8,9]