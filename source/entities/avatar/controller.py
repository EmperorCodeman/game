from source import global_variables
from source.interface import keyboard
from source.abstract.entities.animate import controller
from datetime import datetime
from datetime import timedelta


class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        self.timeOfLastPressR = datetime.now()
        pass

    def on_loop(self):
        if keyboard.KEYBOARD.L_SHIFT:
            self.run()
        else:
            self.walk()

        if keyboard.KEYBOARD.UP == False:
            if keyboard.KEYBOARD.RIGHT == False:
                if keyboard.KEYBOARD.DOWN == False:
                    if keyboard.KEYBOARD.LEFT == False:
                        self.stand()

        if keyboard.KEYBOARD.UP == True:
            self.direction = global_variables.NORTH
            if keyboard.KEYBOARD.RIGHT == True:
                self.direction = global_variables.NORTHEAST
            elif keyboard.KEYBOARD.LEFT == True:
                self.direction = global_variables.NORTHWEST
        
        if keyboard.KEYBOARD.RIGHT == True:
            self.direction = global_variables.EAST
            if keyboard.KEYBOARD.UP == True:
                self.direction = global_variables.NORTHEAST
            elif keyboard.KEYBOARD.DOWN == True:
                self.direction = global_variables.SOUTHEAST
        
        if keyboard.KEYBOARD.DOWN == True:
            self.direction = global_variables.SOUTH
            if keyboard.KEYBOARD.RIGHT == True:
                self.direction = global_variables.SOUTHEAST
            elif keyboard.KEYBOARD.LEFT == True:
                self.direction = global_variables.SOUTHWEST
        
        if keyboard.KEYBOARD.LEFT == True:
            self.direction = global_variables.WEST
            if keyboard.KEYBOARD.UP == True:
                self.direction = global_variables.NORTHWEST
            elif keyboard.KEYBOARD.DOWN == True:
                self.direction = global_variables.SOUTHWEST

        if keyboard.KEYBOARD.RETURN == True:
            #MUST TEST IF YOU ARE IN RANGE OF OBJECT TO PICK UP
            now = datetime.now()
            delta = (now - self.timeOfLastPressR).total_seconds()# / 1000 #miliSec
            if delta > .25:
                self.timeOfLastPressR = datetime.now()
                #if your holding something and you press Retrun then drop it
                if self.holding:
                    self.holding = None
                else:
                    #UPDATE TO BE ABLE TO PICK UP ALGEBRAICLY
                    self.pick_up(self.hectare.rock)

        self.updateAggregatedObjects()
        self.translate()
        pass
