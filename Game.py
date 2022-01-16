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
        obst1 = Object(left=10, top=10, directory="assets//obstacle_horizontal_big.png")
        obst2 = Object(left=10, top=500, directory="assets//obstacle_horizontal_big.png")
        obst3 = Object(left=10, top=30, directory="assets//obstacle_vertical_big.png")
        obst4 = Object(left=790, top=30, directory="assets//obstacle_vertical_big.png")
        return [obst1, obst2, obst3, obst4]

    def generate_dots(self):
        dot1 = Object(left=50, top=50, directory="assets/dot.png")
        dot2 = Object(left=100, top=50, directory="assets/dot.png")
        dot3 = Object(left=150, top=100, directory="assets/dot.png")
        return [dot1, dot2, dot3]

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

        self._puckman = Puckman(left=150, top=150, directory="assets/puckman_right.png", direction='stop', speed=0.25,
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
