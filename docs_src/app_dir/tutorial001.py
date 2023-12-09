from pathlib import Path

import clix

APP_NAME = "my-super-cli-app"


def main():
    app_dir = clix.get_app_dir(APP_NAME)
    config_path: Path = Path(app_dir) / "config.json"
    if not config_path.is_file():
        print("Config file doesn't exist yet")


if __name__ == "__main__":
    clix.run(main)
