import clix
from typing_extensions import Annotated


def main(force: Annotated[bool, clix.Option("--force/--no-force", "-f/-F")] = False):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    clix.run(main)
