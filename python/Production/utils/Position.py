class Position :

    def __init__():
        self.g_face_Order = [
            [Face.FRONT, Face.LEFT, Face.BACK, Face.RIGHT],
            [Face.RIGHT, Face.BACK, Face.LEFT, Face.FRONT],
            [Face.TOP, Face.BACK, Face.BOTTOM, Face.FRONT],
            [Face.TOP, Face.FRONT, Face.BOTTOM, Face.BACK],
            [Face.TOP, Face.RIGHT, Face.BOTTOM, Face.LEFT],
            [Face.TOP, Face.LEFT, Face.BOTTOM, Face.RIGHT]]
    


    def Position(self,p_Up,p_Front):
        self.c_currentUp = p_Up
        self.c_currentFront = p_Front
    

    def Position(self):
        self.c_currentUp = Face.TOP
        self.c_currentFront = Face.FRONT
    

    def getString(self):
        return String.Format("0, 1", FaceHandler.getCharValue(self.c_currentUp), FaceHandler.getCharValue(self.c_currentFront))
    

    def rotate(self, p_rotation):
        l_face = p_rotation.getFace()
        l_direction = p_rotation.getDirection()
        if l_face == Face.TOP:
            if l_direction == Direction.CW:
                self.c_currentFront = getFace(Face.RIGHT)
            else:
                self.c_currentFront = getFace(Face.LEFT)
        else:
            if l_face == Face.RIGHT:
                if l_direction == Direction.CW:
                    l_temp = self.c_currentFront
                    self.c_currentFront = getFace(Face.BOTTOM)
                    self.c_currentUp = l_temp
                else:
                    l_temp = getFace(Face.BACK)
                    self.c_currentFront = self.c_currentUp
                    self.c_currentUp = l_temp
            
            else:
                if l_face == Face.FRONT:
                    if l_direction == Direction.CW:
                        self.c_currentUp = getFace(Face.LEFT)
                    else:
                        self.c_currentUp = getFace(Face.RIGHT)
                else:
                    rotate(Rotation(FaceHandler.getOpposite(l_face), DirectionHandler.getOpposite(l_direction)))

    

    def getCopy(self):
            return Position(self.c_currentUp,self.c_currentFront)

    def getFace(p_viewpoint):
            if p_viewpo== Face.TOP:
                return self.c_currentUp
            else:
                if p_viewpo== Face.BOTTOM:
                    return FaceHandler.getOpposite(self.c_currentUp)
                else:
                    return getHorizonalFacebyVirtual(p_viewpoint)
    


    def getHorizonalFacebyVirtual(self,p_viewpoint):
        i = 0
        while self.g_face_Order[rentUp,i] != self.c_currentFront and i < 4:
            i+=1
        if p_viewpoint==Face.FRONT:
            return self.g_face_Order[rentUp,i]
        else:
            if p_viewpoint==Face.LEFT:
                return self.g_face_Order[rentUp,(i + 1) % 4]
            else:
                if p_viewpoint==Face.BACK:
                    return self.g_face_Order[rentUp,(i + 2) % 4]
                else:
                    return self.g_face_Order[rentUp,(i + 3) % 4]

        
    

    def equals(self, p_position):
        return ((self.c_currentUp == p_position.self.c_currentUp) and
                (self.c_currentFront == p_position.self.c_currentFront))
    
