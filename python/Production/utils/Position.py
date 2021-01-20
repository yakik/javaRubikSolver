


    class Position 

    Face[,] g_faceOrder = new Face[,]
            Face.FRONT, Face.LEFT, Face.BACK, Face.RIGHT, Face.RIGHT, Face.BACK, Face.LEFT, Face.FRONT
    , Face.TOP, Face.BACK, Face.BOTTOM, Face.FRONT
    , Face.TOP, Face.FRONT, Face.BOTTOM, Face.BACK
    , Face.TOP, Face.RIGHT, Face.BOTTOM, Face.LEFT
    , Face.TOP, Face.LEFT, Face.BOTTOM, Face.RIGHT
    
    
    Face c_currentUp
    Face c_currentFront

    def Position(Face p_Up, Face p_Front):
        c_currentUp = p_Up
        c_currentFront = p_Front
    

    def Position(self):
        c_currentUp = Face.TOP
        c_currentFront = Face.FRONT
    

    def getString(self):
        return String.Format("0, 1", FaceHandler.getCharValue(c_currentUp), FaceHandler.getCharValue(c_currentFront))
    

    def rotate(Rotation p_rotation):
        Face l_temp
        Face l_face = p_rotation.getFace()
        Direction l_direction = p_rotation.getDirection()
        if l_face == Face.TOP)
            if l_direction == Direction.CW)
                c_currentFront = getFace(Face.RIGHT)
            else
                c_currentFront = getFace(Face.LEFT)
        else if l_face == Face.RIGHT)
            if l_direction == Direction.CW):
                l_temp = c_currentFront
                c_currentFront = getFace(Face.BOTTOM)
                c_currentUp = l_temp
             else:
                l_temp = getFace(Face.BACK)
                c_currentFront = c_currentUp
                c_currentUp = l_temp
            
        else if l_face == Face.FRONT)
            if l_direction == Direction.CW)
                c_currentUp = getFace(Face.LEFT)
            else
                c_currentUp = getFace(Face.RIGHT)
        else
            rotate(new Rotation(FaceHandler.getOpposite(l_face), DirectionHandler.getOpposite(l_direction)))

    

def getCopy()
        return new Position(c_currentUp,c_currentFront)

    Face getFace(Face p_viewpoint):
        if p_viewpo== Face.TOP)
            return c_currentUp
        else if p_viewpo== Face.BOTTOM)
            return FaceHandler.getOpposite(c_currentUp)
        else
            return getHorizonalFacebyVirtual(p_viewpoint)
    


    def getHorizonalFacebyVirtual(Face p_viewpoint):
        i = 0

        while g_faceOrder[(int)c_currentUp,i] != c_currentFront and i < 4)
            i++
        switch (p_viewpoint):
            case Face.FRONT:
                return g_faceOrder[(int)c_currentUp,i]

            case Face.LEFT:
                return g_faceOrder[(int)c_currentUp,(i + 1) % 4]

            case Face.BACK:
                return g_faceOrder[(int)c_currentUp,(i + 2) % 4]

            case Face.RIGHT:
                return g_faceOrder[(int)c_currentUp,(i + 3) % 4]

            default:
                return Face.TOP

        
    

    def equals(Position p_position):
        return ((c_currentUp == p_position.c_currentUp) and
                (c_currentFront == p_position.c_currentFront))
    
