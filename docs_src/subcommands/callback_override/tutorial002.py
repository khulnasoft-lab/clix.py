import clix

app = clix.Clix()


def users_callback():
    print("Running a users command")


users_app = clix.Clix(callback=users_callback)
app.add_clix(users_app, name="users")


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
