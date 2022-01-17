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

    def is_game_won(self):
        return self._points == self._max_points

    def generate_obstacles(self):
        obstacles = []
        margin = 10
        obst_up = Object(left=margin, top=margin, directory="assets//obstacle_horizontal_big.png")
        obstacles.append(obst_up)

        obst_down = Object(left=margin, top=0, directory="assets//obstacle_horizontal_big.png")
        obst_down.set_position(left=obst_down.left(), top=self.screen_height() - obst_down.down() - margin)
        obstacles.append(obst_down)

        obstacles.append(Object(left=margin, top=obst_up.down(), directory="assets//obstacle_vertical_small.png"))
        obstacles.append(
            Object(left=margin, top=obstacles[-1].down() + 50, directory="assets//obstacle_vertical_small.png"))

        obstacles.append(Object(left=0, top=obst_up.down(),
                                directory="assets//obstacle_vertical_small.png"))
        obstacles[-1].set_position(left=obst_up.right() - obstacles[-1].width(), top=obstacles[-1].top())

        obstacles.append(Object(left=obstacles[-1].left(), top=obstacles[-1].down() + 50,
                                directory="assets//obstacle_vertical_small.png"))

        for ob in obstacles:
            print(ob.directory())
        return obstacles

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

        start_position = (self._obstacles[2].right() + 10, self._obstacles[0].down() + 10)
        self._puckman = Puckman(left=start_position[0], top=start_position[1],
                                directory="assets/puckman_right.png", direction='stop', speed=0.5,
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
