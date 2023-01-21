from BestBusCompany.BusRoute import BusRoute
from BestBusCompany.SchedulRide import ScheduledRide


class ManagerMenu:
    def __init__(self, name=None, password=None):
        self._name = name
        self.__password = password
        self.routes = {}
        self.scheduled_rides = {}

    def add_route(self, line_number, origin, destination, stops):
        self.routes[line_number] = BusRoute(line_number, origin, destination, stops)

    def delete_route(self, line_number):
        if line_number not in self.routes:
            raise ValueError('Route with line number {} does not exist.'.format(line_number))

        self.routes.pop(line_number)
        self.scheduled_rides = {k: v for k, v in self.scheduled_rides.items() if v.line_number != line_number}

    def update_route(self, line_number, **kwargs):
        if line_number not in self.routes:
            raise ValueError('Route with line number {} does not exist.'.format(line_number))

        route = self.routes[line_number]
        for key, value in kwargs.items():
            setattr(route, key, value)

    def add_scheduled_ride(self, line_number, origin_time, destination_time, driver_name):
        if line_number not in self.routes:
            raise ValueError(f'Route with line number {line_number} does not exist.')

        ride = ScheduledRide(line_number, origin_time, destination_time, driver_name)
        self.scheduled_rides[ride.id] = ride
