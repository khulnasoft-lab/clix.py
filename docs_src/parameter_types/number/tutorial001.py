import clix


def main(
    id: int = clix.Argument(..., min=0, max=1000),
    age: int = clix.Option(20, min=18),
    score: float = clix.Option(0, max=100),
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    clix.run(main)
