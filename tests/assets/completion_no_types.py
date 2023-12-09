import clix

app = clix.Clix()


def complete(ctx, args, incomplete):
    clix.echo(f"info name is: {ctx.info_name}", err=True)
    clix.echo(f"args is: {args}", err=True)
    clix.echo(f"incomplete is: {incomplete}", err=True)
    return [
        ("Camila", "The reader of books."),
        ("Carlos", "The writer of scripts."),
        ("Sebastian", "The type hints guy."),
    ]


@app.command()
def main(name: str = clix.Option("World", autocompletion=complete)):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
