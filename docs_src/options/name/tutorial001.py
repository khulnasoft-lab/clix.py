import clix


def main(user_name: str = clix.Option(..., "--name")):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    clix.run(main)
