from flask import render_template, flash, redirect, jsonify, request

from app import app, db
from app.models import Game


# =====================================================================
# Admin routes for creating, editing, & deleting Campaign
# =====================================================================
@app.route('/')
@app.route('/index')
def index():
    games = Game.query.all()

    return render_template('index.html', games=games)


# =====================================================================
# Get all games. Args: order by "asc" or "desc" by date.
# =====================================================================
@app.route('/games/')
def index():
    # =================================================================
    # Parse URL arguments for order parameters
    # =================================================================
    order = request.args.get('order')

    # =================================================================
    # Query DB for all games. Can order by:
    #   - descending ("order=desc") or
    #
    # ...well, anything else returns ascending
    # =================================================================
    if order == 'desc':
        games = Game.query.all().order_by(Game.game_date.desc())
    else:
        games = Game.query.all().order_by(Game.game_date)

    return jsonify(games=games)


# =====================================================================
# Get game by id
# =====================================================================
@app.route('/game/<int:game_id>/')
def get_games(game_id):
    # =================================================================
    # Query DB for game based on game_id argument
    # =================================================================
    game = Campaign.query.filter_by(id=game_id).first()

    return jsonify(game=game)
