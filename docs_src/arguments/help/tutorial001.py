import clix


def main(name: str = clix.Argument(..., help="The name of the user to greet")):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
