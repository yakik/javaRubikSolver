from production.utils.color import Color
from production.utils.face import Face
from production.utils.location import Location
from production.utils.rotation import Rotation
from production.utils.location_in_face import Location_in_face
from production.utils.location_in_face_handler import Location_in_face_handler
from production.utils.direction import Direction
from production.utils.face_handler import Face_handler

class Cube:

	@staticmethod
	def getPermutationFromCube(cube):
		return cube.getCopy()

	@staticmethod
	def getValue(l_permutation, p_highestFloor):
		l_value = 0
		fixedCube = Cube()
		l_value = 2 * (8 - l_permutation.countDifferenceFirstFloor(fixedCube))
		if p_highestFloor > 1:
			l_value += 2 * (4 - l_permutation.countDifferenceSecondFloor(fixedCube))
		if p_highestFloor > 2:
			l_value += 2 * (8 - l_permutation.countDifferenceThirdFloor(fixedCube))
		return l_value

	def equals(self,comparedCube):
		if (self.countDifferenceFirstFloor(comparedCube) + 
				self.countDifferenceSecondFloor(comparedCube) +
				self.countDifferenceThirdFloor(comparedCube)) == 0:
			return True
		else:
			return False

	
	
	def setColor(self,face,locationInFace, color):
		self.colors[face.value][locationInFace.value]=color

	def getColor(self,face,locationInFace):
		return self.colors[face.value][locationInFace.value]


	@staticmethod
	def getColorForFaceForSortedCube(face):
		if face==Face.TOP:
			return Color.TOPCOLOR
		if face==Face.BOTTOM:
			return Color.BOTTOMCOLOR
		if face==Face.RIGHT:
			return Color.RIGHTCOLOR
		if face==Face.LEFT:
			return Color.LEFTCOLOR
		if face==Face.FRONT:
			return Color.FRONTCOLOR
		if face==Face.BACK:
			return Color.BACKCOLOR


	def __init__(self,source=None):
		self.colors = [[Color.TOPCOLOR,Color.TOPCOLOR,Color.TOPCOLOR,Color.TOPCOLOR,Color.TOPCOLOR,Color.TOPCOLOR,Color.TOPCOLOR,Color.TOPCOLOR],
						[Color.BOTTOMCOLOR,Color.BOTTOMCOLOR,Color.BOTTOMCOLOR,Color.BOTTOMCOLOR,Color.BOTTOMCOLOR,Color.BOTTOMCOLOR,Color.BOTTOMCOLOR,Color.BOTTOMCOLOR],
						[Color.RIGHTCOLOR,Color.RIGHTCOLOR,Color.RIGHTCOLOR,Color.RIGHTCOLOR,Color.RIGHTCOLOR,Color.RIGHTCOLOR,Color.RIGHTCOLOR,Color.RIGHTCOLOR],
						[Color.LEFTCOLOR,Color.LEFTCOLOR,Color.LEFTCOLOR,Color.LEFTCOLOR,Color.LEFTCOLOR,Color.LEFTCOLOR,Color.LEFTCOLOR,Color.LEFTCOLOR],
						[Color.FRONTCOLOR,Color.FRONTCOLOR,Color.FRONTCOLOR,Color.FRONTCOLOR,Color.FRONTCOLOR,Color.FRONTCOLOR,Color.FRONTCOLOR,Color.FRONTCOLOR],
						[Color.BACKCOLOR,Color.BACKCOLOR,Color.BACKCOLOR,Color.BACKCOLOR,Color.BACKCOLOR,Color.BACKCOLOR,Color.BACKCOLOR,Color.BACKCOLOR]]



		#	[[0 for x in range(8)] for y in range(6)]
		#for face in list(Face):
		#	for locationInFace in list(Location_in_face):
		#		self.colors[face.value][locationInFace.value]=Cube.getColorForFaceForSortedCube(face)

		if source!=None:
			for locationInFace in list(Location_in_face):
				self.setColor(Face.FRONT, locationInFace, source.getColor(Face.FRONT, locationInFace))
				self.setColor(Face.BACK, locationInFace, source.getColor(Face.BACK, locationInFace))
				self.setColor(Face.RIGHT, locationInFace, source.getColor(Face.RIGHT, locationInFace))
				self.setColor(Face.LEFT, locationInFace, source.getColor(Face.LEFT, locationInFace))
				self.setColor(Face.TOP, locationInFace, source.getColor(Face.TOP, locationInFace))
				self.setColor(Face.BOTTOM, locationInFace, source.getColor(Face.BOTTOM, locationInFace))

	def rotateFace(self,face,direction):
		if face==Face.FRONT:
			self.rotateFrontFace(direction)
			return
		if face == Face.RIGHT:
			self.rotateRightFace(direction)
			return
		if face == Face.LEFT:
			self.rotateLeftFace(direction)
			return
		if face == Face.BACK:
			self.rotateBackFace(direction)
			return
		if face == Face.TOP:
			self.rotateTopFace(direction)
			return
		if face == Face.BOTTOM:
			self.rotateBottomFace(direction)
			return

		#switcher={Face.FRONT:self.rotateFrontFace,
		#		Face.RIGHT:self.rotateRightFace,
		#		Face.LEFT:self.rotateLeftFace,
		#		Face.BACK:self.rotateBackFace,
		#		Face.TOP:self.rotateTopFace,
		#		Face.BOTTOM:self.rotateBottomFace}
		#switcher.get(face)(direction)

	def rotateBottomFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.BOTTOM)

			self.rotateLeftToRight(Face.BACK, Location_in_face.BOTTOM, Face.LEFT, Location_in_face.BOTTOM, Face.FRONT,
								   Location_in_face.BOTTOM, Face.RIGHT, Location_in_face.BOTTOM)
			self.rotateLeftToRight(Face.BACK, Location_in_face.BOTTOMLEFT, Face.LEFT, Location_in_face.BOTTOMLEFT, Face.FRONT,
								   Location_in_face.BOTTOMLEFT, Face.RIGHT, Location_in_face.BOTTOMLEFT)
			self.rotateLeftToRight(Face.BACK, Location_in_face.BOTTOMRIGHT, Face.LEFT, Location_in_face.BOTTOMRIGHT, Face.FRONT,
								   Location_in_face.BOTTOMRIGHT, Face.RIGHT, Location_in_face.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotateBottomFace(Direction.CW)

	def rotateTopFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.TOP)
			self.rotateLeftToRight(Face.BACK, Location_in_face.TOP, Face.RIGHT, Location_in_face.TOP, Face.FRONT,
								   Location_in_face.TOP, Face.LEFT, Location_in_face.TOP)
			self.rotateLeftToRight(Face.BACK, Location_in_face.TOPLEFT, Face.RIGHT, Location_in_face.TOPLEFT, Face.FRONT,
								   Location_in_face.TOPLEFT, Face.LEFT, Location_in_face.TOPLEFT)
			self.rotateLeftToRight(Face.BACK, Location_in_face.TOPRIGHT, Face.RIGHT, Location_in_face.TOPRIGHT, Face.FRONT,
								   Location_in_face.TOPRIGHT, Face.LEFT, Location_in_face.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotateTopFace(Direction.CW)

	def rotateBackFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.BACK)
			self.rotateLeftToRight(Face.TOP, Location_in_face.TOP, Face.LEFT, Location_in_face.LEFT, Face.BOTTOM,
								   Location_in_face.BOTTOM, Face.RIGHT, Location_in_face.RIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.TOPLEFT, Face.LEFT, Location_in_face.BOTTOMLEFT, Face.BOTTOM,
								   Location_in_face.BOTTOMRIGHT, Face.RIGHT, Location_in_face.TOPRIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.TOPRIGHT, Face.LEFT, Location_in_face.TOPLEFT, Face.BOTTOM,
								   Location_in_face.BOTTOMLEFT, Face.RIGHT, Location_in_face.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotateBackFace(Direction.CW)

	def rotateLeftFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.LEFT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.LEFT,
								   Face.FRONT, Location_in_face.LEFT,
								   Face.BOTTOM, Location_in_face.LEFT,
								   Face.BACK, Location_in_face.RIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.BOTTOMLEFT,
								   Face.FRONT, Location_in_face.BOTTOMLEFT,
								   Face.BOTTOM, Location_in_face.BOTTOMLEFT,
								   Face.BACK, Location_in_face.TOPRIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.TOPLEFT,
								   Face.FRONT, Location_in_face.TOPLEFT,
								   Face.BOTTOM, Location_in_face.TOPLEFT,
								   Face.BACK, Location_in_face.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotateLeftFace(Direction.CW)

	def rotateRightFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.RIGHT)

			self.rotateLeftToRight(Face.TOP, Location_in_face.RIGHT,
								   Face.BACK, Location_in_face.LEFT,
								   Face.BOTTOM, Location_in_face.RIGHT,
								   Face.FRONT, Location_in_face.RIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.BOTTOMRIGHT,
								   Face.BACK, Location_in_face.TOPLEFT,
								   Face.BOTTOM, Location_in_face.BOTTOMRIGHT,
								   Face.FRONT, Location_in_face.BOTTOMRIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.TOPRIGHT,
								   Face.BACK, Location_in_face.BOTTOMLEFT,
								   Face.BOTTOM, Location_in_face.TOPRIGHT,
								   Face.FRONT, Location_in_face.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotateRightFace(Direction.CW)

	def rotateFrontFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.FRONT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.BOTTOM, Face.RIGHT, Location_in_face.LEFT, Face.BOTTOM,
								   Location_in_face.TOP, Face.LEFT, Location_in_face.RIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.BOTTOMLEFT, Face.RIGHT, Location_in_face.TOPLEFT, Face.BOTTOM,
								   Location_in_face.TOPRIGHT, Face.LEFT, Location_in_face.BOTTOMRIGHT)
			self.rotateLeftToRight(Face.TOP, Location_in_face.BOTTOMRIGHT, Face.RIGHT, Location_in_face.BOTTOMLEFT, Face.BOTTOM,
								   Location_in_face.TOPLEFT, Face.LEFT, Location_in_face.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotateFrontFace(Direction.CW)

	def rotateLeftToRightFaceOnly(self,face):
		self.rotateLeftToRight(face, Location_in_face.TOP, face, Location_in_face.RIGHT, face, Location_in_face.BOTTOM, face,
							   Location_in_face.LEFT)
		self.rotateLeftToRight(face, Location_in_face.BOTTOMLEFT, face, Location_in_face.TOPLEFT, face, Location_in_face.TOPRIGHT,
							   face, Location_in_face.BOTTOMRIGHT)

	def print(self):
		self.printFace(Face.TOP)
		self.printFace(Face.BOTTOM)
		self.printFace(Face.FRONT)
		self.printFace(Face.BACK)
		self.printFace(Face.LEFT)
		self.printFace(Face.RIGHT)

	def printFace(self,face):
		print ("\n" + Face_handler.getCharValue(face) + "\n\n")
		print(self.getColor(face, Location_in_face.TOPLEFT) + " " +
			  self.getColor(face, Location_in_face.TOP) + " " + self.getColor(face, Location_in_face.TOPRIGHT) + "\n")
		print(self.getColor(face, Location_in_face.LEFT) + " " +
			  self.getColor(face, Location_in_face.RIGHT) + "\n")
		print(self.getColor(face, Location_in_face.BOTTOMLEFT) + " " +
			  self.getColor(face, Location_in_face.BOTTOM) + " " + self.getColor(face, Location_in_face.BOTTOMRIGHT) + "\n")
	
	#                TL T TR
	#                L TOP R 
	#                BL B BR

	#TL T TR TL T TR TL T TR TL T TR
	#LBACK R LLEFT R LFRONTR LRIGHTR 
	#BL B BR BL B BR BL B BR BL B BR

	#                TL T TR
	#                LBOTTOMR 
	#                BL B BR

	def rotateLeftToRight(self,firstFace,firstLocationInFace,secondFace,
			 secondLocationInFace,thirdFace,thirdLocationInFace,fourthFace,
			 fourthLocationInFace):
		temp = self.getColor(fourthFace, fourthLocationInFace)
		self.setColor(fourthFace, fourthLocationInFace, self.getColor(thirdFace, thirdLocationInFace))
		self.setColor(thirdFace, thirdLocationInFace, self.getColor(secondFace, secondLocationInFace))
		self.setColor(secondFace, secondLocationInFace, self.getColor(firstFace, firstLocationInFace))
		self.setColor(firstFace, firstLocationInFace, temp)

	def countDifferenceSecondFloor(self,cube):
		counter = 0
		if (self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.LEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.LEFT) or
				self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.LEFT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.LEFT) or
				self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.RIGHT)):
			counter+=1
		return counter

	def countDifferenceFirstFloor(self,cube):
		counter = 0
		if (self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.TOP)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.LEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.BOTTOM)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.BOTTOMRIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.BOTTOMLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.BOTTOMLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, Location_in_face.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.BOTTOMRIGHT)):
			counter+=1
		return counter

	def countDifferenceThirdFloor(self,cube):
		counter = 0
		if (self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.BOTTOM)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.LEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.TOP)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.TOPRIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.FRONT, Location_in_face.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.TOPLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, Location_in_face.TOPLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, Location_in_face.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.TOP, Location_in_face.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, Location_in_face.TOPRIGHT)):
			counter+=1
		return counter

	def colorInFaceNotEqual(self,comparedCube,face,locationInFace):
		return self.getColor(face, locationInFace) != comparedCube.getColor(face, Location_in_face.BOTTOM)

	def countAllDifferences(self,comparedCube):
		return (self.countDifferenceThirdFloor(comparedCube) +
				self.countDifferenceFirstFloor(comparedCube) +
				self.countDifferenceSecondFloor(comparedCube))
	

	def getCopy(self):
		return Cube(self)
	



	





