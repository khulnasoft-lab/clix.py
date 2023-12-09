import clix
from typing_extensions import Annotated

app = clix.Clix()


@app.command()
def main(name: str, email: Annotated[str, clix.Option(prompt=True)]):
    print(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
    app()
