
from production.utils.rotation import Rotation
from production.utils.direction import Direction
from production.utils.face_handler import Face_handler

class Rotation_sequence:

        def __init__(self, p_List=None):
            if p_List==None:
                self.c_array = list()
            else:
                self.c_array = p_List

        def print(self):
            for l_itr in self.c_array:
                l_itr.print()
            print("\n")

        def add_rotation(self, p_rotation):
            self.c_array.append(p_rotation)

        def remove_rotation(self):
            self.c_array.RemoveAt(len(self.c_array) - 1)

        def is_redundant(self, p_rotation):
            l_returnValue = False
            if len(self.c_array) > 0:
                l_lastFace = self.c_array[(len(self.c_array) - 1)].getFace()
                l_lastDirection = self.c_array[len(self.c_array) - 1].getDirection()
                # rotation is opposite to previous
                if self.c_array[len(self.c_array) - 1].getReverse().equals(p_rotation):
                    l_returnValue = True
                # previouswas opposite and previousgreater then current face
                if (p_rotation.getFace() == Face_handler.getOpposite(l_lastFace) and (l_lastFace > p_rotation.getFace())):
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

        def write_to_file(self, p_writer):
            for l_itr in self.c_array:
                l_itr.write_to_file(p_writer)
            p_writer.write("\n")
        
        def read_from_file(self, p_reader):
            l_rotation = Rotation()
            self.c_array.clear()
            while l_rotation.read_from_file(p_reader):
                self.c_array.append((Rotation(l_rotation.getFace(), l_rotation.getDirection())))
            return (len(self.c_array) != 0)
       
        def get_sub_rotation_linked_list(self):
            return Rotation_sequence(self.c_array[1, len(self.c_array)])

        def size(self):
            return len(self.c_array)

        def get_first_rotation(self):
            return self.c_array[0]
        
        def get_rotation(self,p_index):
            return self.c_array[p_index]
        
        def is_not_empty(self):
            return (len(self.c_array) > 0)

        def get_copy(self):
            l_rotationLinkedList = Rotation_sequence()
            for l_itr in self.c_array:
                l_rotationLinkedList.add_rotation(l_itr)
            return l_rotationLinkedList

        def apply_to_rubik(self,p_rubik):
            for l_itr in self.c_array:
                p_rubik.rotate_face(l_itr.getFace(), l_itr.getDirection())