from production.utils.color import Color
from production.utils.face import Face
from production.utils.location import Location
from production.utils.rotation import Rotation
from production.utils.locationInFace import LocationInFace
from production.utils.direction import Direction
from production.utils.faceHandler import FaceHandler

class Cube:

	@staticmethod
	def getPermutationFromCube(cube):
		return cube.getCopy()

	@staticmethod
	def getValue(l_permutation, p_highestFloor):
		l_value = 0
		fixedCube = Cube()
		l_value = 2 * (8 - l_permutation.self.countDifferenceFirstFloor(fixedCube))
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
		self.colors[locationInFace] = color
	

	def getColor(self,face,locationInFace):
		return self.colors[locationInFace]
	

	def __init__(self,source):
		self.colors = list()
		if source==None:
			for locationInFace in LocationInFace:
				self.setColor(Face.FRONT, locationInFace, Color.FRONTCOLOR)
				self.setColor(Face.BACK, locationInFace, Color.BACKCOLOR)
				self.setColor(Face.RIGHT, locationInFace, Color.RIGHTCOLOR)
				self.setColor(Face.LEFT, locationInFace, Color.LEFTCOLOR)
				self.setColor(Face.TOP, locationInFace, Color.TOPCOLOR)
				self.setColor(Face.BOTTOM, locationInFace, Color.BOTTOMCOLOR)

		else:
			for locationInFace in LocationInFace:
				self.setColor(Face.FRONT, locationInFace, source.getColor(Face.FRONT, locationInFace))
				self.setColor(Face.BACK, locationInFace, source.getColor(Face.BACK, locationInFace))
				self.setColor(Face.RIGHT, locationInFace, source.getColor(Face.RIGHT, locationInFace))
				self.setColor(Face.LEFT, locationInFace, source.getColor(Face.LEFT, locationInFace))
				self.setColor(Face.TOP, locationInFace, source.getColor(Face.TOP, locationInFace))
				self.setColor(Face.BOTTOM, locationInFace, source.getColor(Face.BOTTOM, locationInFace))
		
	

	def rotateFace(self,face,direction):
		switcher={Face.FRONT:self.rotateFrontFace,
				Face.RIGHT:self.rotateRightFace,
				Face.LEFT:self.rotateLeftFace,
				Face.BACK:self.rotateBackFace,
				Face.TOP:self.rotateTopFace,
				Face.BOTTOM:self.rotateBottomFace(direction)}
				
		switcher.get(face)(direction)
		

	

	def rotateBottomFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.BOTTOM)

			self.rotateLeftToRight(Face.BACK, LocationInFace.BOTTOM, Face.LEFT, LocationInFace.BOTTOM, Face.FRONT,
					LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.BOTTOM)
			self.rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMLEFT, Face.LEFT, LocationInFace.BOTTOMLEFT, Face.FRONT,
					LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.BOTTOMLEFT)
			self.rotateLeftToRight(Face.BACK, LocationInFace.BOTTOMRIGHT, Face.LEFT, LocationInFace.BOTTOMRIGHT, Face.FRONT,
					LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotateBottomFace(Direction.CW)
		
	

	def rotateTopFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.TOP)

			self.rotateLeftToRight(Face.BACK, LocationInFace.TOP, Face.RIGHT, LocationInFace.TOP, Face.FRONT,
					LocationInFace.TOP, Face.LEFT, LocationInFace.TOP)
			self.rotateLeftToRight(Face.BACK, LocationInFace.TOPLEFT, Face.RIGHT, LocationInFace.TOPLEFT, Face.FRONT,
					LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.TOPLEFT)
			self.rotateLeftToRight(Face.BACK, LocationInFace.TOPRIGHT, Face.RIGHT, LocationInFace.TOPRIGHT, Face.FRONT,
					LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotateTopFace(Direction.CW)
		
	

	def rotateBackFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.BACK)

			self.rotateLeftToRight(Face.TOP, LocationInFace.TOP, Face.LEFT, LocationInFace.LEFT, Face.BOTTOM,
					LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.RIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.BOTTOMLEFT, Face.BOTTOM,
					LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.TOPRIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.TOPLEFT, Face.BOTTOM,
					LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotateBackFace(Direction.CW)
		
	

	def rotateLeftFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.LEFT)

			self.rotateLeftToRight(Face.TOP, LocationInFace.LEFT,
					Face.FRONT, LocationInFace.LEFT,
					Face.BOTTOM, LocationInFace.LEFT,
					Face.BACK, LocationInFace.RIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT,
					Face.FRONT, LocationInFace.BOTTOMLEFT,
					Face.BOTTOM, LocationInFace.BOTTOMLEFT,
					Face.BACK, LocationInFace.TOPRIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.TOPLEFT,
					Face.FRONT, LocationInFace.TOPLEFT,
					Face.BOTTOM, LocationInFace.TOPLEFT,
					Face.BACK, LocationInFace.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotateLeftFace(Direction.CW)
		
	

	def rotateRightFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.RIGHT)

			self.rotateLeftToRight(Face.TOP, LocationInFace.RIGHT,
					Face.BACK, LocationInFace.LEFT,
					Face.BOTTOM, LocationInFace.RIGHT,
					Face.FRONT, LocationInFace.RIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT,
					Face.BACK, LocationInFace.TOPLEFT,
					Face.BOTTOM, LocationInFace.BOTTOMRIGHT,
					Face.FRONT, LocationInFace.BOTTOMRIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.TOPRIGHT,
					Face.BACK, LocationInFace.BOTTOMLEFT,
					Face.BOTTOM, LocationInFace.TOPRIGHT,
					Face.FRONT, LocationInFace.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotateRightFace(Direction.CW)
		
	

	def rotateFrontFace(self,direction):
		if direction == Direction.CW:
			self.rotateLeftToRightFaceOnly(Face.FRONT)

			self.rotateLeftToRight(Face.TOP, LocationInFace.BOTTOM, Face.RIGHT, LocationInFace.LEFT, Face.BOTTOM,
					LocationInFace.TOP, Face.LEFT, LocationInFace.RIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMLEFT, Face.RIGHT, LocationInFace.TOPLEFT, Face.BOTTOM,
					LocationInFace.TOPRIGHT, Face.LEFT, LocationInFace.BOTTOMRIGHT)
			self.rotateLeftToRight(Face.TOP, LocationInFace.BOTTOMRIGHT, Face.RIGHT, LocationInFace.BOTTOMLEFT, Face.BOTTOM,
					LocationInFace.TOPLEFT, Face.LEFT, LocationInFace.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotateFrontFace(Direction.CW)
		
	

	def rotateLeftToRightFaceOnly(self,face):
		self.rotateLeftToRight(face, LocationInFace.TOP, face, LocationInFace.RIGHT, face, LocationInFace.BOTTOM, face,
				LocationInFace.LEFT)
		self.rotateLeftToRight(face, LocationInFace.BOTTOMLEFT, face, LocationInFace.TOPLEFT, face, LocationInFace.TOPRIGHT,
				face, LocationInFace.BOTTOMRIGHT)
	

	def print(self):
		self.printFace(Face.TOP)
		self.printFace(Face.BOTTOM)
		self.printFace(Face.FRONT)
		self.printFace(Face.BACK)
		self.printFace(Face.LEFT)
		self.printFace(Face.RIGHT)

	

	def printFace(self,face):
		print ("\n"+ FaceHandler.getCharValue(face)+"\n\n")
		print(self.getColor(face, LocationInFace.TOPLEFT)+" "+
				self.getColor(face, LocationInFace.TOP)+" "+ self.getColor(face, LocationInFace.TOPRIGHT)+"\n")
		print("self.getColor(face, LocationInFace.LEFT)+" "+
				self.getColor(face, LocationInFace.RIGHT)+"\n")
		print(self.getColor(face, LocationInFace.BOTTOMLEFT)+" "+
				self.getColor(face, LocationInFace.BOTTOM)+" "+ self.getColor(face, LocationInFace.BOTTOMRIGHT)+"\n")
	
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
		temp = getColor(fourthFace, fourthLocationInFace)
		setColor(fourthFace, fourthLocationInFace, getColor(thirdFace, thirdLocationInFace))
		setColor(thirdFace, thirdLocationInFace, getColor(secondFace, secondLocationInFace))
		setColor(secondFace, secondLocationInFace, getColor(firstFace, firstLocationInFace))
		setColor(firstFace, firstLocationInFace, temp)

	

	def countDifferenceSecondFloor(self,cube):
		counter = 0
		if (self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.LEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.LEFT) or
				self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.LEFT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.RIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.LEFT) or
				self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.RIGHT)):
			counter+=1

		return counter

	


	def countDifferenceFirstFloor(self,cube):
		counter = 0
		if (self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOP)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.LEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOM)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOM) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.RIGHT)):
			counter+=1


		if (self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOMRIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOMLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.BOTTOMLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.BOTTOM, LocationInFace.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.BOTTOMRIGHT)):
			counter+=1

		return counter

	

	def countDifferenceThirdFloor(self,cube):
		counter = 0
		if (self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOM)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.LEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOP)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOP) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.RIGHT)):
			counter+=1


		if (self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOMLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOPRIGHT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.FRONT, LocationInFace.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.BOTTOMRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOPLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.LEFT, LocationInFace.TOPLEFT)):
			counter+=1
		if (self.colorInFaceNotEqual(cube, Face.BACK, LocationInFace.TOPLEFT) or
				self.colorInFaceNotEqual(cube, Face.TOP, LocationInFace.TOPRIGHT) or
				self.colorInFaceNotEqual(cube, Face.RIGHT, LocationInFace.TOPRIGHT)):
			counter+=1

		return counter

	


	def colorInFaceNotEqual(self,comparedCube,face,locationInFace):
		return getColor(face, locationInFace) != comparedCube.getColor(face, LocationInFace.BOTTOM)
	

	def countAllDifferences(self,comparedCube):
		return (countDifferenceThirdFloor(comparedCube) +
				self.countDifferenceFirstFloor(comparedCube) +
				countDifferenceSecondFloor(comparedCube))
	

	def getCopy(self):
		return Cube(this)
	



	





