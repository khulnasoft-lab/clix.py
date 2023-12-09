import clix


def main(
    name: str,
    lastname: str = clix.Option("", help="Last name of person to greet."),
    formal: bool = clix.Option(
        False, help="Say hi formally.", rich_help_panel="Customization and Utils"
    ),
    debug: bool = clix.Option(
        False, help="Enable debugging.", rich_help_panel="Customization and Utils"
    ),
):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    clix.run(main)
