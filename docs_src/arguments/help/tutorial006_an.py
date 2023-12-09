import clix
from typing_extensions import Annotated


def main(name: Annotated[str, clix.Argument(metavar="✨username✨")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
