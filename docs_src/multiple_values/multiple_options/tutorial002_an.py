from typing import List

import clix
from typing_extensions import Annotated


def main(number: Annotated[List[float], clix.Option()] = []):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    clix.run(main)
