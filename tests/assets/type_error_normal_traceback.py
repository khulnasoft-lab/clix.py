import clix

app = clix.Clix()


@app.command()
def main(name: str = "morty"):
    print(name)


broken_app = clix.Clix()


@broken_app.command()
def broken(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app(standalone_mode=False)

    clix.main.get_command(broken_app)()
