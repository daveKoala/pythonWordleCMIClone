import pathlib
import random
from string import ascii_letters

# list = pathlib.Path("wordlist.txt").read_text(encoding="utf-8")
# print(repr(list))

print("This is WYRDL.")

# Constants are UPPER_CASE_AND_UNDERSCORE by Python conventions BUT ARE NOT IMUTABLE!!!!!
# WORD = "SNAKE"


def main():
    # Pre-process
    word = get_random_word()

    print(word)

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            print(f"\nWell done: {guess_num}")
            break

    # Post-process
    else:
        game_over(word)


def get_random_word():
    wordlist = pathlib.Path(__file__).parent / "../wordlist.txt"
    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)


def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))


def game_over(word):
    print(f"The word was {word}")


if __name__ == "__main__":
    main()
