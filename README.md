# Code Guessing Game 🎯

Welcome to the Code Guessing Game! This is a console-based Python game where the player tries to guess a randomly generated 3-digit code. The player receives hints after each guess to help them narrow down the correct code.

## How to Play

1. **Start the Game**: Run the game, and a random 3-digit code with unique digits will be generated.
2. **Make Your Guesses**: 
   - Enter each digit of your guess one by one, in any order.
   - The game will evaluate your guess and provide a hint based on how close your guess is to the actual code.
3. **Receive Hints**: 
   - After each guess, you'll receive a detailed hint indicating:
     - Which digits are correct and in the correct position.
     - Which digits are correct but in the wrong position.
     - Which digits are not in the code at all.
   - If you guess all digits correctly but not in the correct order, the game will inform you.
4. **Win the Game**: Continue guessing until you correctly identify the 3-digit code in the correct order.

## Features

- **Flexible Guessing**: You can input digits in any order, and the game will evaluate your guess accordingly.
- **Detailed Hints**: The game provides hints that are easy to understand, using color coding for clarity:
  - **Green**: Digit is correct and in the correct position.
  - **Yellow**: Digit is correct but in the wrong position.
  - **Red**: Digit is not in the code.
- **Replayability**: After completing a game, you can choose to play again with a new code.
- **Simple and Interactive**: Designed for a fun, quick game with immediate feedback on each guess.

## Example Gameplay

Here’s an example of how the game might play out:

```plaintext
A 3-digit code has been generated. Try to guess it!

Enter digit 1 of 3: 5
Enter digit 2 of 3: 3
Enter digit 3 of 3: 8

Hint: 5 (not in code) | 3 (wrong position) | 8 (correct position)
Summary: 1 correct in place, 1 correct but in wrong place

Enter digit 1 of 3: 4
Enter digit 2 of 3: 8
Enter digit 3 of 3: 2

Hint: 4 (wrong position) | 8 (correct position) | 2 (not in code)
Summary: 1 correct in place, 1 correct but in wrong place

Enter digit 1 of 3: 8
Enter digit 2 of 3: 4
Enter digit 3 of 3: 3

Congratulations! You've guessed the code correctly in the correct order!
