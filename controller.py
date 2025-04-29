"""
Controls the game by integrating game.py and view.py
"""

import pygame
from game import Game
from view import View


def game_loop(game, view):
    """
    Runs one game of Hangman:
      - Displays state
      - Reads one letter
      - Updates game
      - When the game ends (win or lose), shows game-over screen and returns
    """
    while True:
        view.display_game_state(game)
        letter = view.text_input_box()
        if letter is None:
            return

        game.take_turn(letter)
        if game.check_win():
            view.game_over(True, game.word)
        elif game.check_loss():
            view.game_over(False, game.word)

if __name__ == "__main__":
    pygame.init()
    game_loop(Game(), View())
    pygame.quit()
