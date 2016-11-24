# Import flask and template operators
from flask import Flask, render_template

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_home.controllers import mod_home
from app.mod_pi.controllers import mod_pi

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# Register blueprint(s)
app.register_blueprint(mod_home)
app.register_blueprint(mod_pi)
