import pygame

from Object import Object
from Puckman import Puckman

from PuckGUI import win_window


class Game:
    """
    :param: obstacles
    :param: dots
    """

    def __init__(self, screen_width=800, screen_height=600, points=0):
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._screen = None
        self._puckman = None

        self._vertical_obstacles = []
        self._horizontal_obstacles = []
        self._obstacles = self.generate_obstacles()
        self._dots = self.generate_dots()
        self._max_points = len(self._dots)
        self._points = points

    def close(self):
        pygame.display.quit()

    def points(self):
        return self._points

    def obstacles(self):
        return self._obstacles

    def screen_width(self):
        return self._screen_width

    def screen_height(self):
        return self._screen_height

    def is_game_won(self):
        return self._points == self._max_points

    def generate_obstacles(self):
        margin_vertical = 80
        margin_horizontal = 49
        medium_hor_dir = "assets//obstacle_horizontal_medium.png"
        big_hor_dir = "assets//obstacle_horizontal_big.png"
        medium_ver_dir = "assets//obstacle_vertical_medium.png"
        big_ver_dir = "assets//obstacle_vertical_big.png"
        small_hor_dir = "assets//obstacle_horizontal_small.png"
        small_ver_dir = "assets//obstacle_vertical_small.png"
        # up
        self._horizontal_obstacles.append(Object(left=margin_vertical, top=margin_horizontal, directory=big_hor_dir))
        self._horizontal_obstacles.append(Object(left=margin_vertical + 600, top=margin_horizontal, directory=big_hor_dir))
        # down
        self._horizontal_obstacles.append(Object(left=margin_vertical, top=margin_horizontal + 650, directory=big_hor_dir))
        self._horizontal_obstacles.append(Object(left=margin_vertical + 600, top=margin_horizontal + 650, directory=big_hor_dir))
        # left
        self._vertical_obstacles.append(Object(left=margin_vertical, top=margin_horizontal + 20, directory=medium_ver_dir))
        self._vertical_obstacles.append(Object(left=margin_vertical, top=margin_horizontal + 350, directory=medium_ver_dir))
        # right
        self._vertical_obstacles.append(Object(left=self.screen_width() - margin_vertical - 20, top=margin_horizontal + 20,
                                directory=medium_ver_dir))
        self._vertical_obstacles.append(Object(left=self.screen_width() - margin_vertical - 20, top=margin_horizontal + 350,
                                directory=medium_ver_dir))
        # top left
        for i in range(6):
            for j in range(3):
                self._horizontal_obstacles.append(
                    Object(left=margin_vertical + 20 + j * 330, top=margin_horizontal + 20 + i * (30 + 20) + 30,
                           directory=medium_hor_dir))

        # top right
        margin = self._horizontal_obstacles[-1].right()
        for i in range(4):
            self._vertical_obstacles.append(Object(left=margin + i * (20+30), top=margin_horizontal+20, directory=medium_ver_dir))




        return self._horizontal_obstacles + self._vertical_obstacles

    def generate_dots(self):
        dot1 = Object(left=50, top=50, directory="assets/dot.png")
        dot2 = Object(left=100, top=50, directory="assets/dot.png")
        dot3 = Object(left=150, top=100, directory="assets/dot.png")

        dots = [dot1, dot2, dot3]
        self._max_points = len(dots)
        return dots

    def draw_everything(self):
        self._puckman.draw(self._screen)
        for dot in self._dots:
            dot.draw(self._screen)
        for obstacle in self._obstacles:
            obstacle.draw(self._screen)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(f"Punkty xD: {self._points}", False, (255, 255, 255))
        self._screen.blit(textsurface, (0, 0))

    def play(self):
        pygame.init()
        pygame.font.init()

        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption("Puckman")

        self._puckman = Puckman(left=100, top=69,
                                directory="assets/puckman_right.png", direction='stop', speed=1,
                                screen=self)

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

            if self.is_game_won():
                win_window()
                break

        self.close()

    def check_for_collisions(self):
        puckman = self._puckman
        for dot in self._dots:
            if puckman.will_collide_with(dot):
                self._points += 1
                self._dots.remove(dot)

        for obstacle in self._obstacles:
            if puckman.will_collide_with(obstacle):
                self._puckman.control('stop')
                break  # ?
