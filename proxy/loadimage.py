from abc import ABCMeta, abstractmethod


class Image(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.loadFromDisk()

    def loadFromDisk(self):
        print("Loading {filename}".format(filename=self.filename))

    def display(self):
        print("Displaying {filename}".format(filename=self.filename))

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.realImage = None

    def display(self):
        if self.realImage == None:
            self.realImage = RealImage(self.filename)
        print("Displaying {filename}".format(filename=self.filename))

proxyImage = ProxyImage('/home/omiguelperez/Pictures/photo.jpg')
proxyImage.display()
proxyImage.display()
