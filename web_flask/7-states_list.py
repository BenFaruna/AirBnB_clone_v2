#!/usr/bin/python3
"""routing flask and displaying text"""
from flask import Flask, redirect, url_for, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    """closes sqlalchemy session"""
    storage.close()


@app.route("/states_list", strick_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template("template/7-states_list.html", states=states)


if __name__ == "__main__":
   pp.run(host='0.0.0.0', port=5000, debug=True)
