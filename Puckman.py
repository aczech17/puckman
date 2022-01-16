from Movable import Movable


class Puckman(Movable):
    def __init__(self, left, top, directory, speed, direction, screen):
        self._screen_width = screen.screen_width()
        self._screen_height = screen.screen_height()
        self._assets = {
            'right': 'assets//puckman_right.png',
            'left': 'assets//puckman_left.png',
            'up': 'assets//puckman_up.png',
            'down': 'assets//puckman_down.png'
        }
        directory = self._assets['right']
        super().__init__(left, top, directory, speed, direction)

    def current_direction(self):
        return self._current_direction

    def control(self, direction):
        if direction != self._current_direction and direction != 'stop':
            asset_directory = self._assets[direction]
            self._image = self.open_image(asset_directory)
        self._current_direction = direction

    def go(self):
        speed = self._speed
        velocity = {'left': (-speed, 0), 'right': (speed, 0), 'up': (0, -speed), 'down': (0, speed), 'stop': (0, 0)}
        self.move(*velocity[self._current_direction])

        if self.right() > self._screen_width:
            self.set_position(left=0, top=self.top())
        if self.left() < 0:
            self.set_position(left=self._screen_width - self.width(), top=self.top())
        if self.top() < 0:
            self.set_position(left=self.left(), top=self._screen_height - self.height())
        if self.down() > self._screen_height:
            self.set_position(left=self.left(), top=0)
