from app import app
from config import HOST, PORT, DEBUG

__author__ = "Alberto Garcia, Zuri Pabon"
__credits__ = ["Alberto Garcia", "Zuri Pabon"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Zuri Pabon"
__email__ = "jgarcia@itrsgroup.com, zpabon@itrsgroup.com"
__status__ = "beta"

# @TODO Read host and port from cli
app.run(host=HOST, port=PORT, debug=DEBUG)
