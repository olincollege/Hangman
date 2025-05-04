# Hangman

## Summary:

In this project, we have made a fully functional game of Hangman: which is a game in which you are given a series of dashes that represent the length of a word that you need to guess, you can type in one letter at a time and if it is correct all instances of that letter are filled in, but if you are wrong the Hangman gets one more of his parts drawn. If all the parts of the hangman (6 total) are drawn before you guess the word, you lose, otherwise you guessed the word correctly and you won! This game is complete with a PyGame GUI that shows line art of a stick figure being hung as the player gets words wrong, a list of letters that you already used, dashes to represent the letters that still need to be guessed, and letters that have been correctly guessed already replacing the dashed when you input them into the input text box. It also had a "You Win" screen and a "Game Over" screen, both with the actual word displayed.

## Dependencies:

To run the code, you need to have all python files in the same folder, you will also need to install the python libraries `pygame` and `random_word`. Install them by writing the following into your terminal:

```
pip install pygame
pip install random_word
```

## Playing the Game:

You just need to run the file controller.py, and if all of the python files are in the same folder, it will run the game, where you can input your guesses into the PyGame textbox to play the game.
