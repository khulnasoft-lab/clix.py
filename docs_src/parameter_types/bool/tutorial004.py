import clix


def main(in_prod: bool = clix.Option(True, " /--demo", " /-d")):
    if in_prod:
        print("Running in production")
    else:
        print("Running demo")


if __name__ == "__main__":
    clix.run(main)
