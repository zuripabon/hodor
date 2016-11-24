# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = True

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Server's IP address
HOST="0.0.0.0"

# Server's port
PORT=8080

# Time GPIO pin will be high
GPIO_HIGH_TIME=1

# GPIO pin used for the joining door
GPIO_JOIN=17

# GPIO pin used for the leaving door
GPIO_LEAVE=22
