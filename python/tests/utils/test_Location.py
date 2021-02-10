import unittest
from production.utils.location import Location

class LocationTest(unittest.TestCase):
    

        
    def test_isEdge(self):
        myLocation= Location("BOTTOM", "LEFT", "FRONT")
        self.assertEqual(False, myLocation.isEdge())
        myLocation= Location("BOTTOM", "LEFT")
        self.assertEqual(True, myLocation.isEdge())
    

    
    def test_getFaces(self):
        myLocation= Location("BOTTOM", "LEFT", "FRONT")
        #taking into account facecs are sorted according to value
        self.assertEqual("BOTTOM", myLocation.getFace0(),"1")
        self.assertEqual("FRONT", myLocation.getFace1(),"2")
        self.assertEqual("LEFT", myLocation.getFace2(),"3")
    

    
    def test_equals(self):
        myLocation= Location("BOTTOM", "LEFT", "FRONT")
        mySecond= Location("LEFT", "FRONT", "BOTTOM")
        myThird= Location("RIGHT", "FRONT", "BOTTOM")
        self.assertEqual(True, mySecond.equals(myLocation))
        self.assertEqual(False, mySecond.equals(myThird))
    

    
    def test_GetFloor(self):
        self.assertEqual(3, Location("TOP", "LEFT", "FRONT").getFloor(), "1")
        self.assertEqual(3, Location("TOP", "LEFT", "BACK").getFloor(), "2")
        self.assertEqual(3, Location("TOP", "RIGHT", "FRONT").getFloor(), "3")
        self.assertEqual(3, Location("TOP", "RIGHT", "BACK").getFloor(), "4")
        self.assertEqual(1, Location("BOTTOM", "LEFT", "FRONT").getFloor(), "5")
        self.assertEqual(1, Location("BOTTOM", "LEFT", "BACK").getFloor(), "6")
        self.assertEqual(1, Location("BOTTOM", "RIGHT", "FRONT").getFloor(), "7")
        self.assertEqual(1, Location("BOTTOM", "RIGHT", "BACK").getFloor(), "8")

        self.assertEqual(3, Location("TOP", "FRONT").getFloor(), "10")
        self.assertEqual(3, Location("TOP", "BACK").getFloor(), "11")
        self.assertEqual(3, Location("TOP", "LEFT").getFloor(), "12")
        self.assertEqual(3, Location("TOP", "RIGHT").getFloor(), "13")

        self.assertEqual(2, Location("FRONT", "LEFT").getFloor(), "14")
        self.assertEqual(2, Location("FRONT", "RIGHT").getFloor(), "15")
        self.assertEqual(2, Location("BACK", "LEFT").getFloor(), "16")
        self.assertEqual(2, Location("BACK", "RIGHT").getFloor(), "17")

        self.assertEqual(1, Location("BOTTOM", "LEFT").getFloor(), "18")
        self.assertEqual(1, Location("BOTTOM", "RIGHT").getFloor(), "19")
        self.assertEqual(1, Location("FRONT", "BOTTOM").getFloor(), "20")
        self.assertEqual(1, Location("BACK", "BOTTOM").getFloor(), "21")


    

    
    def test_getString(self):
        myLocation= Location("BOTTOM", "LEFT", "FRONT")
        self.assertEqual("D, F, L", myLocation.getString(),"first")
        myLocation= Location("BOTTOM", "LEFT")
        self.assertEqual("D, L", myLocation.getString(),"second")

    

