# Import flask dependencies
from flask import Blueprint
from pi import join as join_pi, leave as leave_pi

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_pi = Blueprint('pi', __name__, url_prefix='/pi')

# Set the route and accepted methods
@mod_pi.route('/join', methods=['GET'])
def join():
    join_pi()
    return "join"

# Set the route and accepted methods
@mod_pi.route('/leave', methods=['GET'])
def leave():
    leave_pi()
    return "leave"
