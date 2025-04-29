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

def test_take_turn_incorrect_input():
    # tests a case where user takes their first turn and guesses
    # incorrectly.
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    game.take_turn("g")
    assert game.mistakes_made == 1

def test_take_turn_repeat_input():
    # tests a case where user takes their first turn and guesses
    # incorrectly.
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    game.take_turn("g")
    game.take_turn("g")
    assert game.mistakes_made == 1

def test_take_turn_incorrect_input():
    # tests a case where user takes their first turn and guesses
    # incorrect input
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    game.take_turn("`")
    assert game.mistakes_made == 0  

def test_game_win_win():
    # tests a case where user takes their turn and they win
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["c","a","_"]
    game.take_turn("t")
    assert game.check_win() == True

def test_game_win_no_win():
    # tests a case where user does not win
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    assert game.check_win() == False

def test_game_lose_lose():
    # tests a case where user takes their turn and they lose
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    game.mistakes_made = 6
    assert game.check_loss() == True


def test_game_lose_no_lose():
    # tests a case where user takes their turn and they dont lose
    game = Game()
    game._secret_word = list("cat")
    game.known_word = ["_","_","_"]
    game.mistakes_made = 1
    assert game.check_loss() == False