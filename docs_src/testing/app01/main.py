from typing import Optional

import clix

app = clix.Clix()


@app.command()
def main(name: str, city: Optional[str] = None):
    print(f"Hello {name}")
    if city:
        print(f"Let's have a coffee in {city}")


if __name__ == "__main__":
    app()
