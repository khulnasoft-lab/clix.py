import clix


def main(config: clix.FileText = clix.Option(...)):
    for line in config:
        print(f"Config line: {line}")


if __name__ == "__main__":
    clix.run(main)
