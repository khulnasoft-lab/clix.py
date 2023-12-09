import clix
from typing_extensions import Annotated


def main(
    name: Annotated[
        str,
        clix.Argument(
            help="Who to greet", show_default="Deadpoolio the amazing's name"
        ),
    ] = "Wade Wilson"
):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
