import flask
import threading
from config import Configuration
from elevator import ElevatorManager

app = flask.Flask(__name__)
app.config.from_object(Configuration)

manager = ElevatorManager()

from views import *
