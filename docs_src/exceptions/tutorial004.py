import clix

app = clix.Clix(pretty_exceptions_enable=False)


@app.command()
def main(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app()
