import clix
from typing_extensions import Annotated


def name_callback(value: str):
    if value != "Camila":
        raise clix.BadParameter("Only Camila is allowed")
    return value


def main(name: Annotated[str, clix.Option(callback=name_callback)]):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
