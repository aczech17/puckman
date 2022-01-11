#from Puckman import Puckman
#from Rectangle import Rectangle

import pygame
import sys
from PIL import Image

from Actor import Actor
from Puckman import Puckman

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

        if dots is None:
            self._dots = []
        else:
            self._dots = dots

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

    def open_puckman_image(self, directory="assets/puckman_small.png"):
        try:
            img = pygame.image.load(directory)
        except FileNotFoundError:
            sys.exit(f"Could not open {directory}")
        return img

    def play(self):
        pygame.init()
        screen_width = self._screen_width
        screen_height = self._screen_height
        self._screen = pygame.display.set_mode((screen_width, screen_height))
        screen = self._screen
        pygame.display.set_caption("Puckman")

        puckman = Puckman(left=10, top=10, directory="assets/puckman_right.png", screen_width=self.screen_width(), screen_height=self.screen_height())

        game_open = True
        while game_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_open = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                puckman.control(0.5, 0, 'right')
            if keys[pygame.K_LEFT]:
                puckman.control(-0.5, 0, 'left')
            if keys[pygame.K_UP]:
                puckman.control(0, -0.5, 'up')
            if keys[pygame.K_DOWN]:
                puckman.control(0, 0.5, 'down')

            screen.fill((0, 0, 0))
            puckman.draw(screen)
            pygame.display.flip()
        self.close()
