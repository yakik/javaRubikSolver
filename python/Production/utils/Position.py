from production.utils.face import Face
from production.utils.rotation import Rotation
from production.utils.direction import Direction
from production.utils.directionHandler import DirectionHandler
from production.utils.faceHandler import FaceHandler

class Position :

    def __init__(self,p_Up,p_Front):

        self.g_face_Order = [
            [Face.FRONT, Face.LEFT, Face.BACK, Face.RIGHT],
            [Face.RIGHT, Face.BACK, Face.LEFT, Face.FRONT],
            [Face.TOP, Face.BACK, Face.BOTTOM, Face.FRONT],
            [Face.TOP, Face.FRONT, Face.BOTTOM, Face.BACK],
            [Face.TOP, Face.RIGHT, Face.BOTTOM, Face.LEFT],
            [Face.TOP, Face.LEFT, Face.BOTTOM, Face.RIGHT]]
        if p_Front!=None:
            self.c_currentUp = p_Up
            self.c_currentFront = p_Front
        else:
            self.c_currentUp = Face.TOP
            self.c_currentFront = Face.FRONT
    
    def getUp(self):
        return self.c_currentUp

    def getFront(self):
        return self.c_currentFront

    def getString(self):
        return FaceHandler.getCharValue(self.c_currentUp)+", "+ FaceHandler.getCharValue(self.c_currentFront)
    

    def rotate(self, p_rotation):
        l_face = p_rotation.getFace()
        l_direction = p_rotation.getDirection()
        if l_face == Face.TOP:
            if l_direction == Direction.CW:
                self.c_currentFront = self.getFace(Face.RIGHT)
            else:
                self.c_currentFront = self.getFace(Face.LEFT)
        else:
            if l_face == Face.RIGHT:
                if l_direction == Direction.CW:
                    l_temp = self.c_currentFront
                    self.c_currentFront = self.getFace(Face.BOTTOM)
                    self.c_currentUp = l_temp
                else:
                    l_temp = self.getFace(Face.BACK)
                    self.c_currentFront = self.c_currentUp
                    self.c_currentUp = l_temp
            
            else:
                if l_face == Face.FRONT:
                    if l_direction == Direction.CW:
                        self.c_currentUp = self.getFace(Face.LEFT)
                    else:
                        self.c_currentUp = self.getFace(Face.RIGHT)
                else:
                    self.rotate(Rotation(FaceHandler.getOpposite(l_face), DirectionHandler.getOpposite(l_direction)))

    def getCopy(self):
            return Position(self.c_currentUp,self.c_currentFront)

    def getFace(self,p_viewpoint):
        if p_viewpoint== Face.TOP:
            return self.c_currentUp
        else:
            if p_viewpoint== Face.BOTTOM:
                return FaceHandler.getOpposite(self.c_currentUp)
            else:
                return self.getHorizonalFacebyVirtual(p_viewpoint)

    def getHorizonalFacebyVirtual(self,p_viewpoint):
        i = 0
        while (self.g_face_Order[self.c_currentUp][i] != self.c_currentFront and i < 4):
            i+=1
        if p_viewpoint==Face.FRONT:
            return self.g_face_Order[self.c_currentUp][i]
        else:
            if p_viewpoint==Face.LEFT:
                return self.g_face_Order[self.c_currentUp][(i + 1) % 4]
            else:
                if p_viewpoint==Face.BACK:
                    return self.g_face_Order[self.c_currentUp][(i + 2) % 4]
                else:
                    return self.g_face_Order[self.c_currentUp][(i + 3) % 4]

    def equals(self, p_position):
        return ((self.c_currentUp == p_position.getUp()) and
                (self.c_currentFront == p_position.getFront()))
    
