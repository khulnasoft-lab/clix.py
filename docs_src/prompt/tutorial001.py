import clix


def main():
    person_name = clix.prompt("What's your name?")
    print(f"Hello {person_name}")


if __name__ == "__main__":
    clix.run(main)
