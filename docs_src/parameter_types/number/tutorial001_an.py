import clix
from typing_extensions import Annotated


def main(
    id: Annotated[int, clix.Argument(min=0, max=1000)],
    age: Annotated[int, clix.Option(min=18)] = 20,
    score: Annotated[float, clix.Option(max=100)] = 0,
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    clix.run(main)
