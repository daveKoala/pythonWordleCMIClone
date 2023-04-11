# The 1970's Mastermind game similar to WYRDLE except it uses colours.

import random

NUM_ROWS = 10
NUM_CELLS = 5
COLOURS = {
    "green": "G",
    "red": "R",
    "yellow": "Y",
    "blue": "B",
    "orange": "O",
    "pink": "P",
    "white": "W"
}


def main():

    # Preprocess

    code = create_code(options=COLOURS)

    # print(code)

    # Process (main loop)

    # For each guess loop
    for guess_code in range(1, NUM_ROWS):

        guess = input(f"\nGuess {guess_code}: ").upper()

        guess_list = list(guess)

        print(f"guess.........{guess_list}")

        intersect = set(code) & set(guess_list)
        intersect_count = len(intersect)

        positional_count = 0

        result_list = []

        for i in range(NUM_CELLS):
            if code[i] == guess_list[i]:
                positional_count += 1
                result_list.append(1)
            elif code[i] in guess_list:
                result_list.append(2)
            else:
                result_list.append(0)

        print("Intersect count:", intersect_count)
        print("Positional count:", positional_count)
        print("Result list:", result_list)

        if all(x == 1 for x in result_list):
            print("Success")
            break

        print(f"Wrong: {code}")


def create_code(options):
    output_code = []

    for i in range(NUM_CELLS):
        key = random.choice(list(options.keys()))

        output_code.append(options[key])

    return output_code


if __name__ == "__main__":
    main()
