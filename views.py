from app import *


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/on_up/<int:current_floor>')
def on_up(current_floor):
    elevator, id = manager.on_up(current_floor)
    return flask.Response(str(elevator) + ' id: {}'.format(id))


@app.route('/on_down/<int:current_floor>')
def on_down(current_floor):
    elevator, id = manager.on_up(current_floor)
    return flask.Response(str(elevator) + ' id: {}'.format(id))


@app.route('/load_passenger/<int:id>/<int:selected_floor>')
def load_passenger(id, selected_floor):
    elevator = manager.elevators[id]
    elevator.load_passenger(selected_floor)
    return flask.Response(str(elevator))


@app.route('/move_elevator/<int:id>')
def move_elevator(id):
    elevator = manager.elevators[id]
    manager.move_elevator_to_next_floor(elevator)
    return flask.Response(str(elevator))




