class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

        
    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')
    
myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

myCar.talk('Michael')

class Race:
    def __init__(self, name, driver_limit):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)

    def get_average_ranking(self):
        total_ranking = 0
        for driver in self.drivers:
            total_ranking += driver.ranking

        return total_ranking / len(self.drivers)

my_course = Race('Seattle 500', 4)
print(my_course.name, my_course.driver_limit, my_course.drivers)

class Driver:
    number_of_drivers = 0

    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1

    def get_ranking(self):
        return self.ranking
    
driver_1 = Driver('Lewis Hamilton', 36, 83)
driver_2 = Driver('Eliud Kipchoge', 36, 95)
driver_3 = Driver('Sebastion Vettel', 34, 76)
driver_4 = Driver('Lightning McQueen', 32, 10)

my_course.add_driver(driver_1)
my_course.add_driver(driver_2)
my_course.add_driver(driver_3)
my_course.add_driver(driver_4)

print(my_course.get_average_ranking())
print(driver_1.number_of_drivers)

my_driver = Driver('Dale Earnhardt', 29, 100)
print(my_driver.get_ranking())