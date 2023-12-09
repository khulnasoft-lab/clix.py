import clix


def main(name: str = clix.Argument("World", help="Who to greet", show_default=False)):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
