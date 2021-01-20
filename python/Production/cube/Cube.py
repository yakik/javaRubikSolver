class Cube: 


		@staticmethod
		def getPermutationFromCube(Cube cube):
			return cube.getCopy()
		

		@staticmethod
		def getValue(Cube l_permutation, p_highestFloor):
			l_value = 0
			Cube fixedCube = new Cube()
			l_value = 2 * (8 - l_permutation.countDifferenceFirstFloor(fixedCube))
			if p_highestFloor > 1)
				l_value += 2 * (4 - l_permutation.countDifferenceSecondFloor(fixedCube))
			if p_highestFloor > 2)
				l_value += 2 * (8 - l_permutation.countDifferenceThirdFloor(fixedCube))

			return l_value
		




		Color[,] colors = new Color[6,8]
	
	 def equals(self, Cube comparedCube):
			if countDifferenceFirstFloor(comparedCube) +
					countDifferenceSecondFloor(comparedCube) +
					countDifferenceThirdFloor(comparedCube) == 0)
				return true
			else
				return false
		

		def setColor(self, Face face, LocationInFace locationInFace, Color color):
			colors[(int)face,(int)locationInFace] = color
		

		def getColor(self, Face face, LocationInFace locationInFace):
			return colors[(int)face,(int)locationInFace]
		

		def __init__(self):

			foreach (LocationInFace locationInFace in Enum.GetValues(typeof(LocationInFace))):
				setColor(Face.FRONT, locationInFace, Color.FRONTCOLOR)
				setColor(Face.BACK, locationInFace, Color.BACKCOLOR)
				setColor(Face.RIGHT, locationInFace, Color.RIGHTCOLOR)
				setColor(Face.LEFT, locationInFace, Color.LEFTCOLOR)
				setColor(Face.TOP, locationInFace, Color.TOPCOLOR)
				setColor(Face.BOTTOM, locationInFace, Color.BOTTOMCOLOR)
			

		

		def __init__(self, Cube source):
			foreach (LocationInFace locationInFace in Enum.GetValues(typeof(LocationInFace)))
			
				setColor(Face.FRONT, locationInFace, source.getColor(Face.FRONT, locationInFace))
				setColor(Face.BACK, locationInFace, source.getColor(Face.BACK, locationInFace))
				setColor(Face.RIGHT, locationInFace, source.getColor(Face.RIGHT, locationInFace))
				setColor(Face.LEFT, locationInFace, source.getColor(Face.LEFT, locationInFace))
				setColor(Face.TOP, locationInFace, source.getColor(Face.TOP, locationInFace))
				setColor(Face.BOTTOM, locationInFace, source.getColor(Face.BOTTOM, locationInFace))
			
		

		def rotateFace(self, Face face, Direction direction):
			switch (face):
				case Face.FRONT:
					rotateFrontFace(direction)
					break
				case Face.RIGHT:
					rotateRightFace(direction)
					break
				case Face.LEFT:
					rotateLeftFace(direction)
					break
				case Face.BACK:
					rotateBackFace(direction)
					break
				case Face.TOP:
					rotateTopFace(direction)
					break
				case Face.BOTTOM:
					rotateBottomFace(direction)
					break
				default:
					break
			

		

		def rotateBottomFace(self, Direction direction):
			if direction == Direction.CW):
				rotateLeftToRightFaceOnly(Face.BOTTOM)

				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOM, Face.LEFT, LocationInFace.BOTTOM, Face.FRONT,
						LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.BOTTOM)
				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMLEFT, Face.LEFT, LocationInFace.BOTTOMLEFT, Face.FRONT,
						LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.BOTTOMLEFT)
				rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMRIGHT, Face.LEFT, LocationInFace.BOTTOMRIGHT, Face.FRONT,
						LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.BOTTOMRIGHT)
			 else:
				if i = 0 i < 3 i++)
					rotateBottomFace(Direction.CW)
			
		

		def rotateTopFace(self, Direction direction):
			if direction == Direction.CW):
				rotateLeftToRightFaceOnly(Face.TOP)

				rotateLeftToRight(Face.BACK, LocationInFace.TOP, Face.RIGHT, LocationInFace.TOP, Face.FRONT,
						LocationInFace.TOP, Face.LEFT, LocationInFace.TOP)
				rotateLeftToRight(Face.BACK, LocationInFace.TOPLEFT, Face.RIGHT, LocationInFace.TOPLEFT, Face.FRONT,
						LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.TOPLEFT)
				rotateLeftToRight(Face.BACK, LocationInFace.TOPRIGHT, Face.RIGHT, LocationInFace.TOPRIGHT, Face.FRONT,
						LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.TOPRIGHT)
			 else:
				if i = 0 i < 3 i++)
					rotateTopFace(Direction.CW)
			
		

		def rotateBackFace(self, Direction direction):
			if direction == Direction.CW):
				rotateLeftToRightFaceOnly(Face.BACK)

				rotateLeftToRight(Face.TOP, LocationInFace.TOP, Face.LEFT, LocationInFace.LEFT, Face.BOTTOM,
						LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.RIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.BOTTOMLEFT, Face.BOTTOM,
						LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.TOPRIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.TOPLEFT, Face.BOTTOM,
						LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.BOTTOMRIGHT)
			 else:
				if i = 0 i < 3 i++)
					rotateBackFace(Direction.CW)
			
		

		def rotateLeftFace(self, Direction direction):
			if direction == Direction.CW):
				rotateLeftToRightFaceOnly(Face.LEFT)

				rotateLeftToRight(Face.TOP, LocationInFace.LEFT,
						Face.FRONT, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.LEFT,
						Face.BACK, LocationInFace.RIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT,
						Face.FRONT, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM, LocationInFace.BOTTOMLEFT,
						Face.BACK, LocationInFace.TOPRIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT,
						Face.FRONT, LocationInFace.TOPLEFT,
						Face.BOTTOM, LocationInFace.TOPLEFT,
						Face.BACK, LocationInFace.BOTTOMRIGHT)
			 else:
				if i = 0 i < 3 i++)
					rotateLeftFace(Direction.CW)
			
		

		def rotateRightFace(self, Direction direction):
			if direction == Direction.CW):
				rotateLeftToRightFaceOnly(Face.RIGHT)

				rotateLeftToRight(Face.TOP, LocationInFace.RIGHT,
						Face.BACK, LocationInFace.LEFT,
						Face.BOTTOM, LocationInFace.RIGHT,
						Face.FRONT, LocationInFace.RIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT,
						Face.BACK, LocationInFace.TOPLEFT,
						Face.BOTTOM, LocationInFace.BOTTOMRIGHT,
						Face.FRONT, LocationInFace.BOTTOMRIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT,
						Face.BACK, LocationInFace.BOTTOMLEFT,
						Face.BOTTOM, LocationInFace.TOPRIGHT,
						Face.FRONT, LocationInFace.TOPRIGHT)
			 else:
				if i = 0 i < 3 i++)
					rotateRightFace(Direction.CW)
			
		

		def rotateFrontFace(self, Direction direction):
			if direction == Direction.CW):
				rotateLeftToRightFaceOnly(Face.FRONT)

				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.LEFT, Face.BOTTOM,
						LocationInFace.TOP, Face.LEFT, LocationInFace.RIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.TOPLEFT, Face.BOTTOM,
						LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.BOTTOMRIGHT)
				rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.BOTTOMLEFT, Face.BOTTOM,
						LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.TOPRIGHT)
			 else:
				if i = 0 i < 3 i++)
					rotateFrontFace(Direction.CW)
			
		

		def rotateLeftToRightFaceOnly(self, Face face):
			rotateLeftToRight(face, LocationInFace.TOP, face, LocationInFace.RIGHT, face, LocationInFace.BOTTOM, face,
					LocationInFace.LEFT)
			rotateLeftToRight(face, LocationInFace.BOTTOMLEFT, face, LocationInFace.TOPLEFT, face, LocationInFace.TOPRIGHT,
					face, LocationInFace.BOTTOMRIGHT)
		

		print(self):
			printFace(Face.TOP)
			printFace(Face.BOTTOM)
			printFace(Face.FRONT)
			printFace(Face.BACK)
			printFace(Face.LEFT)
			printFace(Face.RIGHT)

		

		def printFace(self, Face face):
			Console.Write("\n%S\n\n", FaceHandler.getCharValue(face))
			Console.Write("%11s %11s %11s\n", getColor(face, LocationInFace.TOPLEFT),
					getColor(face, LocationInFace.TOP), getColor(face, LocationInFace.TOPRIGHT))
			Console.Write("%11s             %11s\n", getColor(face, LocationInFace.LEFT),
					getColor(face, LocationInFace.RIGHT))
			Console.Write("%11s %11s %11s\n", getColor(face, LocationInFace.BOTTOMLEFT),
					getColor(face, LocationInFace.BOTTOM), getColor(face, LocationInFace.BOTTOMRIGHT))
		
		//                TL T TR
		//                L TOP R 
		//                BL B BR

		//TL T TR TL T TR TL T TR TL T TR
		//LBACK R LLEFT R LFRONTR LRIGHTR 
		//BL B BR BL B BR BL B BR BL B BR

		//                TL T TR
		//                LBOTTOMR 
		//                BL B BR

		def rotateLeftToRight(self, Face firstFace, LocationInFace firstLocationInFace, Face secondFace,
				LocationInFace secondLocationInFace, Face thirdFace, LocationInFace thirdLocationInFace, Face fourthFace,
				LocationInFace fourthLocationInFace):
			Color temp = getColor(fourthFace, fourthLocationInFace)
			setColor(fourthFace, fourthLocationInFace, getColor(thirdFace, thirdLocationInFace))
			setColor(thirdFace, thirdLocationInFace, getColor(secondFace, secondLocationInFace))
			setColor(secondFace, secondLocationInFace, getColor(firstFace, firstLocationInFace))
			setColor(firstFace, firstLocationInFace, temp)

		

		def countDifferenceSecondFloor(self, Cube cube):
			counter = 0
			if colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.LEFT) or
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.RIGHT))
				counter++
			if colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.LEFT) or
					colorInFaceNotEqual(cube, Face.BACK, LocationInFace.RIGHT))
				counter++
			if colorInFaceNotEqual(cube, Face.BACK, LocationInFace.LEFT) or
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.RIGHT))
				counter++
			if colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.LEFT) or
					colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.RIGHT))
				counter++

			return counter

		


		def countDifferenceFirstFloor(self, Cube cube):
			counter = 0
			if colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOM) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOP))
				counter++
			if colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOM) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.LEFT))
				counter++
			if colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOM) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOM))
				counter++
			if colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOM) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.RIGHT))
				counter++


			if colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOMLEFT) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOPLEFT) or
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOMRIGHT))
				counter++
			if colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOMRIGHT) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOPRIGHT) or
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOMLEFT))
				counter++
			if colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOMRIGHT) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOMLEFT) or
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOMLEFT))
				counter++
			if colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOMLEFT) or
					colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOMRIGHT) or
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOMRIGHT))
				counter++

			return counter

		

		def countDifferenceThirdFloor(self, Cube cube):
			counter = 0
			if colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOP) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOM))
				counter++
			if colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOP) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.LEFT))
				counter++
			if colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOP) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOP))
				counter++
			if colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOP) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.RIGHT))
				counter++


			if colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOPLEFT) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOMLEFT) or
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOPRIGHT))
				counter++
			if colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOPRIGHT) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOMRIGHT) or
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOPLEFT))
				counter++
			if colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOPRIGHT) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOPLEFT) or
					colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOPLEFT))
				counter++
			if colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOPLEFT) or
					colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOPRIGHT) or
					colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOPRIGHT))
				counter++

			return counter

		


		def colorInFaceNotEqual(self, Cube comparedCube, Face face, LocationInFace locationInFace):
			return getColor(face, locationInFace) != comparedCube.getColor(face, LocationInFace.BOTTOM)
		

		def countAllDifferences(self, Cube comparedCube):
			return countDifferenceThirdFloor(comparedCube) +
					countDifferenceFirstFloor(comparedCube) +
					countDifferenceSecondFloor(comparedCube)
		

		def getCopy(self):
			return new Cube(this)
		



	





