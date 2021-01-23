from .face import Face
class Face_handler:

    @staticmethod
    def getCharValue(face):
        if face==Face.TOP:
            return 'U'
        if face==Face.BOTTOM:
            return 'D'
        if face==Face.RIGHT:
            return 'R'
        if face==Face.LEFT:
            return 'L'
        if face==Face.FRONT:
            return 'F'
        if face==Face.BACK:
            return 'B'

       # switcher={Face.TOP: 'U',
       #         Face.BOTTOM: 'D',
       #         Face.RIGHT: 'R',
       #         Face.LEFT: 'L',
       #         Face.FRONT: 'F',
       #         Face.BACK: 'B'}
       # return switcher.get(face)

    @staticmethod
    def getFaceInt(intValue):
        switcher={0: Face.TOP,
                 1: Face.BOTTOM,
                 2: Face.RIGHT,
                 3: Face.LEFT,
                 4: Face.FRONT,
                 5: Face.BACK}
        return switcher.get(intValue)

    @staticmethod
    def getIntFaceValue(intValue):
        switcher = {Face.TOP:0,
                    Face.BOTTOM:1,
                    Face.RIGHT:2,
                    Face.LEFT:3,
                    Face.FRONT:4,
                    Face.BACK:5}
        return switcher.get(intValue)

    @staticmethod
    def getFaceChar(charValue):
        switcher = {'U': Face.TOP,
            'D': Face.BOTTOM,
            'R': Face.RIGHT,
            'L': Face.LEFT,
            'F': Face.FRONT,
            'B': Face.BACK}
        return switcher.get(charValue)

    @staticmethod
    def getOpposite( face):
        switcher = {Face.LEFT: Face.RIGHT,
                    Face.RIGHT: Face.LEFT,
            Face.TOP: Face.BOTTOM,
            Face.BOTTOM: Face.TOP,
            Face.FRONT: Face.BACK,
            Face.BACK: Face.FRONT}
        return switcher.get(face)