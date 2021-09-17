from app import app
from flask import render_template
from models.player import Player
from models.game import Game

@app.route("/rps")
def index():
    return render_template("index.html", title = "Home")

@app.route("/rock")
def rock(index):
    return render_template("base.html", title = "Rock Paper Scissors")