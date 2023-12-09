from typing import Optional

import clix

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise clix.Exit()


def main(
    name: str = clix.Option("World"),
    version: Optional[bool] = clix.Option(
        None, "--version", callback=version_callback
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
