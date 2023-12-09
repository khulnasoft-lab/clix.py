import clix


def main(project_name: str = clix.Option(..., prompt=True, confirmation_prompt=True)):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    clix.run(main)
