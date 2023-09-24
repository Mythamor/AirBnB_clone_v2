#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb')
def html_all_filters():
    """display html page w/ working city/state filters & amenities/properties
       runs with web static css files
    """
    state_objs = [s for s in storage.all(State).values()]
    amenity_objs = [a for a in storage.all(Amenity).values()]
    place_objs = [p for p in storage.all(Place).values()]
    user_objs = [u for u in storage.all(User).values()]
    place_owner_objs = []
    for place in place_objs:
        for user in user_objs:
            if place.user_id == user.id:
                place_owner_objs.append(["{} {}".format(
                    user.first_name, user.last_name), place])
    place_owner_objs.sort(key=lambda p: p[1].name)
    return render_template('100-hbnb.html',
                           state_objs=state_objs,
                           amenity_objs=amenity_objs,
                           place_owner_objs=place_owner_objs)



if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000, debug=True)
