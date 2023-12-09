import random

import clix
from typing_extensions import Annotated


def get_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


def main(name: Annotated[str, clix.Argument(default_factory=get_name)]):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
