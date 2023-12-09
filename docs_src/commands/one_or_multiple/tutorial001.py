import clix

app = clix.Clix()


@app.command()
def create():
    print("Creating user: Hiro Hamada")


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
