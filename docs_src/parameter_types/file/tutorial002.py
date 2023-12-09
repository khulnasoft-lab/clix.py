import clix


def main(config: clix.FileTextWrite = clix.Option(...)):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    clix.run(main)
