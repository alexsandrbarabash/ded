import os

# функція для вода чисел
def input_num(text):
    while True:
        num = input(text)
        if num.isdigit():
            return int(num)

# функція для очистки консолі
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    # метод отримання повного імені
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

# пасажир
class Passenger(Person):
    def __init__(self, id, first_name, last_name, car_number, seat):
        super().__init__(first_name, last_name)
        self.id = id
        self.car_number = car_number
        self.seat = seat

# вагон
class Car:
    __passangers = []
    def __init__(self, number):
        self.__passangers = [] # очищаєм пасажирів
        self.__number = number
 
    def add_passanger(self, passanger: Passenger):
        # перевірка на правильність номера вагона
        if passanger.car_number == self.__number:
             self.__passangers.append(passanger)
        else:
             print(f'You mistake a car: {passanger.full_name}') # виводим помилку якщо номер не співпадає
    
    # метод для отримання всіх пасажирів що в вагоні
    @property
    def passangers(self):
        return self.__passangers

    # отримання номера вагона
    @property
    def number(self):
        return self.__number
    
    # зміна номера вагона
    def change_number(self, number):
        self.__number = number
        # міняємо номер вагона і в пасажирів що в вагоні
        for item in self.__passangers:
            item.car_number = number

    # видалення пасажирів по id
    def delete_passanger(self, id):
        for i in range(len(self.__passangers)):
            if self.__passangers[i-1].id == id:
                self.__passangers.pop(i-1)

# кондуктор
class Conductor(Person):
     def __init__(self, first_name, last_name, car:Car):# для створення кондутора потрібно створити вагон
          super().__init__(first_name, last_name)
          self.car = car
          self.first_name = first_name
          self.last_name = last_name

     # добавляємо кондуктору можливість додавати пасажирів
     def add_passanger(self, passanger: Passenger):
         self.car.add_passanger(passanger)

     # добавляємо кондуктору можливість видаляти пасажирів
     def delete_passanger(self, passanger: Passenger):
         self.car.delete_passanger(passanger.id)


def game_in_conductor():
    car_new = Car(input_num('Enter car number for start '))
    conductor = Conductor('Nazar', 'Victorovuch', car_new)
    counter = 0
    while True:
        print('1) Add passanger to car')
        print('2) Show all pessanger')
        print('3) Delete passanger to car')
        print('4) Get number car')
        print('5) Change number to car')
        print('6) Clear')
        action = input('Select action:')
        if action == '1':
            first_name = input('First name: ')
            last_name = input('Last name: ')
            car_number = input_num('Car number: ')
            seat_number = input_num('Seat number: ')
            conductor.add_passanger(Passenger(counter, first_name, last_name, car_number, seat_number))
            counter = counter + 1

        if action == '2':
            print([f'{k.full_name} car:{k.car_number} id:{k.id}' for k in car_new.passangers])
        
        if action == '3':
            car_new.delete_passanger(input_num('Id: '))
        
        if action == '4':
            print(car_new.number)

        if action == '5':
            car_new.change_number(input_num('Car number: '))

        if action == '6':
            clearConsole()


def main():
    car = Car(1) # ініціалізация вагона

    conductor = Conductor('Dmutro', 'Sergiyovuch', car) # ініціалізация кондуктора

    # ініціалізация пасажирів
    ivan = Passenger(1, 'Ivan', 'Ivanovuch', 1, 1)

    olya = Passenger(2, 'Olya', 'Berezkina', 1, 2)
    petro = Passenger(3, 'Petro', 'Petrenko', 1, 4)
    korneliys = Passenger(4, 'Korneliys', 'Gats', 2, 3)
    
    # Додаємо пасажирів через кондуктора
    conductor.add_passanger(ivan)
    conductor.add_passanger(olya)
    conductor.add_passanger(petro)

    conductor.add_passanger(korneliys) # Виведе помилку

    print('Додані пасажири:')
    print([f'{k.full_name}' for k in car.passangers]) # Виводим всіх пасажирів в вагоні

    print('\n Міняєм номер вагона') 
    car.change_number(2)

    print([f'{k.full_name} car:{k.car_number}' for k in car.passangers]) # Виводим всіх пасажирів в вагоні з його номером

    print('\n Пасажири з id:') 
    print([f'{k.full_name} id:{k.id}' for k in car.passangers])

    print('\n Видаляємо Олю:')
    conductor.delete_passanger(olya)

    print([f'{k.full_name} id:{k.id}' for k in car.passangers])
    
    print('\n\nStart game\n')
    # запускаємо гру
    game_in_conductor()

main()