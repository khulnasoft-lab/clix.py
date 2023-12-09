import clix
import clix.main

clix.main.rich = None


def main(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    clix.run(main)
