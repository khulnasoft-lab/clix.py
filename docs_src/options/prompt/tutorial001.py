import clix


def main(name: str, lastname: str = clix.Option(..., prompt=True)):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    clix.run(main)
