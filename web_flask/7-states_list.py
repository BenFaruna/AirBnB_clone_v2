#!/usr/bin/python3
"""routing flask and displaying text"""
from flask import Flask, redirect, url_for, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """closes sqlalchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """route to states list"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
