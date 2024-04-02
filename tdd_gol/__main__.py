import random
from tkinter import Canvas, Tk
from tdd_gol import Cell
from tdd_gol.factories import GameFactory, RandomGameFactory

class GameOfLife(Tk):
    def __init__(self, game_factory: GameFactory, width_and_height=400, resolution=100) -> None:
        super().__init__()

        self.resizable(False, False)

        self.width_and_height = width_and_height
        self.resolution = resolution
        self.size_factor = self.width_and_height / self.resolution

        self.geometry(f"{self.width_and_height}x{self.width_and_height}")

        self.canvas = Canvas(
            self,
            width=self.width_and_height,
            height=self.width_and_height,
            bg="darkorchid1",
        )
        self.canvas.pack()

        self.game = game_factory.create_game(width=self.resolution, height=self.resolution)

        self.after(50, self.update_board)

    def generate_board(self):
        "Draw a square on the game board for every live cell in the grid."
        for row_number, row in enumerate(self.game.board):
            for column_number, cell in enumerate(row):
                real_x = row_number * self.size_factor
                real_y = column_number * self.size_factor

                self.draw_cell(cell, real_x, real_y, self.size_factor)

    def draw_cell(self, cell: Cell, y, x, size):
        index = random.randint(0, 3)
        colour = ["chartreuse1", "aqua", "gold1", "cyan"][index]

        if cell.is_dead():
            return

        self.canvas.create_oval(x, y, x + size, y + size, fill=colour, outline=colour)

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
    game_of_life = GameOfLife(game_factory=RandomGameFactory(), resolution=50, width_and_height=600)
    game_of_life.mainloop()


if __name__ == "__main__":
    main()
