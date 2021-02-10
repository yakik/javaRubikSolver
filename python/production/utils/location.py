from production.utils.face_handler import Face_handler

class Location:

    def containsFace(self,p_face):
        if p_face == self.c_face0 or p_face == self.c_face1 or ( (not self.c_isEdge) and (p_face == self.c_face2)):
            return True
        else:
            return False
    

    def get_copy(self):
        if self.isEdge():
            return Location(self.c_face0, self.c_face1)
        else:
            return Location(self.c_face0, self.c_face1, self.c_face2)
    

    def __init__(self,p_face0,p_face1,p_face2=None):
        if p_face2 == None:
            self.location2(p_face0,p_face1)
        else:
            self.c_isEdge = False
            self.c_face0 = p_face0
            self.c_face1 = p_face1
            self.c_face2 = p_face2
            # bubble sort to keep order within faces		
            if self.c_face0 > self.c_face1:
            
                l_tmp = self.c_face1
                self.c_face1 = self.c_face0
                self.c_face0 = l_tmp
            
            if self.c_face1 > self.c_face2:
            
                l_tmp = self.c_face2
                self.c_face2 = self.c_face1
                self.c_face1 = l_tmp
            
            if self.c_face0 > self.c_face1:
            
                l_tmp = self.c_face1
                self.c_face1 = self.c_face0
                self.c_face0 = l_tmp
        

    

    def location2(self,p_face0,p_face1):
        self.c_isEdge = True
        self.c_face2 = None
        self.c_face0 = p_face0
        self.c_face1 = p_face1
        if p_face0 > p_face1:
        
            self.c_face1 = p_face0
            self.c_face0 = p_face1
        
        else:
        
            self.c_face0 = p_face0
            self.c_face1 = p_face1
        
    

    def isEdge(self):
        return self.c_isEdge
    

    def getFace0(self):
        return self.c_face0
    

    def getFace1(self):
        return self.c_face1
    

    def getFloor(self):
        if self.equals(Location("TOP", "LEFT", "FRONT")):
            return 3
        if self.equals(Location("TOP", "LEFT", "BACK")):
            return 3
        if self.equals(Location("TOP", "RIGHT", "FRONT")):
            return 3
        if self.equals(Location("TOP", "RIGHT", "BACK")):
            return 3
        if self.equals(Location("BOTTOM", "LEFT", "FRONT")):
            return 1
        if self.equals(Location("BOTTOM", "LEFT", "BACK")):
            return 1
        if self.equals(Location("BOTTOM", "RIGHT", "FRONT")):
            return 1
        if self.equals(Location("BOTTOM", "RIGHT", "BACK")):
            return 1

        if self.equals(Location("TOP", "FRONT")):
            return 3
        if self.equals(Location("TOP", "BACK")):
            return 3
        if self.equals(Location("TOP", "LEFT")):
            return 3
        if self.equals(Location("TOP", "RIGHT")):
            return 3

        if self.equals(Location("FRONT", "LEFT")):
            return 2
        if self.equals(Location("FRONT", "RIGHT")):
            return 2
        if self.equals(Location("BACK", "LEFT")):
            return 2
        if self.equals(Location("BACK", "RIGHT")):
            return 2

        if self.equals(Location("BOTTOM", "LEFT")):
            return 1
        if self.equals(Location("BOTTOM", "RIGHT")):
            return 1
        if self.equals(Location("FRONT", "BOTTOM")):
            return 1
        if self.equals(Location("BACK", "BOTTOM")):
            return 1
        return 0
    

    def getFace2(self):
        if self.isEdge():
            return None
        else:
            return self.c_face2
    

    #	getValue(self):
    #		return (getFace0() * 1 + getFace1() * 6 + getFace2() * 36 + isEdge() * 216)
    #	


    
    def equals(self, p_location):
        return ((self.c_face0 == p_location.getFace0()) and
                (self.c_face1 == p_location.getFace1()) and
                (self.c_face2 == p_location.getFace2()) and
                (self.c_isEdge == p_location.isEdge()))
    


    def getString(self):
        if self.c_isEdge:
            return Face_handler.getCharValue(self.c_face0) + ", " + Face_handler.getCharValue(self.c_face1)
        else:
        
            return Face_handler.getCharValue(self.c_face0) + ", " + Face_handler.getCharValue(self.c_face1) + ", " + Face_handler.getCharValue(self.c_face2)
        
    


