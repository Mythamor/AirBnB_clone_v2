#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present
            in DBStorage sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name></B>
Must use the option strict_slashes=False in your route definition
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    """
    Render template with states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)

    # sort State object alphabetically by name
    # sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
    Clean-up session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
