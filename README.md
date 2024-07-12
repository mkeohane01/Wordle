## Project 1: Wordle

### Introduction
Welcome to the Wordle game development project! In this project, you will build [Wordle](https://www.nytimes.com/games/wordle/index.html), a word puzzle game where the player has to guess a word within a limited number of attempts. After each guess, the game provides feedback on the correctness of the guess. This README will guide you through the game, explain what is expected from you, and suggest some possible extensions to enhance the game. 

In order to submit this project, we will do live demos on Monday with Jon in attendence.

### How to Play
1. The game will choose a random word from the word bank establish in ```wordlebank.py```.
2. The player has a limited number of attempts (default is 6) to guess the word.
3. After each guess, the game needs to provide feedback:
    - 🟩: Correct letter in the correct position.
    - 🟨: Correct letter in the wrong position.
    - 🔲: Incorrect letter.
4. The game continues until you either guess the word correctly or run out of attempts.
5. After the game, print out the feedback for all of your guesses.

### Example
If the word is "apple" and the player guesses "meals", the feedback would be "🔲🟨🟨🟩🔲"

### What is Expected
- Build out the game loop to get user inputs
    - Make sure to check that the input is valid (correct length and in wordbank)
    - Print out informative messages troughout
- Check each letter of the user guess with real answer and provide feedback on guess
    - Store each feedback string to provide recap of all guesses at the end
- Break the loop after user reaches the set max number of guesses or if the guess is correct
    - Print out winning or losing message along with guesses recap
- Try to implement at least 1 extension to enhance the project. It doesn't have to even be one on the list below.

### Optional Extensions
Here are some ideas to extend the project:
1. **Letter Bank:** Keep track of all avaliable letters and once a letter is used (and incorrect), remove it from the letter bank.
2. **Edit the word options:** Edit the lists in the `wordbank.py` file to increase the variety of words. Also could make a user input to seed a word for your friend to guess.
3. **Difficulty levels:** Implement different difficulty levels with varying word lengths and number of attempts. May need to make another list in wordlebank for this.
4. **Scoring system:** Add a scoring system to track the player's performance over multiple games.
5. **Mastermind Mode:** Option to set to [mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) mode which uses symbols instead of words, yet provides similar feedback structure


### Hints
- Try using ```.lower()``` on the user guess to make it comparable to bank
- Remember you can store strings inside of lists as well as loop over them both
- If you want a list of all letters in alphabet: ```list("abcdefghijklmnopqrstuvwxyz")```
- The emojis are treated as characters in the string