import clix


def main(username: str):
    if username == "root":
        print("The root user is reserved")
        raise clix.Abort()
    print(f"New user created: {username}")


if __name__ == "__main__":
    clix.run(main)
