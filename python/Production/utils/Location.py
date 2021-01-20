from .face import Face

class Location:

    def containsFace(self,p_face):
        if p_face == self.c_face0 or p_face == self.c_face1 or ( (not self.c_isEdge) and (p_face == self.c_face2)):
            return True
        else:
            return False
    

    def getCopy(self):
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
        self.c_face2 = Face.NOTDEFINED
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
        if self.equals(Location(Face.TOP, Face.LEFT, Face.FRONT)):
            return 3
        if self.equals(Location(Face.TOP, Face.LEFT, Face.BACK)):
            return 3
        if self.equals(Location(Face.TOP, Face.RIGHT, Face.FRONT)):
            return 3
        if self.equals(Location(Face.TOP, Face.RIGHT, Face.BACK)):
            return 3
        if self.equals(Location(Face.BOTTOM, Face.LEFT, Face.FRONT)):
            return 1
        if self.equals(Location(Face.BOTTOM, Face.LEFT, Face.BACK)):
            return 1
        if self.equals(Location(Face.BOTTOM, Face.RIGHT, Face.FRONT)):
            return 1
        if self.equals(Location(Face.BOTTOM, Face.RIGHT, Face.BACK)):
            return 1

        if self.equals(Location(Face.TOP, Face.FRONT)):
            return 3
        if self.equals(Location(Face.TOP, Face.BACK)):
            return 3
        if self.equals(Location(Face.TOP, Face.LEFT)):
            return 3
        if self.equals(Location(Face.TOP, Face.RIGHT)):
            return 3

        if self.equals(Location(Face.FRONT, Face.LEFT)):
            return 2
        if self.equals(Location(Face.FRONT, Face.RIGHT)):
            return 2
        if self.equals(Location(Face.BACK, Face.LEFT)):
            return 2
        if self.equals(Location(Face.BACK, Face.RIGHT)):
            return 2

        if self.equals(Location(Face.BOTTOM, Face.LEFT)):
            return 1
        if self.equals(Location(Face.BOTTOM, Face.RIGHT)):
            return 1
        if self.equals(Location(Face.FRONT, Face.BOTTOM)):
            return 1
        if self.equals(Location(Face.BACK, Face.BOTTOM)):
            return 1
        return 0
    

    def getFace2(self):
        if self.isEdge():
            return Face.NOTDEFINED
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
            return String.Format("0, 1", FaceHandler.getCharValue(self.c_face0), FaceHandler.getCharValue(self.c_face1))
        else:
        
            return String.Format("0, 1, 2", FaceHandler.getCharValue(self.c_face0), FaceHandler.getCharValue(self.c_face1), FaceHandler.getCharValue(self.c_face2))
        
    


