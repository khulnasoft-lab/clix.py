import clix
from typing_extensions import Annotated


def main(config: Annotated[clix.FileTextWrite, clix.Option()]):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    clix.run(main)
