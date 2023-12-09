import clix


def name_callback(ctx: clix.Context, param: clix.CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    print(f"Validating param: {param.name}")
    if value != "Camila":
        raise clix.BadParameter("Only Camila is allowed")
    return value


def main(name: str = clix.Option(..., callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    clix.run(main)
