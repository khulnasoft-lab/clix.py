import time

import clix


def main():
    total = 0
    with clix.progressbar(range(100), label="Processing") as progress:
        for value in progress:
            # Fake processing time
            time.sleep(0.01)
            total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    clix.run(main)
