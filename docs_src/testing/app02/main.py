import clix

app = clix.Clix()


@app.command()
def main(name: str, email: str = clix.Option(..., prompt=True)):
    print(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
    app()
