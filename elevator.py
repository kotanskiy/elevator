from time import sleep


class Elevator:
    max_count_of_floors = 5

    def __init__(self, speed, max_count_of_people):
        self.passengers = []
        self.speed = speed
        self.max_count_of_people = max_count_of_people
        self.current_floor = 1
        self.vector = 0
        self.selected_floors = set()

    def __str__(self):
        return 'count of passengers: {} max passengers: {} current floor: {} selected floors: {}'.format(
            len(self.passengers), self.max_count_of_people, self.current_floor, self.selected_floors)

    def move_to_per_step(self, floor):
        if floor < 1 or floor > Elevator.max_count_of_floors or not isinstance(floor, int):
            raise RuntimeError('Floor does not exist')
        if floor > self.current_floor:
            self.vector = self.speed
        else:
            self.vector = - self.speed
        if floor != round(self.current_floor):
            self.current_floor += self.vector
        else:
            self.current_floor = round(self.current_floor)
            self.vector = 0
            print('Elevator arrived on the {}th floor'.format(self.current_floor))

    def load_passenger(self, selected_floor_by_passenger):
        if selected_floor_by_passenger < 1 or selected_floor_by_passenger > Elevator.max_count_of_floors:
            raise RuntimeError('Floor does not exist')
        if len(self.passengers) + 1 > self.max_count_of_people:
            raise RuntimeError('No place in this elevator')
        self.passengers.append({'selected_floor': selected_floor_by_passenger})
        self.selected_floors.add(selected_floor_by_passenger)

    def upload_passengers(self, current_floor):
        for passenger in self.passengers:
            if passenger['selected_floor'] == current_floor:
                self.passengers.remove(passenger)
        self.selected_floors.remove(current_floor)


class ElevatorManager:
    def __init__(self):
        self.elevators = [Elevator(0.5, 4), Elevator(0.3, 6)]

    def on_up(self, current_floor):
        for elevator in self.elevators:
            if elevator.current_floor <= current_floor and elevator.vector >= 0:
                if elevator.current_floor != current_floor:
                    elevator.selected_floors.add(current_floor)
                return elevator, self.elevators.index(elevator)

    def on_down(self, current_floor):
        for elevator in self.elevators:
            if elevator.current_floor >= current_floor and elevator.vector <= 0:
                if elevator.current_floor != current_floor:
                    elevator.selected_floors.add(current_floor)
                return elevator, self.elevators.index(elevator)

    def move_elevator_to_next_floor(self, elevator):
        if elevator.selected_floors:
            distances = []
            for floor in elevator.selected_floors:
                distances.append({'distance': abs(floor - elevator.current_floor), 'floor': floor})
            next_floor = min(distances, key=lambda distance: distance['distance'])['floor']
            while elevator.current_floor != next_floor:
                sleep(1)
                elevator.move_to_per_step(next_floor)
            else:
                elevator.upload_passengers(elevator.current_floor)
