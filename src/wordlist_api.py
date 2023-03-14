import requests
import pathlib
from string import ascii_letters

out_path = pathlib.Path("wordlist.txt")

url = "https://www.gutenberg.org/files/1661/1661-0.txt"

response = requests.get(url)

words = sorted(
    {
        word.lower()
        for word in response.text.split()
        if all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (len(word), word)
)

out_path.write_text("\n".join(words))
