from abc import ABC, abstractmethod

# Abstract Products


class Car(ABC):
    @abstractmethod
    def drive(self) -> None:
        pass


class Truck(ABC):
    @abstractmethod
    def haul(self) -> None:
        pass


# Concrete Products


class ElectricCar(Car):
    def drive(self) -> None:
        print("Driving an Electric car...")


class GasolineCar(Car):
    def drive(self) -> None:
        print("Driving a Gasoline car...")


class ElectricTruck(Truck):
    def haul(self) -> None:
        print("Hauling cargo in an Electric truck...")


class GasolineTruck(Truck):
    def haul(self) -> None:
        print("Hauling cargo in a Gasoline truck...")


# Abstract Factory


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_truck(self) -> Truck:
        pass


# Concrete Factories


class ElectricVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return ElectricCar()

    def create_truck(self) -> Truck:
        return ElectricTruck()


class GasolineVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return GasolineCar()

    def create_truck(self) -> Truck:
        return GasolineTruck()


# Client


def client_code(factory: VehicleFactory) -> None:
    car = factory.create_car()
    car.drive()

    truck = factory.create_truck()
    truck.haul()


def main():
    electric_factory = ElectricVehicleFactory()
    client_code(electric_factory)

    gasoline_factory = GasolineVehicleFactory()
    client_code(gasoline_factory)


main()
