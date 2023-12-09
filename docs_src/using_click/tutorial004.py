import click
import clix


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    click.echo("Dropped the database")


app = clix.Clix()


@app.command()
def sub():
    """
    A single-command Clix sub app
    """
    print("Clix is now below Click, the Click app is the top level")


clix_click_object = clix.main.get_command(app)

cli.add_command(clix_click_object, "sub")

if __name__ == "__main__":
    cli()
