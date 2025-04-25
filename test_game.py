from game import Game

def test_take_turn_one_turn():
    # tests a case where user takes their first turn and guesses
    # correctly.
    game = Game()
    game._secret_word = "cat"
    game.known_word = ["_","_","_"]
    game.take_turn("a")
    assert game.known_word == ["_","a","_"]


def test_take_turn_one_turn_incorrect():
    # tests a case where user takes their first turn and guesses
    # incorrectly.
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    game.take_turn("g")
    assert game.known_word == ["_","_","_"]

def test_take_turn_one_turn_game_win():
    # tests a case where user takes their turn and they win
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["c","a","_"]
    assert game.take_turn("t") == True

def test_take_turn_one_turn_game_lose():
    # tests a case where user takes their turn and they win
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    game.mistakes_made = 5
    assert game.take_turn("h") == False
