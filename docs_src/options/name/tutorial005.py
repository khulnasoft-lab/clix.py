import clix


def main(
    name: str = clix.Option(..., "--name", "-n"),
    formal: bool = clix.Option(False, "--formal", "-f"),
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
