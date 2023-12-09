import clix


def main(force: bool = clix.Option(False, "--force/--no-force", "-f/-F")):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    clix.run(main)
