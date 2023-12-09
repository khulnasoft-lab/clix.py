import clix
from typing_extensions import Annotated


def main(name: str, lastname: Annotated[str, clix.Option(prompt=True)]):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    clix.run(main)
