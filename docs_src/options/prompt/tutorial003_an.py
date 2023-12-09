import clix
from typing_extensions import Annotated


def main(
    project_name: Annotated[str, clix.Option(prompt=True, confirmation_prompt=True)]
):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    clix.run(main)
