from source import global_variables
import animation
import random
class Action:
    action = None
    entity_name = None
    north = None
    east = None
    west = None
    south = None

    def __init__(self, data):
        self.action = data["action"]
        self.entity_name = data["entity_name"]
        self.assign_directions(data)
        pass

    def assign_directions(self, data):
        for ani in data["animations"]:
            if ani["direction"] == "north":
                self.north = animation.Animation(data, ani)
            elif ani["direction"] == "east":
                self.east = animation.Animation(data, ani)
            elif ani["direction"] == "south":
                self.south = animation.Animation(data, ani)
            elif ani["direction"] == "west":
                self.west = animation.Animation(data, ani)
            else:
                print("Error: Avatar Animations Action not valid option")
        pass

    def on_render(self, camera, obj):
        if obj.direction >= global_variables.NORTHWEST or obj.direction <= global_variables.NORTHEAST:
             self.north.on_render(camera, obj)
        elif obj.direction >= global_variables.NORTHEAST and obj.direction <= global_variables.SOUTHEAST:
             self.east.on_render(camera, obj)
        elif obj.direction >= global_variables.SOUTHEAST and obj.direction <= global_variables.SOUTHWEST:
             self.south.on_render(camera, obj)
        elif obj.direction >= global_variables.SOUTHWEST and obj.direction <= global_variables.NORTHWEST:
            self.west.on_render(camera, obj)
        pass
    def on_render_NoMovement(self, camera, obj):
        #temp workaround to allow workable display of tiles
        #hash will give constant location of tile so that you can display it
        choseTileToDisplay = (2 * (obj.position.x % 7) + obj.position.y % 39)\
                             % 7


        if choseTileToDisplay == 4:
            choseTileToDisplay = 3
        if choseTileToDisplay == 5:
            choseTileToDisplay = 1
        if choseTileToDisplay == 6:
            choseTileToDisplay = 2

        if choseTileToDisplay == 0:
            self.north.on_render(camera, obj)
        if choseTileToDisplay == 1.0:
            self.east.on_render(camera, obj)
        if choseTileToDisplay == 2.0:
            self.south.on_render(camera, obj)
        if choseTileToDisplay == 3.0:
            self.west.on_render(camera, obj)
