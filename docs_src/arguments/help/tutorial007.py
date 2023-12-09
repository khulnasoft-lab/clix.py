import clix


def main(
    name: str = clix.Argument(..., help="Who to greet"),
    lastname: str = clix.Argument(
        "", help="The last name", rich_help_panel="Secondary Arguments"
    ),
    age: str = clix.Argument(
        "", help="The user's age", rich_help_panel="Secondary Arguments"
    ),
):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
