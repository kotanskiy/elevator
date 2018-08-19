import threading
import unittest
from time import sleep

from app import run_elevator, app
from elevator import ElevatorManager


class ViewsManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.manager = ElevatorManager()
        for elevator in self.manager.elevators:
            threading.Thread(target=run_elevator, kwargs={'manager': self.manager, 'elevator': elevator})

    def test_on_up(self):
        self.app.get('/on_up/1')
        sleep(5)
        response = self.app.get('/on_up/1')
        assert b'count of passengers: 0 max passengers: 6 current floor: 1 selected floors: set() id: 1' == response.data
        response = self.app.get('/on_up/0')
        assert b'Floor does not exist' == response.data
        response = self.app.get('/on_up/5')
        assert b'top floor' == response.data
        response = self.app.get('/on_up/6')
        assert b'Floor does not exist' == response.data

    def test_on_down(self):
        self.app.get('/on_up/1')
        sleep(5)
        response = self.app.get('/on_down/1')
        assert b'bottom floor' == response.data
        response = self.app.get('/on_down/0')
        assert b'Floor does not exist' == response.data
        response = self.app.get('/on_down/5')
        assert b'count of passengers: 0 max passengers: 4 current floor: 3.0 selected floors: {5} id: 0' == response.data
        response = self.app.get('/on_down/6')
        assert b'Floor does not exist' == response.data

    def test_load_passenger(self):
        response = self.app.get('/load_passenger/0/1')
        assert b'Are you on this floor' == response.data
        response = self.app.get('/load_passenger/1/1')
        assert b'Are you on this floor' == response.data
        response = self.app.get('/load_passenger/0/3')
        assert b'count of passengers: 1 max passengers: 4 current floor: 1 selected floors: {3}' == response.data
        response = self.app.get('/load_passenger/2/3')
        assert b'Elevator does not exist' == response.data
        response = self.app.get('/load_passenger/0/6')
        assert b'Floor does not exist' == response.data


if __name__ == '__main__':
    unittest.main()
