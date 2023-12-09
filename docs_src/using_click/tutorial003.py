import click
import clix

app = clix.Clix()


@app.command()
def top():
    """
    Top level command, form Clix
    """
    print("The Clix app is at the top level")


@app.callback()
def callback():
    """
    Clix app, including Click subapp
    """


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo("Hello %s!" % name)


clix_click_object = clix.main.get_command(app)

clix_click_object.add_command(hello, "hello")

if __name__ == "__main__":
    clix_click_object()
