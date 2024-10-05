from abc import ABCMeta, abstractmethod
from enum import Enum


class DogBreed(Enum):
    POODLE = "poodle"
    ROTTWEILER = "rottweiler"
    HUSKY = "husky"


class Dog(metaclass=ABCMeta):
    @abstractmethod
    def bark(self) -> str:
        pass


class Poodle(Dog):
    def bark(self) -> str:
        return 'The Poodle says "yap"'


class Rottweiler(Dog):
    def bark(self) -> str:
        return 'The Rottweiler says "ruff"'


class SiberianHusky(Dog):
    def bark(self) -> str:
        return 'The Siberian Husky says "woof"'

    def howl(self) -> str:
        return 'The Siberian Husky says "Awoooooo"'


def get_dog(dog: DogBreed) -> Dog:
    if dog == DogBreed.POODLE:
        return Poodle()
    elif dog == DogBreed.ROTTWEILER:
        return Rottweiler()
    elif dog == DogBreed.HUSKY:
        return SiberianHusky()
    else:
        raise ValueError(f"Invalid dog type: {dog}")


def main():
    print(get_dog(DogBreed.POODLE).bark())
    print(get_dog(DogBreed.ROTTWEILER).bark())
    print(get_dog(DogBreed.HUSKY).bark())


main()
