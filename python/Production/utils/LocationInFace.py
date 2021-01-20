s


    enum LocationInFace 
        TOP=0,
        BOTTOM=1,
        RIGHT=2,
        LEFT=3,
        TOPRIGHT=4,
        TOPLEFT=5,
        BOTTOMRIGHT=6,
        BOTTOMLEFT=7/*, NOTDEFINED('Z', 9)*/ //don't change this sequence, for Rubik's sake!
    
    class LocationInFaceHandle  
   
    @staticmethod
    def LocationInFace GetLocationInFace( intValue):
            switch (intValue)
            
                case 0:
                    return LocationInFace.TOP
                case 1:
                    return LocationInFace.BOTTOM
                case 2:
                    return LocationInFace.RIGHT
                case 3:
                    return LocationInFace.LEFT
                case 4:
                    return LocationInFace.TOPRIGHT
                case 5:
                    return LocationInFace.TOPLEFT
                case 6:
                    return LocationInFace.BOTTOMRIGHT
                case 7:
                    return LocationInFace.BOTTOMLEFT
                default:
                    return LocationInFace.TOP

            
           
    


   



