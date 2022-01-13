import sys
import pygame

from Object import Object


class Movable(Object):
    def __init__(self, left, top, directory):
        super().__init__(left, top, directory)

    def move(self, x, y):
        self._left = self._left + x
        self._top = self._top + y

    def set_position(self, left, top):
        self._left = left
        self._top = top
