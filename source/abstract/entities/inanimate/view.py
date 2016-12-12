import pygame

from source.abstract.entities.entity import view

from animation_config import stand

class View(view.View):
    def __init__(self):
        view.View.__init__(self)

        self.height = 32
        self.width = 32
        pass

    def on_render(self, camera):
        pass
