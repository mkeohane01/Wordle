### PROJECT 1 - WORDLE 
# The wordle game is a word puzzle game where the player has to guess a word.
# The player has a limited number of attempts to guess the word.
# After each guess, the game provides feedback on the correctness of the guess.
# Feedback: 🟩 - correct letter in the correct position, 🟨 - correct letter in the wrong position, 🔲 - incorrect letter.
# The game continues until the player either guesses the word correctly or runs out of attempts.

# Prepopulated code to get you started. Feel free to edit these lines as you progress.
# Import random and the wordle list
import random
from wordlebank import wordbank

# Welcome messages
print("Welcome to Worldle! Try to guess the word.")
print("Feedback: 🟩 - correct letter in the correct position, 🟨 - correct letter in the wrong position, 🔲 - incorrect letter.")

# Come up with a word for the player to guess
worldle_word = random.choice(wordbank)

# Set the maximum number of attempts
num_attempts = 6

# Build game logic