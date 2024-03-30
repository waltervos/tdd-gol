import os
import time
from tdd_gol import Game


def main():
    game = Game(
        width=10,
        height=8,
        living_cells_at=[
            (1, 7),
            (2, 7),
            (2, 8),
            (3, 7),
            (2, 5),
            (3, 5),
            (4, 5),
            (5, 3),
            (6, 3),
            (6, 1),
        ],
    )

    game = Game(
        width=41,
        height=3,
        living_cells_at=(
            [(1, i) for i in range(1, 9)]
            + [(1, j) for j in range(10, 15)]
            + [(1, k) for k in range(18, 21)]
            + [(1, l) for l in range(27, 34)]
            + [(1, l) for l in range(35, 40)]
        ),
    )
    game = Game(
        width=40,
        height=40,
        living_cells_at=[(37, 37), (37, 38), (37, 39), (38, 37), (39, 38)],
    )

    os.system("cls")
    print(game)
    for round in game:
        time.sleep(0.25)
        os.system("cls")
        print(round)


if __name__ == "__main__":
    main()
