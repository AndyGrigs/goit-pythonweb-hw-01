from abc import ABC, abstractmethod
from logger import logging

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass
       

class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make:str, model:str)-> Vehicle:
        return Car(f"{make} {model} USA", model)
    def create_motorcycle(self, make:str, model:str)-> Vehicle:
        return Motorcycle(f"{make} {model} USA", model)
    
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make:str, model:str)-> Vehicle:
        return Car(f"{make} {model} EU", model)
    def create_motorcycle(self, make:str, model:str)-> Vehicle:
        return Motorcycle(f"{make} {model} EU", model)
 
# Використання
factory = USVehicleFactory()
car1 = factory.create_car("Ford", "Mustang")
car1.start_engine()
factory = EUVehicleFactory()
motorcycle1 = factory.create_car("BMW", "R12")
motorcycle1.start_engine()
