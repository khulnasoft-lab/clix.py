import click
import clix


class CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"<CustomClass: value={self.value}>"


class CustomClassParser(click.ParamType):
    name = "CustomClass"

    def convert(self, value, param, ctx):
        return CustomClass(value * 3)


def main(
    custom_arg: CustomClass = clix.Argument(click_type=CustomClassParser()),
    custom_opt: CustomClass = clix.Option("Foo", click_type=CustomClassParser()),
):
    print(f"custom_arg is {custom_arg}")
    print(f"--custom-opt is {custom_opt}")


if __name__ == "__main__":
    clix.run(main)
