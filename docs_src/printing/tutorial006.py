import clix


def main(name: str):
    clix.secho(f"Welcome here {name}", fg=clix.colors.MAGENTA)


if __name__ == "__main__":
    clix.run(main)
