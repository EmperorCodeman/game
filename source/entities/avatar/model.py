from source.abstract.entities.animate import model
import copy
class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2
    CARRYBULKY = 3
    CARRYLIGHT = 4

class Model(model.Model):
    hectare = None

    holding = None


    def __init__(self):
        model.Model.__init__(self)
        pass

    def run(self):
        self.move_state = MoveState.RUN
        pass

    def walk(self):
        self.move_state = MoveState.WALK
        pass
    def pickUp(self, object):
        #if your not holding something and your within distance pick it up
        if not object:
            print "error picked up a NONE type object"

        if self.testIfInRange(
            object.position, self.position, 40
        ):
            self.holding = object
            object.position.x = self.position.x #+ 20
            object.position.y = self.position.y + 20
            object.position.z = self.position.z
    def testIfInRange(self, pygameVector, pygameVector2, acceptableRange):
        x = pygameVector.x
        y = pygameVector.y
        z = pygameVector.z
        x2 = pygameVector2.x
        y2 = pygameVector2.y
        z2 = pygameVector2.z
        #take radius
        #acceptableRange /= 2
        #ensure that x axis values are within accepatable range of eachother
        if (x + acceptableRange) > x2 and (x - acceptableRange) < x2:
           if (y + acceptableRange) > y2 and (y - acceptableRange) < y2:
               if (z + acceptableRange) > z2 and (z - acceptableRange) < z2:
                   return True
               else:
                   return False




