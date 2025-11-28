import random

print("Welcome to the HANGMAN GAME!")

hangman_words = [
    "adventure",
    "butterfly",
    "chocolate",
    "discovery",
    "elephant",
    "fireplace",
    "galaxy",
    "happiness",
    "island",
    "journey",
    "kangaroo",
    "landscape",
    "mountain",
    "mystery",
    "notebook",
    "orchestra",
    "playground",
    "rainbow",
    "sunshine",
    "treasure"
]

word = hangman_words[random.randint(0, len(hangman_words) - 1)]
word_length = len(word)
game_over = False
word_indicator = []
chances = 5

for char in range (0, word_length):
    word_indicator.append("_")

while not game_over:
    print("Guess the letter!")
    print (word_indicator)
    letter = input(">")
    for char in range(0, len(word)):
        if letter == word[char]:
            word_indicator[char] = letter
    if letter not in word:
        chances -= 1

    if chances == 0:
        print("The man was hanged! GAME OVER!!")
        game_over = True
    elif not "_" in word_indicator:
        print("Word Guessed! Congratulations")
        game_over = True


