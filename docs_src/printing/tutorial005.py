import clix


def main(good: bool = True):
    message_start = "everything is "
    if good:
        ending = clix.style("good", fg=clix.colors.GREEN, bold=True)
    else:
        ending = clix.style("bad", fg=clix.colors.WHITE, bg=clix.colors.RED)
    message = message_start + ending
    clix.echo(message)


if __name__ == "__main__":
    clix.run(main)
