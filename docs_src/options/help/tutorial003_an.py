import clix
from typing_extensions import Annotated


def main(fullname: Annotated[str, clix.Option(show_default=False)] = "Wade Wilson"):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    clix.run(main)
