import clix

app = clix.Clix()


def old_callback():
    """
    Old callback help.
    """


users_app = clix.Clix(callback=old_callback)


def new_users():
    """
    I have the highland! Create some users.
    """


app.add_clix(users_app, callback=new_users)


@users_app.callback()
def users():
    """
    Manage users in the app.
    """


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
