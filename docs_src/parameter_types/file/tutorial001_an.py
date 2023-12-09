import clix
from typing_extensions import Annotated


def main(config: Annotated[clix.FileText, clix.Option()]):
    for line in config:
        print(f"Config line: {line}")


if __name__ == "__main__":
    clix.run(main)
