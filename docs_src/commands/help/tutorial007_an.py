from typing import Union

import clix
from typing_extensions import Annotated

app = clix.Clix(rich_markup_mode="rich")


@app.command()
def create(
    username: Annotated[str, clix.Argument(help="The username to create")],
    lastname: Annotated[
        str,
        clix.Argument(
            help="The last name of the new user", rich_help_panel="Secondary Arguments"
        ),
    ] = "",
    force: Annotated[bool, clix.Option(help="Force the creation of the user")] = False,
    age: Annotated[
        Union[int, None],
        clix.Option(help="The age of the new user", rich_help_panel="Additional Data"),
    ] = None,
    favorite_color: Annotated[
        Union[str, None],
        clix.Option(
            help="The favorite color of the new user",
            rich_help_panel="Additional Data",
        ),
    ] = None,
):
    """
    [green]Create[/green] a new user. :sparkles:
    """
    print(f"Creating user: {username}")


@app.command(rich_help_panel="Utils and Configs")
def config(configuration: str):
    """
    [blue]Configure[/blue] the system. :wrench:
    """
    print(f"Configuring the system with: {configuration}")


if __name__ == "__main__":
    app()
