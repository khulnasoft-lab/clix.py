import clix
from typing_extensions import Annotated


def main(user_name: Annotated[str, clix.Option("--name")]):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    clix.run(main)
