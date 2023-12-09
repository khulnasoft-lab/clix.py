import clix
from typing_extensions import Annotated

app = clix.Clix()


@app.command()
def main(name: Annotated[str, clix.Option(help="The name to say hi to.")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
