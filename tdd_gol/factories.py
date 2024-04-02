from abc import ABC, abstractmethod
from tdd_gol import Game

class GameFactory(ABC):
    @abstractmethod
    def create_game(self, width: int, height: int) -> Game:
        pass

class RandomGameFactory(GameFactory):
    def create_game(self, width: int, height: int) -> Game:
        from random import randint

        return Game(
            width=width,
            height=height,
            living_cells_at=[
                (row, column)
                for row in range(0, width)
                for column in range(0, height)
                if randint(0, 1) == 1
            ],
        )

class GliderGameFactory(GameFactory):
    def create_game(self, width: int, height: int) -> Game:
        return Game(
            width=width,
            height=height,
            living_cells_at=[
                (height - 3, width - 3),
                (height - 3, width - 2),
                (height - 3, width - 1),
                (height - 2, width - 3),
                (height - 1, width - 2),
            ],
        )