import controller, model, view

class Avatar(controller.Controller, model.Model, view.View):
    def __init__(self, hectare):
        controller.Controller.__init__(self)
        model.Model.__init__(self)
        view.View.__init__(self)
        self.hectare = hectare
