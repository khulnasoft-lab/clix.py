from typing import Tuple

import clix


def main(
    names: Tuple[str, str, str] = clix.Argument(
        ("Harry", "Hermione", "Ron"), help="Select 3 characters to play with"
    )
):
    for name in names:
        print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
