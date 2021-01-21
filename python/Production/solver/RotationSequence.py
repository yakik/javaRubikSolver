from production.utils.color import Color
from production.utils.face import Face
from production.utils.location import Location
from production.utils.rotation import Rotation
from production.utils.locationInFace import LocationInFace
from production.utils.direction import Direction
from production.utils.faceHandler import FaceHandler

class RotationSequence:

        def __init__(self, p_List=None):
            if p_List==None:
                self.c_array = list()
            else:
                self.c_array = p_List

        def print(self):
            for l_itr in self.c_array:
                l_itr.print()
            print("\n")

        def addRotation(self, p_rotation):
            self.c_array.append(p_rotation)

        def removeRotation(self):
            self.c_array.RemoveAt(len(self.c_array) - 1)

        def isRedundant(self, p_rotation):
            l_returnValue = False
            if len(self.c_array) > 0:
                l_lastFace = self.c_array[(len(self.c_array) - 1)].getFace()
                l_lastDirection = self.c_array[len(self.c_array) - 1].getDirection()
                # rotation is opposite to previous
                if self.c_array[len(self.c_array) - 1].getReverse().equals(p_rotation):
                    l_returnValue = True
                # previouswas opposite and previousgreater then current face
                if (p_rotation.getFace() == FaceHandler.getOpposite(l_lastFace) and (l_lastFace > p_rotation.getFace())):
                    l_returnValue = True
                # two clockwise rotation of same face
                if ((p_rotation.getFace() == l_lastFace) and (l_lastDirection == Direction.CW) and
                        p_rotation.getDirection() == Direction.CW):
                    l_returnValue = True
                #no three counter clockwise rotations
                if len(self.c_array) > 1:
                    if ((p_rotation.getFace() == l_lastFace) and (l_lastDirection == Direction.CCW) and
                            (p_rotation.getDirection() == Direction.CCW) and
                            (self.c_array[len(self.c_array) - 2].getFace() == l_lastFace) and (l_lastDirection == Direction.CCW) and
                            (self.c_array[len(self.c_array) - 2].getDirection() == Direction.CCW)):
                        l_returnValue = True
                else:
                    l_returnValue = False
            return l_returnValue

        def writeToFile(self, p_writer):
            for l_itr in self.c_array:
                l_itr.writeToFile(p_writer)
            p_writer.write("\n")
        
        def readFromFile(self, p_reader):
            l_rotation = Rotation()
            self.c_array.Clear()
            while l_rotation.readFromFile(p_reader):
                self.c_array.append((Rotation(l_rotation.getFace(), l_rotation.getDirection())))
            return (len(self.c_array) != 0)
       
        def getSubRotationLinkedList(self):
            return RotationSequence(self.c_array[1, len(self.c_array)])

        def size(self):
            return len(self.c_array)

        def  getFirstRotation(self):
            return self.c_array[0]
        
        def getRotation(self,p_index):
            return self.c_array[p_index]
        
        def isNotEmpty(self):
            return (len(self.c_array) > 0)

        def getCopy(self):
            l_rotationLinkedList = RotationSequence()
            for l_itr in self.c_array:
                l_rotationLinkedList.addRotation(l_itr)
            return l_rotationLinkedList

        def applyToRubik(self,p_rubik):
            for l_itr in self.c_array:
                p_rubik.rotateFace(l_itr.getFace(), l_itr.getDirection())