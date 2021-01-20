


    class Location
    
        Boolean c_isEdge
        Face c_face0
        Face c_face1
        Face c_face2

        Location():
        

        Boolean containsFace(Face p_face):
            if p_face == c_face0 or p_face == c_face1 or (!c_isEdge and (p_face == c_face2)))
                return true
            else
                return false
        

        Location getCopy():
            if isEdge())
                return new Location(c_face0, c_face1)
            else
                return new Location(c_face0, c_face1, c_face2)
        

        Location(Face p_face0, Face p_face1, Face p_face2):
            Face l_tmp
            c_isEdge = false
            c_face0 = p_face0
            c_face1 = p_face1
            c_face2 = p_face2
            // bubble sort to keep order within faces		
            if (int)c_face0 > (int)c_face1)
            
                l_tmp = c_face1
                c_face1 = c_face0
                c_face0 = l_tmp
            
            if (int)c_face1 > (int)c_face2)
            
                l_tmp = c_face2
                c_face2 = c_face1
                c_face1 = l_tmp
            
            if (int)c_face0 > (int)c_face1)
            
                l_tmp = c_face1
                c_face1 = c_face0
                c_face0 = l_tmp
            

        

        Location(Face p_face0, Face p_face1):
            c_isEdge = true
            //       c_face2 = Face.NOTDEFINED
            c_face0 = p_face0
            c_face1 = p_face1
            if (int)p_face0 > (int)p_face1)
            
                c_face1 = p_face0
                c_face0 = p_face1
            
            else
            
                c_face0 = p_face0
                c_face1 = p_face1
            
        

        Boolean isEdge():
            return c_isEdge
        

        Face getFace0():
            return c_face0
        

        Face getFace1():
            return c_face1
        

        getFloor():
            if this.equals(new Location(Face.TOP, Face.LEFT, Face.FRONT))) return 3
            if this.equals(new Location(Face.TOP, Face.LEFT, Face.BACK))) return 3
            if this.equals(new Location(Face.TOP, Face.RIGHT, Face.FRONT))) return 3
            if this.equals(new Location(Face.TOP, Face.RIGHT, Face.BACK))) return 3
            if this.equals(new Location(Face.BOTTOM, Face.LEFT, Face.FRONT))) return 1
            if this.equals(new Location(Face.BOTTOM, Face.LEFT, Face.BACK))) return 1
            if this.equals(new Location(Face.BOTTOM, Face.RIGHT, Face.FRONT))) return 1
            if this.equals(new Location(Face.BOTTOM, Face.RIGHT, Face.BACK))) return 1

            if this.equals(new Location(Face.TOP, Face.FRONT))) return 3
            if this.equals(new Location(Face.TOP, Face.BACK))) return 3
            if this.equals(new Location(Face.TOP, Face.LEFT))) return 3
            if this.equals(new Location(Face.TOP, Face.RIGHT))) return 3

            if this.equals(new Location(Face.FRONT, Face.LEFT))) return 2
            if this.equals(new Location(Face.FRONT, Face.RIGHT))) return 2
            if this.equals(new Location(Face.BACK, Face.LEFT))) return 2
            if this.equals(new Location(Face.BACK, Face.RIGHT))) return 2

            if this.equals(new Location(Face.BOTTOM, Face.LEFT))) return 1
            if this.equals(new Location(Face.BOTTOM, Face.RIGHT))) return 1
            if this.equals(new Location(Face.FRONT, Face.BOTTOM))) return 1
            if this.equals(new Location(Face.BACK, Face.BOTTOM))) return 1
            return 0
        

        Face getFace2():
            //        if isEdge())
            //            return Face.NOTDEFINED
            //        else
            return c_face2
        

        //	getValue():
        //		return (getFace0() * 1 + getFace1() * 6 + getFace2() * 36 + isEdge() * 216)
        //	

        Boolean equals(Location p_location):
            return ((c_face0 == p_location.c_face0) and
                    (c_face1 == p_location.c_face1) and
                    (c_face2 == p_location.c_face2) and
                    (c_isEdge == p_location.c_isEdge))
        


        String getString():
            if c_isEdge)
                return String.Format("0, 1", FaceHandler.getCharValue(c_face0), FaceHandler.getCharValue(c_face1))
            else
            
                return String.Format("0, 1, 2", FaceHandler.getCharValue(c_face0), FaceHandler.getCharValue(c_face1), FaceHandler.getCharValue(c_face2))
            
        

    
