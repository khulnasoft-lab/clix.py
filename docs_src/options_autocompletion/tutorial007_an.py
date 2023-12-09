from typing import List

import clix
from typing_extensions import Annotated

valid_completion_items = [
    ("Camila", "The reader of books."),
    ("Carlos", "The writer of scripts."),
    ("Sebastian", "The type hints guy."),
]


def complete_name(ctx: clix.Context, incomplete: str):
    names = ctx.params.get("name") or []
    for name, help_text in valid_completion_items:
        if name.startswith(incomplete) and name not in names:
            yield (name, help_text)


app = clix.Clix()


@app.command()
def main(
    name: Annotated[
        List[str],
        clix.Option(help="The name to say hi to.", autocompletion=complete_name),
    ] = ["World"],
):
    for n in name:
        print(f"Hello {n}")


if __name__ == "__main__":
    app()
