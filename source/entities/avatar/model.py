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
    def pick_up(self, object):
        #if you are not holding something and your within distance pick it up
        if object == None:
            print "error picked up a NONE type object"
        close_enough = 40
        if self.reachable(
            object.position, self.position, close_enough
        ):
            self.holding = object
            object.position.x = self.position.x #+ 20
            #offset y to not block face
            object.position.y = self.position.y + 20
            object.position.z = self.position.z
    def reachable(self, pygameVector, pygameVector2, acceptableRange):
        #ensure that x axis values are within accepatable range of eachother
        return     (pygameVector.x + acceptableRange) > pygameVector2.x \
               and (pygameVector.x - acceptableRange) < pygameVector2.x \
               and (pygameVector.y + acceptableRange) > pygameVector2.y \
               and (pygameVector.y - acceptableRange) < pygameVector2.y \
               and (pygameVector.z + acceptableRange) > pygameVector2.z \
               and (pygameVector.z - acceptableRange) < pygameVector2.z

    def updateAggregatedObjects(self):
        if self.holding:
            self.holding.position.x = self.position.x
            self.holding.position.y = self.position.y + 20
            self.holding.position.z = self.position.z




