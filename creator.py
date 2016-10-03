import abc
from abc import ABCMeta

class Pizza:
    def __init__(self):
        self.masa = None
        self.salsa = None
        self.relleno = None

    def doSomethig(self):
        print("{masa} - {salsa} - {relleno}".format(
            masa=self.masa, salsa=self.salsa, relleno=self.relleno
        ))

class PizzaBuilder:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.pizza = None

    def createNewPizza(self):
        self.pizza = Pizza()

    @abc.abstractmethod
    def buildMasa(self):
        pass

    @abc.abstractmethod
    def buildSalsa(self):
        pass

    @abc.abstractmethod
    def buildRelleno(self):
        pass

class HawaiPizzaBuilder(PizzaBuilder):
    def buildMasa(self):
        self.pizza.masa = 'suave'

    def buildSalsa(self):
        self.pizza.salsa = 'dulce'

    def buildRelleno(self):
        self.pizza.relleno = 'chorizo+alcachofa'

class PicantePizzaBuilder(PizzaBuilder):
    def buildMasa(self):
        self.pizza.masa = 'cocida'

    def buildSalsa(self):
        self.pizza.salsa = 'picante'

    def buildRelleno(self):
        self.pizza.relleno = 'pimienta+salchichon'

class Cocina:
    def __init__(self):
        self.pizzaBuilder = None

    def setPizzaBuilder(self, pizzaBuilder):
        self.pizzaBuilder = pizzaBuilder

    def buildPizza(self):
        self.pizzaBuilder.createNewPizza()
        self.pizzaBuilder.buildMasa()
        self.pizzaBuilder.buildSalsa()
        self.pizzaBuilder.buildRelleno()

cocina = Cocina()

hawaiPizzaBuilder = HawaiPizzaBuilder()
cocina.setPizzaBuilder(hawaiPizzaBuilder)
cocina.buildPizza()
cocina.pizzaBuilder.pizza.doSomethig()

picantePizzaBuilder = PicantePizzaBuilder()
cocina.setPizzaBuilder(picantePizzaBuilder)
cocina.buildPizza()
cocina.pizzaBuilder.pizza.doSomethig()
