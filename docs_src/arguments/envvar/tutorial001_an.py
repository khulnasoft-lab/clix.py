import clix
from typing_extensions import Annotated


def main(name: Annotated[str, clix.Argument(envvar="AWESOME_NAME")] = "World"):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    clix.run(main)
