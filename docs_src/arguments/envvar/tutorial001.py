import clix


def main(name: str = clix.Argument("World", envvar="AWESOME_NAME")):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    clix.run(main)
