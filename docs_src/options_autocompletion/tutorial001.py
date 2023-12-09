import clix

app = clix.Clix()


@app.command()
def main(name: str = clix.Option("World", help="The name to say hi to.")):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
