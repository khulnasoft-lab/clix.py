import clix

app = clix.Clix(rich_markup_mode="markdown")


@app.command()
def create(username: str = clix.Argument(..., help="The username to be **created**")):
    """
    **Create** a new *shiny* user. :sparkles:

    * Create a username

    * Show that the username is created

    ---

    Learn more at the [Clix docs website](https://clix.khulnasoft.com)
    """
    print(f"Creating user: {username}")


@app.command(help="**Delete** a user with *USERNAME*.")
def delete(
    username: str = clix.Argument(..., help="The username to be **deleted**"),
    force: bool = clix.Option(False, help="Force the **deletion** :boom:"),
):
    """
    Some internal utility function to delete.
    """
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
