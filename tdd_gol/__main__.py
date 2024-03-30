import os
import random
import time
from tkinter import Canvas, Tk
from tdd_gol import Game


class GameOfLife(Tk):
    def __init__(self, width_and_height=400, resolution=100) -> None:
        super().__init__()

        self.resizable(False, False)

        self.width_and_height = width_and_height
        self.resolution = resolution
        self.size_factor = self.width_and_height / self.resolution

        self.geometry(f"{self.width_and_height}x{self.width_and_height}")

        self.canvas = Canvas(
            self, width=self.width_and_height, height=self.width_and_height, bg="gray27"
        )
        self.canvas.pack()

        self.game = Game(
            width=self.resolution,
            height=self.resolution,
            # living_cells_at=[ # Creates a glider in the bottom right
            #     (self.resolution - 3, self.resolution - 3),
            #     (self.resolution - 3, self.resolution - 2),
            #     (self.resolution - 3, self.resolution - 1),
            #     (self.resolution - 2, self.resolution - 3),
            #     (self.resolution - 1, self.resolution - 2),
            # ],
            # living_cells_at=[ # Creates 4 blinkers
            #     ((self.resolution / 2) - 1, (self.resolution / 2) - 1),
            #     ((self.resolution / 2) - 2, (self.resolution / 2) - 1),
            #     ((self.resolution / 2) - 2, (self.resolution / 2) - 2),
            #     ((self.resolution / 2) - 2, self.resolution / 2),
            # ],
            living_cells_at=[ # Random
                (row, column)
                for row in range(0, self.resolution)
                for column in range(0, self.resolution)
                if random.randint(0,1) == 1
            ],
        )

        self.after(50, self.update_board)

    def generate_board(self):
        "Draw a square on the game board for every live cell in the grid."
        for row_number, row in enumerate(self.game.board):
            for column_number, cell in enumerate(row):
                real_x = row_number * self.size_factor
                real_y = column_number * self.size_factor
                if cell.is_alive():
                    self.draw_square(real_x, real_y, self.size_factor)

    def draw_square(self, y, x, size):
        self.canvas.create_rectangle(
            x, y, x + size, y + size, fill="chartreuse1", outline="chartreuse1"
        )

    def update_board(self):
        # Clear the canvas.
        self.canvas.delete("all")
        # Run the next generation and update the game grid.
        try:
            self.game = next(self.game)
        except StopIteration:
            self.quit()
            return
        # Generate the game board with the current population.
        self.generate_board()
        # Set the next tick in the timer.
        self.after(100, self.update_board)


def main():
    game_of_life = GameOfLife()
    game_of_life.mainloop()


if __name__ == "__main__":
    main()
