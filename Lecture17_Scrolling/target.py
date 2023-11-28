from pico2d import (load_image, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT, draw_rectangle,
                    SDL_MOUSEMOTION)

import game_world
import game_framework
import random
import math

import server


class Target:
    image = None

    def __init__(self, x=None, y=None):
        self.y = x
        self.x = y
        self.image = load_image('target.png')


    def draw(self):
        self.image.draw(self.x, self.y)


    def handle_events(self, events):
        global running, mx, my, targets
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                mx, my = self.x, self.y
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                targets.append(Target(self.x, self.y))
