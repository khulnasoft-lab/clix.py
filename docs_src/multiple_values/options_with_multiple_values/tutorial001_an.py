from typing import Tuple

import clix
from typing_extensions import Annotated


def main(user: Annotated[Tuple[str, int, bool], clix.Option()] = (None, None, None)):
    username, coins, is_wizard = user
    if not username:
        print("No user provided")
        raise clix.Abort()
    print(f"The username {username} has {coins} coins")
    if is_wizard:
        print("And this user is a wizard!")


if __name__ == "__main__":
    clix.run(main)
