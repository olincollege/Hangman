# controller.py

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

        result = game.take_turn(letter)
        if result is not None:
            view.game_over(result, game.word)
            return


if __name__ == "__main__":
    pygame.init()
    game_loop(Game(), View())
    pygame.quit()
