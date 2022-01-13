import sys
import subprocess
import pygame

from Game import Game


def main():
    game = Game(screen_width=800, screen_height=600)
    game.play()


if __name__ == "__main__":
    main()
