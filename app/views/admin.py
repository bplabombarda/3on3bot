from flask import Flask, render_template

from app import app, db
from app.models import Game


# =====================================================================
# Routes for pledge pages and AJAX endpoints.
# =====================================================================
@app.route('/admin')
def index():
    return render_template('admin/index.html')
