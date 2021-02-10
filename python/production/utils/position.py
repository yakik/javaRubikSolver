from production.utils.rotation import Rotation
from production.utils.direction_handler import Direction_handler
from production.utils.face_handler import Face_handler

class Position :

    def __init__(self,p_Up,p_Front):

        self.g_face_Order = [
            ["FRONT", "LEFT", "BACK", "RIGHT"],
            ["RIGHT", "BACK", "LEFT", "FRONT"],
            ["TOP", "BACK", "BOTTOM", "FRONT"],
            ["TOP", "FRONT", "BOTTOM", "BACK"],
            ["TOP", "RIGHT", "BOTTOM", "LEFT"],
            ["TOP", "LEFT", "BOTTOM", "RIGHT"]]
        if p_Front!=None:
            self.c_currentUp = p_Up
            self.c_currentFront = p_Front
        else:
            self.c_currentUp = "TOP"
            self.c_currentFront = "FRONT"
    
    def getUp(self):
        return self.c_currentUp

    def getFront(self):
        return self.c_currentFront

    def getString(self):
        return Face_handler.getCharValue(self.c_currentUp) + ", " + Face_handler.getCharValue(self.c_currentFront)
    

    def rotate(self, p_rotation):
        l_face = p_rotation.getFace()
        l_direction = p_rotation.getDirection()
        if l_face == "TOP":
            if l_direction == "CW":
                self.c_currentFront = self.getFace("RIGHT")
            else:
                self.c_currentFront = self.getFace("LEFT")
        else:
            if l_face == "RIGHT":
                if l_direction == "CW":
                    l_temp = self.c_currentFront
                    self.c_currentFront = self.getFace("BOTTOM")
                    self.c_currentUp = l_temp
                else:
                    l_temp = self.getFace("BACK")
                    self.c_currentFront = self.c_currentUp
                    self.c_currentUp = l_temp
            
            else:
                if l_face == "FRONT":
                    if l_direction == "CW":
                        self.c_currentUp = self.getFace("LEFT")
                    else:
                        self.c_currentUp = self.getFace("RIGHT")
                else:
                    self.rotate(Rotation(Face_handler.getOpposite(l_face), Direction_handler.getOpposite(l_direction)))

    def get_copy(self):
            return Position(self.c_currentUp,self.c_currentFront)

    def getFace(self,p_viewpoint):
        if p_viewpoint== "TOP":
            return self.c_currentUp
        else:
            if p_viewpoint== "BOTTOM":
                return Face_handler.getOpposite(self.c_currentUp)
            else:
                return self.getHorizonalFacebyVirtual(p_viewpoint)

    def getHorizonalFacebyVirtual(self,p_viewpoint):
        i = 0
        while (self.g_face_Order[Face_handler.getIntFaceValue(self.c_currentUp)][i] != self.c_currentFront and i < 4):
            i+=1
        if p_viewpoint=="FRONT":
            return self.g_face_Order[Face_handler.getIntFaceValue(self.c_currentUp)][i]
        else:
            if p_viewpoint=="LEFT":
                return self.g_face_Order[Face_handler.getIntFaceValue(self.c_currentUp)][(i + 1) % 4]
            else:
                if p_viewpoint=="BACK":
                    return self.g_face_Order[Face_handler.getIntFaceValue(self.c_currentUp)][(i + 2) % 4]
                else:
                    return self.g_face_Order[Face_handler.getIntFaceValue(self.c_currentUp)][(i + 3) % 4]

    def equals(self, p_position):
        return ((self.c_currentUp == p_position.getUp()) and
                (self.c_currentFront == p_position.getFront()))
    
