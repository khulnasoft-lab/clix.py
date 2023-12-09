from typing import Optional

import clix
from typing_extensions import Annotated


def main(name: Annotated[Optional[str], clix.Argument()] = None):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
