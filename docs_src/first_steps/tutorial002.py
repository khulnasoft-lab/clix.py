import clix


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
