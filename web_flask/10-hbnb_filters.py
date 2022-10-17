#!/usr/bin/python3
"""routing flask and displaying text"""
from flask import Flask, redirect, url_for, render_template

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """closes sqlalchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """routing for state list"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states, cities={})


@app.route("/states/<id>", strict_slashes=False)
def state_with_city(id):
    """check for cities under a state using it's id"""
    states = storage.all(State).values()
    cities = storage.all(City).values()

    for state in states:
        if state.id == id:
            return render_template("9-states.html",
                                   states=[state], cities=cities)
    return render_template("9-states.html", states={}, cities={})


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """gets filter values from the database and display on webpage"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           states=states, cities=cities, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
