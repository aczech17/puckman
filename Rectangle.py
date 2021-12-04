from Actor import Actor as Actor


class Rectangle(Actor):
    def __init__(self, left, top, directory, width, height):
        super().__init__(left, top, directory)
        self._width = width
        self._height = height

    def width(self):
        return self._width

    def height(self):
        return self._height

    def right(self):
        return self._left + self._width

    def down(self):
        return self._top + self._height

    def collides_with_point(self, point):
        x = point[0]
        y = point[1]
        return self.left() <= x <= self.right() and self.top() <= y <= self.down()

