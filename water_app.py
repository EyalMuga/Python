import os
import pickle
from datetime import datetime
import random


class ScheduledRides:
    def __init__(self, origin_time: int, destination_time: int, driver_name: str, delays=None):
        self.id = id
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.driver_name = driver_name
        self.delays: list = delays

    def __str__(self):
        return f'id:{self.id} origin_time:{self.origin_time} destination_time:{self.destination_time} driver name: {self.driver_name}'

    def __repr__(self):
        return f'id:{self.id} origin_time:{self.origin_time} destination_time:{self.destination_time}'

    def get_dict_s(self):
        s_dict = {}
        s_dict['origin_time'] = self.origin_time
        s_dict['destination_time'] = self.destination_time
        s_dict['delays'] = self.delays
        return s_dict

    #
    def add_delay(self, delay_min):
        self.delays.append(delay_min)


class Bus:
    def __init__(self, company: best_bus.BestBusCompany):
        self._company: best_bus.BestBusCompany = company

    def select(self, massage, low_option, high_option) -> int:
        print(massage)
        while True:
            a = input('select  ')
            if not a.isnumeric():
                print('please enter a number:')
                continue
            b = int(a)
            if b < low_option or b > high_option:
                print(f'please enter a number between {low_option} {high_option}: ')
                continue
            return b

    def top_menu(self):
        men1 = self.select("[1] for Manager type 1 \n[2] for Passenger type 2", 1, 2)

        if men1 == 1:
            if not self.password():
                return
            self.menu_manager()

        if men1 == 2:
            self.menu_passenger()

    def password(self) -> bool:
        for i in range(0, 3):
            p = input("please enter password here:  ")
            if p == "3":
                return True
        print('password is incorrect')
        return False

    def menu_manager(self) -> int:
        while True:
            menu_man = self.select(
                "[1] add_route \n[2] delete_route \n[3] update_route \n[4] add_schedule \n[5] company_info \n[6] quit",
                1, 6)
            match (menu_man):
                case 1:
                    self.add_route()
                case 2:
                    self.delete_route()
                case 3:
                    self.update_route()
                case 4:
                    self.add_schedule()
                case 5:
                    self.company_info()
                case 6:
                    return

    def add_route(self):
        line = self.select("please enter line number: ", 1, 1000)
        add = input("please type origin, destination and stops, comma seperated: ")
        add1 = add.split(',')
        if len(add1) < 3:
            print('wrong input')
            return
        stops = []
        for i in range(2, len(add1)):
            stops.append(add1[i])
        self._company.add_route(line, add1[0], add1[1], stops)

    def delete_route(self):
        line_to_del = self.select("please type the line number you would like to delete: ", 1, 1000)
        # checks if line number exists:
        if not self._company.is_line(line_to_del):
            print(f'the line number:{line_to_del} does not exist!')
        if self._company.is_line(line_to_del):
            q = input("are you sure you want to delete this route? type: y/n")
            if q != 'y':
                print('no line has been deleted!')
                return
            self._company.delete_route(line_to_del)
            print(f'line {line_to_del} has been deleted!')

    def add_schedule(self):
        line_number = self.select("please select the line you would like to add schedule to: ", 1, 1000)
        if self._company.is_line(line_number):
            add_s = input("please add the origin time, destination time and driver name, comma seperated: ")
            sch = add_s.split(',')
            if len(sch) != 3:
                return
            origin_time, destination_time, driver_name = sch[0], sch[1], sch[2]
            print("the schedule has been added to the route!")
            self._company.broute(line_number).add_schedule(origin_time, destination_time, driver_name)

    def update_route(self):
        line_to_update = self.select("please type the line number you would like to update: ", 1, 1000)
        # checks if line number exists:
        if not self._company.is_line(line_to_update):
            print(f'the line number:{line_to_update} does not exist!')
        if self._company.is_line(line_to_update):
            origin = input("please enter the origin")
            destination = input("please enter the destination")
            stops = input('please enter the list of stops, comma seperated')
            list_stops = []
            for s in range(0, len(stops)):
                list_stops.append(s)
            print("the route has been updated!")
            self._company.update_route(origin, destination, list_stops)

    # presents all the info on all routes and schedules:
    def company_info(self):
        print(self._company.BusRoute())

    def menu_passenger(self):
        menu_pas = self.select("[1] search_route \n [2] add_delay \n [3] quit", 1, 3)
        match (menu_pas):
            case 1:
                self.search_route()
            case 2:
                self.add_delay()
            case 3:
                self.top_menu()

    def search_route(self):
        search_field = self.select(
            "please select the field you would like to search by:\n [1] line_number \n [2] origin \n [3] destination \n [4] stops \n [5] quit",
            1, 5)
        match (search_field):
            case 1:
                self.search_byline()
            case 2:
                self.search_origin()
            case 3:
                self.search_destination()
            case 4:
                self.search_bystops()
            case 5:
                return

    def add_delay(self):
        line = self.select("please insert the line you would like to report the delay:", 1, 1000)
        if not self._company.is_line(line):
            print(f'the line number:{line} does not exist!')
        if self._company.is_line(line):
            print("this is the information for line {line}: ")
            print(self._company.broute(line))
            id = int(input('enter the bus ride id from the list above: '))
            delay = int(input("please enter the number of minutes of the delay: "))
            print(f"thank you for adding delay for line number {line}, id: {id}!")
            return self._company.broute(line).add_delay(delay, id)

    def search_origin(self):
        origin = input("please insert the origin would like to search: ")
        for l in self._company.search_origin(origin):
            print(self._company.display_route_by(l))
        print(f'origin {origin} not found')

    def search_destination(self):
        destination = input("please insert the destination would like to search: ")
        for l in self._company.search_destination(destination):
            print(self._company.display_route_by(l))
        print(f'destination {destination} not found')

    def search_byline(self):
        line_number = self.select("please insert the line you would like to search: ", 1, 1000)
        if self._company.is_line(line_number):
            print(self._company.display_route_by(line_number))
        print('no such line number')

    def search_bystops(self):
        station = input("please insert the station you would like to search by: ")
        for l in self._company.search_station(station):
            print(self._company.display_route_by(l))


