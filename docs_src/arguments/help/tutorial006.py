import clix


def main(name: str = clix.Argument("World", metavar="✨username✨")):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
