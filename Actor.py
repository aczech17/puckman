import sys
import pygame


class Actor:
    def __init__(self, left, top, directory):
        self._left = left
        self._top = top
        try:
            self._image = pygame.image.load(directory)
        except Exception:
            sys.exit(f"Could not open {directory}.")

    def move(self, x, y):
        self._left = self._left + x
        self._top = self._top + y

    def left(self):
        return self._left

    def top(self):
        return self._top

    def draw(self, screen):
        screen.blit(self._image, (self._left, self._top))
