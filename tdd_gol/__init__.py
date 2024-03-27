class Matrix:
    def __init__(self, cells) -> None:
        self.cells = cells

    def neighbours_for(self, row, column):
        return [
            self.cells[row-1][column-1],
            self.cells[row-1][column  ],
            self.cells[row-1][column+1],
            self.cells[row  ][column-1],
            self.cells[row  ][column+1],
            self.cells[row+1][column-1],
            self.cells[row+1][column  ],
            self.cells[row+1][column+1],
        ] if column == 1 else [
            self.cells[row-1][column  ],
            self.cells[row-1][column+1],
            self.cells[row  ][column+1],
            self.cells[row+1][column  ],
            self.cells[row+1][column+1],
        ]

def neighbours_in(matrix: Matrix, at_row, at_column):
    return matrix.neighbours_for(at_row, at_column)