import clix
from typing_extensions import Annotated


def main(
    id: Annotated[int, clix.Argument(min=0, max=1000)],
    rank: Annotated[int, clix.Option(max=10, clamp=True)] = 0,
    score: Annotated[float, clix.Option(min=0, max=100, clamp=True)] = 0,
):
    print(f"ID is {id}")
    print(f"--rank is {rank}")
    print(f"--score is {score}")


if __name__ == "__main__":
    clix.run(main)
