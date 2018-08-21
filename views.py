from app import *


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/on_up/<int:current_floor>')
def on_up(current_floor):
    try:
        elevator, id = manager.on_up(current_floor)
    except RuntimeError as error:
        return flask.Response(str(error))
    return flask.Response(str(elevator) + ' id: {}'.format(id))


@app.route('/on_down/<int:current_floor>')
def on_down(current_floor):
    try:
        elevator, id = manager.on_down(current_floor)
    except RuntimeError as error:
        return flask.Response(str(error))
    return flask.Response(str(elevator) + ' id: {}'.format(id))


@app.route('/load_passenger/<int:id>/<int:selected_floor>')
def load_passenger(id, selected_floor):
    try:
        elevator = manager.elevators[id]
        elevator.load_passenger(selected_floor)
    except RuntimeError as error:
        return flask.Response(str(error))
    except IndexError:
        return flask.Response('Elevator does not exist')
    return flask.Response(str(elevator))


@app.route('/elevator_state/<int:id>')
def elevator_state(id):
    try:
        elevator = manager.elevators[id]
        return flask.Response(str(elevator) + ' id: {}'.format(id))
    except IndexError:
        return flask.Response('Elevator does not exist')




