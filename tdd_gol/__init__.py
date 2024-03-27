def neighbours_in(matrix, at_row, at_column):
    return [
        matrix[at_row-1][at_column-1],
        matrix[at_row-1][at_column  ],
        matrix[at_row-1][at_column+1],
        matrix[at_row  ][at_column-1],
        matrix[at_row  ][at_column+1],
        matrix[at_row+1][at_column-1],
        matrix[at_row+1][at_column  ],
        matrix[at_row+1][at_column+1],
    ] if at_column == 1 else [
        matrix[at_row-1][at_column  ],
        matrix[at_row-1][at_column+1],
        matrix[at_row  ][at_column+1],
        matrix[at_row+1][at_column  ],
        matrix[at_row+1][at_column+1],
    ]