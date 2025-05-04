"""
Test file for game.py
"""

from game import Game

def test_take_turn_one_turn():
    """
    Tests a case where user takes their first turn and guesses correctly.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = "cat"
    game.known_word = ["_", "_", "_"]
    game.take_turn("a")
    assert game.known_word == ["_", "a", "_"]


def test_take_turn_one_turn_incorrect():
    """
    Tests a case where user takes their first turn and guesses incorrectly.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_", "_", "_"]
    game.take_turn("g")
    assert game.known_word == ["_", "_", "_"]


def test_take_turn_incorrect_input_letter():
    """
    Tests a case where user takes their first turn and guesses incorrectly in
    the form of a letter.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_", "_", "_"]
    game.take_turn("g")
    assert game.mistakes_made == 1


def test_take_turn_repeat_input():
    """
    Tests a case where user takes their first turn and guesses incorrectly.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_", "_", "_"]
    game.take_turn("g")
    game.take_turn("g")
    assert game.mistakes_made == 1


def test_take_turn_incorrect_input_non_letter_symbol():
    """
    Tests a case where user takes their first turn and guesses incorrect input
    in the form of a non-letter symbol.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_", "_", "_"]
    game.take_turn("`")
    assert game.mistakes_made == 0


def test_game_win_win():
    """
    tests a case where user takes their turn and they win.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["c", "a", "_"]
    game.take_turn("t")
    assert game.check_win() is True


def test_game_win_no_win():
    """
    Tests a case where user does not win.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_", "_", "_"]
    assert game.check_win() is False

def test_game_lose_lose():
    """
    Tests a case where user takes their turn and they lose.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_", "_", "_"]
    game.mistakes_made = 6
    assert game.check_loss() is True


def test_game_lose_no_lose():
    """
    Tests a case where user takes their turn and they dont lose.

    Args:
        None.
    
    Returns:
        None.
    """
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_", "_", "_"]
    game.mistakes_made = 1
    assert game.check_loss() is False
