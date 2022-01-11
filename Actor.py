import sys
import pygame


class Actor:
    def __init__(self, left, top, directory):
        self._left = left
        self._top = top
        try:
            self._image = pygame.image.load(directory)
        except FileNotFoundError:
            sys.exit(f"Could not open {directory}.")
        self._width = self._image.get_width()
        self._height = self._image.get_height()

    def width(self):
        return self._width

    def height(self):
        return self._height

    def left(self):
        return self._left

    def top(self):
        return self._top

    def right(self):
        return self._left + self._width

    def down(self):
        return self._top + self._height

    def _collides_with_point(self, point):
        x = point[0]
        y = point[1]
        return self.left() <= x <= self.right() and self.top() <= y <= self.down()

    def collides_with_actor(self, actor):
        return (self._collides_with_point(actor.down()) or self._collides_with_point(actor.top()) or
                self._collides_with_point(actor.left()) or self._collides_with_point(actor.right()))

    def move(self, x, y):
        self._left = self._left + x
        self._top = self._top + y

    def set_position(self, left, top):
        self._left = left
        self._top = top

    def draw(self, screen):
        screen.blit(self._image, (self._left, self._top))
