from enum import Enum

import clix
from typing_extensions import Annotated


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


def main(
    network: Annotated[
        NeuralNetwork, clix.Option(case_sensitive=False)
    ] = NeuralNetwork.simple
):
    print(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    clix.run(main)
