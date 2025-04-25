from game import Game
from view import View

class Controller:
    def __init__(self, game, view):
        """
        runs a game of Hangman.

        Attributes:
            game: a instance of the Game class containing functions to run a game
            of Hangman.

            view: a instance of the View class containing functions that create the
            GUI and user interface of a game of hangman.
        """
        self.game = game
        self.view = view

    def gameloop(self):
        """
        runs one game of hangman.
        Args:
            None
        Returns:
            None 
        """
        game = self.game
        view = self.view
        while True:
            view.display_game_state(game)
            input = view.text_input_box()
            game.take_turn(input)
            if game.mistakes_made == 6:
                view.game_over()

#runs the game
if __name__ == '__main__':
    game = Game()
    view = View()
    controller = Controller(game,view)
    controller.gameloop()
        
