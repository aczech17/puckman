from Puckman import Puckman
from Rectangle import Rectangle

import pygame
import sys
from PIL import Image


class Game:
    """
    :param: obstacles
    :param: dots
    """

    def __init__(self, obstacles=None, dots=None, screen_width=800, screen_height=600):
        if obstacles is None:
            self._obstacles = []
        else:
            self._obstacles = obstacles
        for o in self._obstacles:
            if not isinstance(o, Rectangle):
                raise TypeError

        if dots is None:
            self._dots = []
        else:
            self._dots = dots
        for d in self._dots:
            if not isinstance(d, Rectangle):
                raise TypeError
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._screen = None
        # self.play()

    def close(self):
        pygame.display.quit()

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
        pass

    def generate_dots(self):
        pass

    def open_puckman_image(self, direction="assets/puckman_small.png"):
        try:
            img = pygame.image.load(direction)
        except Exception:
            sys.exit(f"Could not open {direction}")
        return img

    def play(self):
        pygame.init()
        screen_width = self._screen_width
        screen_height = self._screen_height
        self._screen = pygame.display.set_mode((screen_width, screen_height))
        screen = self._screen
        pygame.display.set_caption("Puckman")

        puckman = Puckman(left=10, top=10, hp=10)

        game_open = True
        while game_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_open = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and puckman.right() < screen_width:
                puckman.move(0.5, 0)
            if keys[pygame.K_LEFT] and puckman.left() > 0:
                puckman.move(-0.5, 0)
            if keys[pygame.K_UP] and puckman.top() > 0:
                puckman.move(0, -0.5)
            if keys[pygame.K_DOWN] and puckman.down() < screen_height:
                puckman.move(0, 0.5)

            screen.fill((0, 0, 0))
            puckman.draw(screen)
            pygame.display.flip()
        self.close()
