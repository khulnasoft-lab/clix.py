import clix
from typing_extensions import Annotated


def main(name: Annotated[str, clix.Argument(help="Who to greet")] = "World"):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
