# Number Guessing Game

I created a simple number guessing game using Python where players have to guess a random number between 1 and 100 each round.

To run it: `python3 guess.py`. 

- It makes use of the `random` module to generate the number each round (limited to integers from 1 to 100 inclusive)
- It makes use of `while` loops to ensure the replayability of the game, the possibility of multiple attempts in a single round and ensure that only guesses that are valid (integers from 1 to 100) are allowed.
- It makes use of `if`/`elif`/`else` statements to determine if guesses are within the range of 1 to 100, if the guess is higher or lower than the random number and if a valid answer is given to the option to play again.
- It makes use of `try`/`except` statements are used to to catch entries that aren't whole numbers, such as text or decimals
- The game counts attempts and reports the total when you win.
- Invalid entries don't count as attempts so typos do not count as incorrect guesses
- The replay question accepts only `yes` or `no`, so `y` is rejected.       