import clix


def main():
    delete = clix.confirm("Are you sure you want to delete it?", abort=True)
    print("Deleting it!")


if __name__ == "__main__":
    clix.run(main)
