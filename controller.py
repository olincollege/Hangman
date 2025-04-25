"""
Controls a game of Hangman by integrating game.py and view.py.
"""

from game import Game
from view import View

def game_loop(game,view):
    """
    runs one game of hangman.
    Args:
        None
    Returns:
        None
    """
    while True:
        view.display_game_state(game)
        letter = view.text_input_box()
        turn_result = game.take_turn(letter)
        if not turn_result is None:
            view.game_over(turn_result)

# runs the game
if __name__ == "__main__":
    game_loop(Game(), View())
