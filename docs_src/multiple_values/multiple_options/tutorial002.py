from typing import List

import clix


def main(number: List[float] = clix.Option([])):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    clix.run(main)
