class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

class Passenger(Person):
    def __init__(self, id, first_name, last_name, car_number, seat):
        super().__init__(first_name, last_name)
        self.id = id
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
    
    def change_number(self, number):
        self.__number = number
        for item in self.__passangers:
            item.car_number = number
    
    def delete_passanger(self, id):
        for i in range(len(self.__passangers)):
            if self.__passangers[i-1].id == id:
                self.__passangers.pop(i-1)


class Conductor(Person):
     def __init__(self, first_name, last_name, car:Car):
          super().__init__(first_name, last_name)
          self.car = car
          self.first_name = first_name
          self.last_name = last_name

     def add_passanger(self, passanger: Passenger):
         self.car.add_passanger(passanger)
     
     def delete_passanger(self, passanger: Passenger):
         self.car.delete_passanger(passanger.id)


def main():
    car = Car(1)

    conductor = Conductor('Dmutro', 'Sergiyovuch', car)

    ivan = Passenger(1, 'Ivan', 'Ivanovuch', 1, 1)

    olya = Passenger(2, 'Olya', 'Berezkina', 1, 2)
    
    print('Додаємо пасажирів') # Додаємо пасажирів через кондуктора
    conductor.add_passanger(ivan)
    conductor.add_passanger(olya)

    print([f'{k.full_name}' for k in car.passangers])
    print([f'{k.full_name} car:{k.car_number}' for k in car.passangers])

    car.change_number(2)

    print([f'{k.full_name} car:{k.car_number}' for k in car.passangers])

    print([f'{k.full_name} id:{k.id}' for k in car.passangers])

    conductor.delete_passanger(olya)

    print([f'{k.full_name} id:{k.id}' for k in car.passangers])

main()