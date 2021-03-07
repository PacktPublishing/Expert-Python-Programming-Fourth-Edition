import itertools
from dataclasses import dataclass

from zope.interface import Interface, Attribute, implementer
from zope.interface.verify import verifyObject


def rects_collide(rect1, rect2):
    """Check collision between rectangles

    Rectangle coordinates:
        ┌───(x2, y2)
        │       │
      (x1, y1)──┘
    """
    return (
        rect1.x1 < rect2.x2
        and rect1.x2 > rect2.x1
        and rect1.y1 < rect2.y2
        and rect1.y2 > rect2.y1
    )


def find_collisions(objects):
    for item in objects:
        verifyObject(ICollidable, item)

    return [
        (item1, item2)
        for item1, item2 in itertools.combinations(objects, 2)
        if rects_collide(item1.bounding_box, item2.bounding_box)
    ]


class ICollidable(Interface):
    bounding_box = Attribute("Object's bounding box")


@dataclass
class Box:
    x1: float
    y1: float
    x2: float
    y2: float


@implementer(ICollidable)
@dataclass
class Square:
    x: float
    y: float
    size: float

    @property
    def bounding_box(self):
        return Box(self.x, self.y, self.x + self.size, self.y + self.size)


@implementer(ICollidable)
@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def bounding_box(self):
        return Box(self.x, self.y, self.x + self.width, self.y + self.height)


@implementer(ICollidable)
@dataclass
class Circle:
    x: float
    y: float
    radius: float

    @property
    def bounding_box(self):
        return Box(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        )


@dataclass
class Point:
    x: float
    y: float


if __name__ == "__main__":
    print("Valid attempt:")
    for collision in find_collisions(
        [
            Square(0, 0, 10),
            Rect(5, 5, 20, 20),
            Square(15, 20, 5),
            Circle(1, 1, 2),
        ]
    ):
        print(collision)

    print("Invalid attempt")
    for collision in find_collisions(
        [
            Square(0, 0, 10),
            Rect(5, 5, 20, 20),
            Square(15, 20, 5),
            Circle(1, 1, 2),
            Point(100, 200),
        ]
    ):
        print(collision)
