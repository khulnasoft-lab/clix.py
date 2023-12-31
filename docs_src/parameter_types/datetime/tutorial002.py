from datetime import datetime

import clix


def main(
    launch_date: datetime = clix.Argument(
        ..., formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y"]
    )
):
    print(f"Launch will be at: {launch_date}")


if __name__ == "__main__":
    clix.run(main)
