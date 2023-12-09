from typing import Optional

import clix

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise clix.Exit()


def name_callback(name: str):
    if name != "Camila":
        raise clix.BadParameter("Only Camila is allowed")
    return name


def main(
    name: str = clix.Option(..., callback=name_callback),
    version: Optional[bool] = clix.Option(
        None, "--version", callback=version_callback, is_eager=True
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
