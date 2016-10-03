from abc import ABCMeta, abstractmethod

class CarFactory(metaclass=ABCMeta):
    @staticmethod
    def getFactory(factoryName):
        if factoryName == 'nissan':
            return NissanFactory()
        elif factoryName == 'porsche':
            return PorscheFactory()
        raise 'Unknown factory name'

class NissanFactory:
    def createCar(self, carModel):
        if carModel == 'sentra':
            return NissanSentra()
        elif carModel == 'patrol':
            return NissanPatrol()
        raise 'Unknown car model'

class PorscheFactory:
    def createCar(self, carModel):
        if carModel == 'boxster':
            return PorscheBoxster()
        elif carModel == 'cayman':
            return PorscheCayman()
        raise 'Unknown car model'

class Car(metaclass=ABCMeta):
    def __init__(self):
        self.model = None
        self.brand = None

    def __str__(self):
        return "{brand} - {model}".format(brand=self.brand, model=self.model)

class NissanSentra(Car):
    def __init__(self):
        self.model = 'Sentra'
        self.brand = 'Nissan'

class NissanPatrol(Car):
    def __init__(self):
        self.model = 'Patrol'
        self.brand = 'Nissan'

class PorscheBoxster(Car):
    def __init__(self):
        self.model = 'Boxster'
        self.brand = 'Porsche'

class PorscheCayman(Car):
    def __init__(self):
        self.model = 'Cayman'
        self.brand = 'Porsche'

factory = CarFactory.getFactory('porsche')
car = factory.createCar('cayman')
print(car)
