import clix
from typing_extensions import Annotated


def main(
    name: Annotated[str, clix.Option("--name", "-n")],
    formal: Annotated[bool, clix.Option("--formal", "-f")] = False,
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