class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_stops: list):
        self.origin = origin
        self.destination = destination
        self.list_stops = list_stops
        self._bus_schedule = {}
        self._line_number: int = line_number

    def __str__(self) -> str:
        return f'line_number: {self._line_number} \n origin: {self.origin} \n destination: {self.destination} \n list_stops: {self.list_stops} \n bus_schedule: {self._bus_schedule}'

    def __repr__(self):
        return self.__str__()

    def search_origin(self, origin) -> bool:
        return self.origin == origin

    def search_destination(self, destination) -> bool:
        return self.destination == destination

    def search_station(self, station) -> bool:
        return station in self.list_stops

    def add_delay(self, delay_min):
        return self._bus_schedule[id].add_delay(delay_min)

    # def get_schedule(self):
    #     return self._bus_schedule

    def display_r(self):
        print(self.__str__())
        for s in self._bus_schedule:
            print(self._bus_schedule[s])

    # def update_route(self, origin, destination, list_stops:list):
    #     # for BusRoute[line_number]:
    #     self.origin = origin
    #     self.destination= destination
    #     self.list_stops = list_stops

    # adds the object to self._bus_schedule = {}
    def add_schedule(self, origin_time: int, destination_time: int, driver_name: str):
        s = schedule.ScheduledRides(origin_time, destination_time, driver_name)
        id: int = int(random.randrange(1, 1000))
        self._bus_schedule[id] = origin_time, destination_time, driver_name

    # adds delay to list of delays in self._bus_schedule by schedule class:
    def add_delay(self, delay, id):
        # d = schedule.ScheduledRides(delays)
        self._bus_schedule[id] = delay

    def get_sc_dict(self):
        print(self._bus_schedule)


