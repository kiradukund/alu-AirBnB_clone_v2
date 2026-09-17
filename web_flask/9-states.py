#!/usr/bin/python3
"""Flask web application - States and State."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display HTML page with list of states."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('9-states.html', states=states, state=None)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Display HTML page with state and its cities."""
    all_states = storage.all(State)
    state = all_states.get('State.' + id)
    return render_template('9-states.html', states=None, state=state)


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
