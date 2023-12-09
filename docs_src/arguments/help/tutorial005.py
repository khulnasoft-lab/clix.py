import clix


def main(
    name: str = clix.Argument(
        "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
    )
):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
