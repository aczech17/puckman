import sys
import subprocess
import pygame

from Game import Game


def install_pygame():
    print("Installing pygame. Please wait...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])


def main():
    install_pygame()
    game = Game(screen_width=800, screen_height=600)
    game.play()


if __name__ == "__main__":
    main()
