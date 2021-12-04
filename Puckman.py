from Rectangle import Rectangle
from Actor import Actor as Actor


class Puckman(Actor):
    def __init__(self, left, top, directory="assets//puckman_small.png", hp=1):
        super().__init__(left, top, directory)
        self._radius = self._image.get_width() / 2
        self._hp = hp

    def radius(self):
        return self._radius

    def hp(self):
        return self._hp

    def right(self):
        return self._left + 2 * self._radius

    def down(self):
        return self._top + 2 * self._radius

    def collides_with_rectangle(self, rectangle: Rectangle):
        return (rectangle.collides_with_point(self.top()) or rectangle.collides_with_point(self.down()) or
                rectangle.collides_with_point(self.left()) or rectangle.collides_with_point(self.right()))
