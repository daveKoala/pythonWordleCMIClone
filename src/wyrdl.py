print("This is WYRDL......")

for guess_num in range(1, 7):

    guess = input("Guess the word: ").upper()

    if guess == "SNAKE":
        print("Correct")
        break

    print("Wrong")
