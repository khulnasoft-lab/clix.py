import clix


def name_callback(value: str):
    print("Validating name")
    if value != "Camila":
        raise clix.BadParameter("Only Camila is allowed")
    return value


def main(name: str = clix.Option(..., callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
