from pathlib import Path
from typing import Optional

import clix


def main(config: Optional[Path] = clix.Option(None)):
    if config is None:
        print("No config file")
        raise clix.Abort()
    if config.is_file():
        text = config.read_text()
        print(f"Config file contents: {text}")
    elif config.is_dir():
        print("Config is a directory, will use all its config files")
    elif not config.exists():
        print("The config doesn't exist")


if __name__ == "__main__":
    clix.run(main)
