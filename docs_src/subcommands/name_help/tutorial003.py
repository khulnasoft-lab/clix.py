import clix

app = clix.Clix()


def users():
    """
    Manage users in the app.
    """


users_app = clix.Clix(callback=users)
app.add_clix(users_app)


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
