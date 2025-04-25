"""
Implements the class that represents a game of Hangman
"""

from random_word import RandomWords

# An integer that represents the amount of mistakes that the player can make
# before the entire hangman is drawn and they lose the game.
ALLOWED_MISTAKES = 6

# A list of strings that represents numbers 0 through 9 as strings and is used
# to check against to make sure that the player does not input a number instead
# of a letter.
NUM_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Game:
    """
    Represents a game of Hangman.

    Attributes:
        used_letters: A list of strings that represents all the letters that the
        user has already guessed this game (correct and incorrect) and can't
        guess again.

        known_word: A list of strings that represents the letters that the
        user has successfully guessed this game filled into their respective
        positions in the word.

        mistakes_made: An integer representing the amount of incorrect guesses
        the users have made, it dictates how much of the hangman is drawn, and
        when it reaches 6 (head, torso, 2 hands, 2 feet) the game ends.
    """

    def __init__(self):
        """
        Constructor for Game class

        Args:
            None.

        Returns:
            None.
        """
        self.used_letters = []
        self._secret_word = list(
            RandomWords().get_random_word()
        )  # A list that represents the word that is being guessed in the game,
        # split up such that each letter is an element of the list.
        self.known_word = ["_" for _ in range(len(self._secret_word))]
        self.mistakes_made = 0

    def take_turn(self, letter):
        """
        Prompts the user to take their turn by inputting a letter and checks of
        their input is valid and in the word. If it is invalid the user is
        notified and allowed to enter a letter again, if it is not in the word
        mistakes_made is incremented, and if it is valid and in the word, then
        all instances of the letter are inserted into the blanks of the word.

        Args:
            letter: string representing the input character.

        Returns:
            False is the user has made the maximum amount of mistakes, and True
            otherwise.
        """
        if len(letter) != 1 or letter in NUM_LIST:
            print(
                f"'{letter}' is not a valid input, please only input a single"
                " letter"
            )
            self.take_turn()
        elif letter in self.used_letters:
            print(f"You already used '{letter}', choose another letter.")
            self.take_turn()
        elif letter in self._secret_word:
            for secret_word_letter_index, secret_word_letter_value in enumerate(
                self._secret_word
            ):
                if letter == secret_word_letter_value:
                    self.known_word[secret_word_letter_index] = letter
        else:
            self.mistakes_made += 1
        if self.mistakes_made >= ALLOWED_MISTAKES:
            return False
        return True

    @property
    def secret_word(self):
        """
        Uses the @property decorator to return a property of the _secret_word
        list so that it can be accessed outside of the class without the risk of
        it being accidentally modified.

        Args:
            None.

        Returns:
            A list of strings that represents a property of the _secret_word
            list, which represents the word that the player is trying to guess
            split up such that each letter is an element.
        """
        return self._secret_word
