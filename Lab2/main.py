class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

class Passenger(Person):
    def __init__(self, first_name, last_name, car_number, seat):
        super().__init__(first_name, last_name)
        self.car_number = car_number
        self.seat = seat

class Car:
    __passangers = []
    def __init__(self, number):
        self.__number = number

    def add_passanger(self, passanger: Passenger):
        if passanger.car_number == self.__number:
             self.__passangers.append(passanger)
        else:
             print('You mistake a car')

    @property
    def passangers(self):
        return self.__passangers

    @property
    def number(self):
        return self.__number

class Conductor(Person):
     def __init__(self, first_name, last_name, car:Car):
          super().__init__(first_name, last_name)
          self.car = car
          self.first_name = first_name
          self.last_name = last_name

     def add_passanger(self, passanger: Passenger):
         self.car.add_passanger(passanger)

car = Car(1)

conductor = Conductor('Dmutro', 'Sergiyovuch', car)

ivan = Passenger('Ivan', 'Ivanovuch', 1, 1)

olya = Passenger('Olya', 'Berezkina', 1, 2)

conductor.add_passanger(ivan)
conductor.add_passanger(olya)

print([f'{k.first_name} {k.last_name}' for k in car.passangers])