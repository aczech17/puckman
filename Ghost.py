import Movable


class Ghost(Movable):
    def __init__(self, left, top, directory, speed, direction='stop'):
        super().__init__(left, top, directory, speed, direction)
