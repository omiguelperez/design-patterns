from abc import ABCMeta, abstractmethod

class Dog(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass

class Poodle(Dog):
    def speak(self):
        print("The poodle says \"arf\"")

class Rottweiler(Dog):
    def speak(self):
        print("The Rottweiler says (in a very deep voice) \"WOOF!\"")

class SiberianHusky(Dog):
    def speak(self):
        print("The husky says \"Dude, what's up?\"")

class DogFactory(metaclass=ABCMeta):
    @staticmethod
    def getDog(type):
        if type == 'small':
            return Poodle()
        elif type == 'big':
            return Rottweiler()
        elif type == 'working':
            return SiberianHusky()
        raise "Unknown dog type"
