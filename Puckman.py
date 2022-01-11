#from Rectangle import Rectangle
import pygame.image

from Actor import Actor as Actor


class Puckman(Actor):
    def __init__(self, left, top, directory, screen_width, screen_height):
        super().__init__(left, top, directory)
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._assets = {
            'right': 'assets//puckman_right.png',
            'left': 'assets//puckman_left.png',
            'up': 'assets//puckman_up.png',
            'down': 'assets//puckman_down.png'
        }

    def control(self, x, y, direction):
        asset_directory = self._assets[direction]
        self._image = pygame.image.load(asset_directory)
        self.move(x, y)
        if self.right() > self._screen_width:
            self.set_position(left=0, top=self.top())
        if self.left() < 0:
            self.set_position(left=self._screen_width - self.width(), top=self.top())
        if self.top() < 0:
            self.set_position(left=self.left(), top=self._screen_height - self.height())
        if self.top() > self._screen_height:
            self.set_position(left=self.left(), top=0)