class BestBusCompany:
    def __init__(self):
        self.__bus_route: {classmethod} = {}

    # when adding schedule, returns bus route object:
    def broute(self, line: int) -> busroute:
        return self.__bus_route[line]

    def display_c(self):
        return self.__bus_route

    def display_route_by(self, line_number):
        return self.__bus_route[line_number]

    def display_route(self):
        print(self.__bus_route)

    # adds object from type busroute (class) to bus_route dict:
    def add_route(self, line_number, origin, destination, list_stops) -> bool:
        if line_number in self.__bus_route:
            return False
        b = busroute.BusRoute(line_number, origin, destination, list_stops)
        self.__bus_route[line_number] = b
        return True

    def delete_route(self, line_number) -> bool:
        if not line_number in self.__bus_route:
            return False
        if line_number in self.__bus_route:
            del self.__bus_route
            print(f'line {line_number} has been deleted')
        else:
            print('no such line number')
            return

    def update_route(self, origin, destination, list_stops: list):
        # for BusRoute[line_number]:
        self.origin = origin
        self.destination = destination
        self.list_stops = list_stops

    # searches for stations and returns list of lines that include this station:
    def search_station(self, station) -> list:
        stops_lst = []
        for line in self.__bus_route:
            if self.__bus_route[line].search_station(station):
                stops_lst.append(line)
        return stops_lst

    # searches for origin and returns list of lines that include this origin:
    def search_origin(self, origin) -> list:
        origin_lst = []
        for line in self.__bus_route:
            if self.__bus_route[line].search_origin(origin):
                origin_lst.append(line)
        return origin_lst

    # searches for destination and returns list of lines that include this destination:
    def search_destination(self, destination) -> list:
        dest_lst = []
        for line in self.__bus_route:
            if self.__bus_route[line].search_destination(destination):
                dest_lst.append(line)
        return dest_lst

    # checks if line exists in route:
    def is_line(self, line_number) -> bool:
        if line_number in self.__bus_route:
            return True
        else:
            return False

    def add_delay(self, delay_min, id):
        return self.__bus_route.add_delay(delay_min, id)
#
# company = BestBusCompany()
# company.add_route(4,'telaviv','raanana',['aaa','bbb'])
# company.add_route(6,'telaviv','raanana',['aah','jbb'])
# company.broute(4).add_schedule(9,10,"Moshe")
# # print(company.display_route_by(4))
# print(company.search_origin('telaviv'))

# company.broute(4).add_schedule(9,10,"Moshe")
# company.broute(4).update_route('yy','bb',['mk','dr','se'])
# print(company.display_c())
# # company.search_items_val('origin', 'telaviv')


# a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# # b = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# # c = BusRoute(5,'bal', 'rm', ['aaa','bbb'])
# a.add_schedule(3,4,'noa')
# print(a.add_delay(4,5))
# print(a.__str__())
# a.add_schedule(4,5,'noaded')
# print(a.get_schedule())
#
# a.add_schedule(9,11,'noa')
# # a.search_route('origin', 'tkklko')
#
# print(a.get_dict(9,11,'noa'))

# print(a.my_s_dict)
# a.__str__()
# #
# for i in d['bus_schedule']:
#     a.add_delay(i,5)
# print(a.get_dict(),'ooo')
# a.display_r()


# a.search_route('origin', 'telaviv')

# print(a)
# a.add_schedule(9,10,'noa')
# s.search('origin','telaviv')

if __name__ == '__main__':

    if not os.path.exists('company.pickle'):
        company = best_bus.BestBusCompany()
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('company.pickle', 'rb') as fh:
            company = pickle.load(fh)


    b = menu.Bus(company)
    b.top_menu()
    # company.add_route(1,'gtv','nui','ijo')
    # company.broute(1).add_schedule(3,4,'noa')
    # company.display_c()


    file = open('company.pickle', 'wb')
    pickle.dump(company, file)