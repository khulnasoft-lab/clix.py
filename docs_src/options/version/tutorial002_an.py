from typing import Optional

import clix
from typing_extensions import Annotated

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise clix.Exit()


def name_callback(name: str):
    if name != "Camila":
        raise clix.BadParameter("Only Camila is allowed")


def main(
    name: Annotated[str, clix.Option(callback=name_callback)],
    version: Annotated[
        Optional[bool], clix.Option("--version", callback=version_callback)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
