from app import app
from flask import render_template, request
from models.player import Player
from models.game import Game

@app.route("/task1/rock/scissors")
def player_1_wins_with_rock():
    return "Player 1 wins by playing rock"

@app.route("/<player_1_selection>/<player_2_selection>")
def two_player_game_route_handler(player_1_selection, player_2_selection):
    game = Game()
    player_1 = Player("Player 1", player_1_selection)
    player_2 = Player("Player 2", player_2_selection)
    winner = game.determine_game(player_1, player_2) 
    # return f"Player 1 choice is {player_1_selection} and Player 2 choice is {player_2_selection}, the winner is {winner.name}"
    return render_template("results.html", title = "Play", winner = winner, player_1 = player_1, player_2 = player_2)

@app.route("/welcome")
def show_welcome_page():
    return render_template("welcome.html", title = "Home")

@app.route("/<player_1_selection>")
def play_with_computer(player_1_selection):
    game = Game()
    player_1 = Player("Player 1", player_1_selection)
    player_2 = Player("Computer", game.make_computer_selection())
    winner = game.determine_game(player_1, player_2) 
    return render_template("results.html", title = "Play", winner = winner, player_1 = player_1, player_2 = player_2)

@app.route("/play")
def player_form():
    return render_template("play.html", title = "Play")

@app.route("/play", methods = ["POST"])
def play_game():
    game = Game()
    player_name = request.form["name"]
    player_choice = request.form["choice"]
    player = Player(player_name, player_choice)
    computer_player = Player("Computer", game.make_computer_selection())
    winner = game.determine_game(player, computer_player)
    return render_template("/results.html", title = "Results", winner = winner, player_1 = player, player_2 = computer_player)


