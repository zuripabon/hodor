# Import flask dependencies
from flask import Blueprint, render_template

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_home = Blueprint('home', __name__)

# Set the route and accepted methods
@mod_home.route('/', methods=['GET'])
def home():
    return render_template("home/index.html")
