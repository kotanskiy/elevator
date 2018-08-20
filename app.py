import flask
import threading
from config import Configuration
from elevator import ElevatorManager, event

app = flask.Flask(__name__)
app.config.from_object(Configuration)

manager = ElevatorManager()


def run_elevator(manager, elevator):
    while True:
        event.wait()
        manager.move_elevator_to_next_floor(elevator)
        event.clear()


for elevator in manager.elevators:
    threading.Thread(target=run_elevator, kwargs={'manager': manager, 'elevator': elevator}, daemon=True).start()


from views import *
