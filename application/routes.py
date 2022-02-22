from application import app, db
from application.models import Games
from flask import render_template
@app.route('/')
@app.route('/home')
def home():
    all_games = Games.query.all()
    return render_template('index.html', title="Home", all_games=all_games)

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete/<name>')
def delete(name):
    first_game = Games.query.first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return f"name {id} deleted"