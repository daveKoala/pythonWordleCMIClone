# Similar to WYRDLE except it uses colours. There are two modes easy and hard. Easy will give feed back that can be mapped to your guess the hard mode you are given an aggragate

import random

NUM_ROWS = 5
NUM_CELLS = 6
COLOURS = {
    "green": "G",
    "red": "R",
    "yellow": "Y",
    "blue": "B"
}


def main():

    # Preprocess

    code = create_code(options=COLOURS)

    print(code)

    # Process (main loop)

    # For each guess loop
    for guess_code in range(1, NUM_ROWS):

        guess = input(f"\nGuess {guess_code}: ").upper()

        guess_list = list(guess)

        print(f"guess.........{guess_list}")

        intersect = set(guess_list) & set(code)
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

        if guess == code:
            print("Success")
            break

        print("Wrong")


def create_code(options):
    output_code = []

    for i in range(NUM_CELLS):
        key = random.choice(list(options.keys()))

        output_code.append(options[key])

    return output_code


if __name__ == "__main__":
    main()
