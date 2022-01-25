from Movable import Movable
from random import randint

class Ghost(Movable):
    def __init__(self, left, top, directory, speed, direction, screen):
        super().__init__(left, top, directory, speed, direction)
        self._screen_width = screen.screen_width()
        self._screen_height = screen.screen_height()

    def set_random_direction(self):
        directions = {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
        direction = directions[randint(0, 3)]
        self.set_direction(direction)

    def go(self, obstacles):
        if self.direction() == 'stop':
            self.set_random_direction()
            return
        for obstacle in obstacles:
            if self.will_collide_with(obstacle):
                self.set_random_direction()

        if self.left() == 0:
            self.set_direction('right')
        elif self.right() == self._screen_width:
            self.set_direction('left')

        speed = self._speed
        velocity = {'left': (-speed, 0), 'right': (speed, 0), 'up': (0, -speed), 'down': (0, speed), 'stop': (0, 0)}
        self.move(*velocity[self._current_direction])
