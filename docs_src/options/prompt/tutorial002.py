import clix


def main(
    name: str, lastname: str = clix.Option(..., prompt="Please tell me your last name")
):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    clix.run(main)
