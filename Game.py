import pygame

from Object import Object
from Puckman import Puckman


class Game:
    """
    :param: obstacles
    :param: dots
    """

    def __init__(self, screen_width=800, screen_height=600):
        self._obstacles = self.generate_obstacles()
        self._dots = self.generate_dots()

        self._screen_width = screen_width
        self._screen_height = screen_height
        self._screen = None
        self._puckman = None
        self._points = 0

    def close(self):
        pygame.display.quit()

    def points(self):
        return self._points

    def obstacles(self):
        return self._obstacles

    def add_obstacle(self, rectangle):
        self._obstacles.append(rectangle)

    def is_obstacle(self, point):
        x = point[0]
        y = point[1]
        for obstacle in self._obstacles:
            if obstacle.collides_with_point(x, y):
                return True
        return False

    def screen_width(self):
        return self._screen_width

    def screen_height(self):
        return self._screen_height

    def generate_obstacles(self):
        return []

    def generate_dots(self):
        dot1 = Object(left=50, top=50, directory="assets/dot.png")
        dot2 = Object(left=100, top=50, directory="assets/dot.png")
        return [dot1, dot2]

    def draw_everything(self):
        self._puckman.draw(self._screen)
        for dot in self._dots:
            dot.draw(self._screen)
        for obstacle in self._obstacles:
            obstacle.draw(self._screen)

    def play(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption("Puckman")

        self._puckman = Puckman(left=10, top=10, directory="assets/puckman_right.png", screen_width=self.screen_width(),
                                screen_height=self.screen_height())

        game_open = True
        while game_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_open = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self._puckman.control('right')
            if keys[pygame.K_LEFT]:
                self._puckman.control('left')
            if keys[pygame.K_UP]:
                self._puckman.control('up')
            if keys[pygame.K_DOWN]:
                self._puckman.control('down')
            if keys[pygame.K_RETURN]:
                self._puckman.control('stop')

            self.check_for_collisions()
            self._puckman.go()

            self._screen.fill((0, 0, 0))
            self.draw_everything()
            pygame.display.flip()
        self.close()

    def check_for_collisions(self):
        for dot in self._dots:
            if dot.collides_with(self._puckman):
                self._points += 1
                self._dots.remove(dot)
