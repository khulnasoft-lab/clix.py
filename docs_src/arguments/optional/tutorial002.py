from typing import Optional

import clix


def main(name: Optional[str] = clix.Argument(default=None)):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
