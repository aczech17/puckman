import sys
import pygame

from Object import Object


class Movable(Object):
    def __init__(self, left, top, directory, speed, direction='stop'):
        super().__init__(left, top, directory)
        self._speed = speed
        self._current_direction = direction

    def speed(self):
        return self._speed

    def vertical_collision(self, an_object: Object):
        return an_object.top() <= self.down() <= an_object.down() or self.top() <= an_object.down() <= self.down()

    def horizontal_collision(self, an_object: Object):
        return an_object.left() <= self.left() <= an_object.right() or self.left() <= an_object.left() <= self.right()

    def will_collide_with(self, an_object: Object):
        if self._current_direction == 'stop':
            return False

        top = self.top()
        down = self.down()
        left = self.left()
        right = self.right()
        future_top = self.top() - self.speed()
        future_down = self.down() + self.speed()
        future_left = self.left() - self.speed()
        future_right = self.right() + self.speed()

        if self._current_direction == 'up':
            return future_top <= an_object.down() < down and self.horizontal_collision(an_object)
        if self._current_direction == 'down':
            return future_down >= an_object.top() > top and self.horizontal_collision(an_object)
        if self._current_direction == 'left':
            return future_left <= an_object.right() < right and self.vertical_collision(an_object)
        if self._current_direction == 'right':
            return future_right >= an_object.left() > left and self.vertical_collision(an_object)

    def move(self, x, y):
        self._left = self._left + x
        self._top = self._top + y

