import clix


def main(name: str = clix.Argument(..., help="The name of the user to greet")):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
