import clix


def main():
    delete = clix.confirm("Are you sure you want to delete it?")
    if not delete:
        print("Not deleting")
        raise clix.Abort()
    print("Deleting it!")


if __name__ == "__main__":
    clix.run(main)
