import clix


def main(
    name: str, email: str = clix.Option(..., prompt=True, confirmation_prompt=True)
):
    print(f"Hello {name}, your email is {email}")


if __name__ == "__main__":
    clix.run(main)
