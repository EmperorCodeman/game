from source.abstract.entities.inanimate import view
from source.action import action
from animation_config import stand

import random

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(stand.stand_data)
        self.height = 100
        self.width = 100
        pass

    def on_render(self, camera):


        if self.animation == None or self.animation.action != "stand":
            self.animation = action.Action(stand.stand_data)
        self.animation.on_render_NoMovement(camera, self)
        pass

