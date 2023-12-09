from typing import List, Optional

import clix
from typing_extensions import Annotated


def main(user: Annotated[Optional[List[str]], clix.Option()] = None):
    if not user:
        print("No provided users")
        raise clix.Abort()
    for u in user:
        print(f"Processing user: {u}")


if __name__ == "__main__":
    clix.run(main)
