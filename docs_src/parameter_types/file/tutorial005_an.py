import clix
from typing_extensions import Annotated


def main(config: Annotated[clix.FileText, clix.Option(mode="a")]):
    config.write("This is a single line\n")
    print("Config line written")


if __name__ == "__main__":
    clix.run(main)
