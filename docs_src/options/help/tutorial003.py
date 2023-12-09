import clix


def main(fullname: str = clix.Option("Wade Wilson", show_default=False)):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    clix.run(main)
