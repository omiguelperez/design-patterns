from abc import ABCMeta

class Shape(metaclass=ABCMeta):
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('I am a circle.')

class Rectangle(Shape):
    def draw(self):
        print('I am a rectangle.')

class ShapeDecorator(Shape):
    def __init__(self, decoratedShape):
        self.decoratedShape = decoratedShape

    def draw(self):
        self.decoratedShape.draw()

    def doSomething(self):
        pass

class ColorRedShapeDecorator(ShapeDecorator):
    def draw(self):
        super(ColorRedShapeDecorator, self).draw()
        self.doSomething()

    def doSomething(self):
        print('Coloring red')

class ColorBlueShapeDecorator(ShapeDecorator):
    def draw(self):
        super(ColorBlueShapeDecorator, self).draw()
        self.doSomething()

    def doSomething(self):
        print('Coloring blue.')

if __name__ == '__main__':
    circle = Circle()
    circle = ColorRedShapeDecorator(circle)
    circle = ColorBlueShapeDecorator(circle)
    circle.draw()
