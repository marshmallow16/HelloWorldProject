from abc import ABC,abstractmethod

#Product interface
class vehicle(ABC):
	@abstractmethod
	def drive(self):
		pass

#Concrete class
class car(vehicle):
	def drive(self):
		return "Driving a car"

class bike(vehicle):
	def drive(self):
		return "Driving from class bike"

#to understand abstract principles and enforce consistency, consistent interface for all concrete factories. This ensures that all factories provide the same method #for creating objects, making the system easier to understand and maintain.

class vehicleFactory(ABC):
	@abstractmethod
	def create_vehicle(self):
		pass

class CarFactory(vehicleFactory):
    def create_vehicle(self):
        return car()

class BikeFactory(vehicleFactory):
    def create_vehicle(self):
        return bike()

#factory is instance of vehicleFactory which is car factory when client_code(car_factory) 
def client_code(factory: vehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.drive())

# Usage
if __name__ == "__main__":
    car_factory = CarFactory()
    client_code(car_factory)  # Output: Driving a car

    bike_factory = BikeFactory()
    client_code(bike_factory)  # Output: Riding a bike

