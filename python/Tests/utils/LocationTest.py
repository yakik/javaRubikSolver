import unittest
class LocationTest(unittest.TestCase):
    

        
        def isEdge(self):
            myLocation= Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            self.assertEqual(False, myLocation.isEdge())
            my= Location(Face.BOTTOM, Face.LEFT)
            self.assertEqual(True, myLocation.isEdge())
        

        
        def getFaces(self):
            myLocation= Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            #taking into account facecs are sorted according to value
            self.assertEqual(Face.BOTTOM, myLocation.getFace0())
            self.assertEqual(Face.LEFT, myLocation.getFace1())
            self.assertEqual(Face.FRONT, myLocation.getFace2())
        

        
        def equals(self):
            myLocation= Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            mySecond= Location(Face.LEFT, Face.FRONT, Face.BOTTOM)
            myThird= Location(Face.RIGHT, Face.FRONT, Face.BOTTOM)
            self.assertEqual(True, mySecondLocation.equals(myLocation))
            self.assertEqual(False, mySecondLocation.equals(myThirdLocation))
        

        
        def testGetFloor(self):
            self.assertEqual(3, Location(Face.TOP, Face.LEFT, Face.FRONT).getFloor(), "1")
            self.assertEqual(3, Location(Face.TOP, Face.LEFT, Face.BACK).getFloor(), "2")
            self.assertEqual(3, Location(Face.TOP, Face.RIGHT, Face.FRONT).getFloor(), "3")
            self.assertEqual(3, Location(Face.TOP, Face.RIGHT, Face.BACK).getFloor(), "4")
            self.assertEqual(1, Location(Face.BOTTOM, Face.LEFT, Face.FRONT).getFloor(), "5")
            self.assertEqual(1, Location(Face.BOTTOM, Face.LEFT, Face.BACK).getFloor(), "6")
            self.assertEqual(1, Location(Face.BOTTOM, Face.RIGHT, Face.FRONT).getFloor(), "7")
            self.assertEqual(1, Location(Face.BOTTOM, Face.RIGHT, Face.BACK).getFloor(), "8")

            self.assertEqual(3, Location(Face.TOP, Face.FRONT).getFloor(), "10")
            self.assertEqual(3, Location(Face.TOP, Face.BACK).getFloor(), "11")
            self.assertEqual(3, Location(Face.TOP, Face.LEFT).getFloor(), "12")
            self.assertEqual(3, Location(Face.TOP, Face.RIGHT).getFloor(), "13")

            self.assertEqual(2, Location(Face.FRONT, Face.LEFT).getFloor(), "14")
            self.assertEqual(2, Location(Face.FRONT, Face.RIGHT).getFloor(), "15")
            self.assertEqual(2, Location(Face.BACK, Face.LEFT).getFloor(), "16")
            self.assertEqual(2, Location(Face.BACK, Face.RIGHT).getFloor(), "17")

            self.assertEqual(1, Location(Face.BOTTOM, Face.LEFT).getFloor(), "18")
            self.assertEqual(1, Location(Face.BOTTOM, Face.RIGHT).getFloor(), "19")
            self.assertEqual(1, Location(Face.FRONT, Face.BOTTOM).getFloor(), "20")
            self.assertEqual(1, Location(Face.BACK, Face.BOTTOM).getFloor(), "21")


        

        
        def getString(self):
            myLocation= Location(Face.BOTTOM, Face.LEFT, Face.FRONT)
            self.assertEqual("D, L, F", myLocation.getString(),"first")
            myLocation= Location(Face.BOTTOM, Face.LEFT)
            self.assertEqual("D, L", myLocation.getString(),"second")

        
    
