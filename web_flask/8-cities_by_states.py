#!/usr/bin/python3
"""routing flask and displaying text"""
from flask import Flask, redirect, url_for, render_template

from models import storage
from models.state import State
from models.city import City

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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """routing for displaying cities by their states"""
    states = storage.all(State)
    cities = storage.all(City)

    return render_template("8-cities_by_states.html",
                           states=states, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
