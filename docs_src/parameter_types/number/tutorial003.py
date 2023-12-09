import clix


def main(verbose: int = clix.Option(0, "--verbose", "-v", count=True)):
    print(f"Verbose level is {verbose}")


if __name__ == "__main__":
    clix.run(main)
