from app import app
from flask import render_template
from models.player import Player
from models.game import Game

@app.route("/rock/scissors")
def player_1_wins_with_rock():
    return "Player 1 wins by playing rock"