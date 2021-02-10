
  

from production.utils.face import Face
from production.utils.location_in_face import Location_in_face
from production.utils.face_handler import Face_handler

class Cube:

	@staticmethod
	def get_permutation_from_cube(cube):
		return cube.get_copy()

	@staticmethod
	def get_value(l_permutation, p_highestFloor):
		l_value = 0
		fixedCube = Cube()
		l_value = 2 * (8 - l_permutation.count_difference_first_floor(fixedCube))
		if p_highestFloor > 1:
			l_value += 2 * (4 - l_permutation.count_difference_second_floor(fixedCube))
		if p_highestFloor > 2:
			l_value += 2 * (8 - l_permutation.count_difference_third_floor(fixedCube))
		return l_value

	def equals(self,comparedCube):
		if (self.count_difference_first_floor(comparedCube) +
			self.count_difference_second_floor(comparedCube) +
			self.count_difference_third_floor(comparedCube)) == 0:
			return True
		else:
			return False

	
	
	def set_color(self, face, locationInFace, color):
		self.colors[face.value][locationInFace.value]=color

	def get_color(self, face, locationInFace):
		return self.colors[face.value][locationInFace.value]


	def __init__(self,source=None):
		self.colors = [["TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR"],
						["BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR"],
						["RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR"],
						["LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR"],
						["FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR"],
						["BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR"]]



		#	[[0 for x in range(8)] for y in range(6)]
		#for face in list(Face):
		#	for locationInFace in list(Location_in_face):
		#		self.colors[face.value][locationInFace.value]=Cube.getColorForFaceForSortedCube(face)

		if source!=None:
			for locationInFace in list(Location_in_face):
				self.set_color(Face.FRONT, locationInFace, source.get_color(Face.FRONT, locationInFace))
				self.set_color(Face.BACK, locationInFace, source.get_color(Face.BACK, locationInFace))
				self.set_color(Face.RIGHT, locationInFace, source.get_color(Face.RIGHT, locationInFace))
				self.set_color(Face.LEFT, locationInFace, source.get_color(Face.LEFT, locationInFace))
				self.set_color(Face.TOP, locationInFace, source.get_color(Face.TOP, locationInFace))
				self.set_color(Face.BOTTOM, locationInFace, source.get_color(Face.BOTTOM, locationInFace))

	def rotate_face(self, face, direction):
		if face==Face.FRONT:
			self.rotate_front_face(direction)
			return
		if face == Face.RIGHT:
			self.rotate_right_face(direction)
			return
		if face == Face.LEFT:
			self.rotate_left_face(direction)
			return
		if face == Face.BACK:
			self.rotate_back_face(direction)
			return
		if face == Face.TOP:
			self.rotate_top_Face(direction)
			return
		if face == Face.BOTTOM:
			self.rotate_bottom_face(direction)
			return

		#switcher={Face.FRONT:self.rotateFrontFace,
		#		Face.RIGHT:self.rotateRightFace,
		#		Face.LEFT:self.rotateLeftFace,
		#		Face.BACK:self.rotateBackFace,
		#		Face.TOP:self.rotateTopFace,
		#		Face.BOTTOM:self.rotateBottomFace}
		#switcher.get(face)(direction)

	def rotate_bottom_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only(Face.BOTTOM)

			self.rotate_left_to_right(Face.BACK, Location_in_face.BOTTOM, Face.LEFT, Location_in_face.BOTTOM, Face.FRONT,
									  Location_in_face.BOTTOM, Face.RIGHT, Location_in_face.BOTTOM)
			self.rotate_left_to_right(Face.BACK, Location_in_face.BOTTOMLEFT, Face.LEFT, Location_in_face.BOTTOMLEFT, Face.FRONT,
									  Location_in_face.BOTTOMLEFT, Face.RIGHT, Location_in_face.BOTTOMLEFT)
			self.rotate_left_to_right(Face.BACK, Location_in_face.BOTTOMRIGHT, Face.LEFT, Location_in_face.BOTTOMRIGHT, Face.FRONT,
									  Location_in_face.BOTTOMRIGHT, Face.RIGHT, Location_in_face.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotate_bottom_face("CW")

	def rotate_top_Face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only(Face.TOP)
			self.rotate_left_to_right(Face.BACK, Location_in_face.TOP, Face.RIGHT, Location_in_face.TOP, Face.FRONT,
									  Location_in_face.TOP, Face.LEFT, Location_in_face.TOP)
			self.rotate_left_to_right(Face.BACK, Location_in_face.TOPLEFT, Face.RIGHT, Location_in_face.TOPLEFT, Face.FRONT,
									  Location_in_face.TOPLEFT, Face.LEFT, Location_in_face.TOPLEFT)
			self.rotate_left_to_right(Face.BACK, Location_in_face.TOPRIGHT, Face.RIGHT, Location_in_face.TOPRIGHT, Face.FRONT,
									  Location_in_face.TOPRIGHT, Face.LEFT, Location_in_face.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotate_top_Face("CW")

	def rotate_back_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only(Face.BACK)
			self.rotate_left_to_right(Face.TOP, Location_in_face.TOP, Face.LEFT, Location_in_face.LEFT, Face.BOTTOM,
									  Location_in_face.BOTTOM, Face.RIGHT, Location_in_face.RIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.TOPLEFT, Face.LEFT, Location_in_face.BOTTOMLEFT, Face.BOTTOM,
									  Location_in_face.BOTTOMRIGHT, Face.RIGHT, Location_in_face.TOPRIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.TOPRIGHT, Face.LEFT, Location_in_face.TOPLEFT, Face.BOTTOM,
									  Location_in_face.BOTTOMLEFT, Face.RIGHT, Location_in_face.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotate_back_face("CW")

	def rotate_left_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only(Face.LEFT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.LEFT,
									  Face.FRONT, Location_in_face.LEFT,
									  Face.BOTTOM, Location_in_face.LEFT,
									  Face.BACK, Location_in_face.RIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.BOTTOMLEFT,
									  Face.FRONT, Location_in_face.BOTTOMLEFT,
									  Face.BOTTOM, Location_in_face.BOTTOMLEFT,
									  Face.BACK, Location_in_face.TOPRIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.TOPLEFT,
									  Face.FRONT, Location_in_face.TOPLEFT,
									  Face.BOTTOM, Location_in_face.TOPLEFT,
									  Face.BACK, Location_in_face.BOTTOMRIGHT)
		else:
			for _ in range(0,3):
				self.rotate_left_face("CW")

	def rotate_right_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only(Face.RIGHT)

			self.rotate_left_to_right(Face.TOP, Location_in_face.RIGHT,
									  Face.BACK, Location_in_face.LEFT,
									  Face.BOTTOM, Location_in_face.RIGHT,
									  Face.FRONT, Location_in_face.RIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.BOTTOMRIGHT,
									  Face.BACK, Location_in_face.TOPLEFT,
									  Face.BOTTOM, Location_in_face.BOTTOMRIGHT,
									  Face.FRONT, Location_in_face.BOTTOMRIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.TOPRIGHT,
									  Face.BACK, Location_in_face.BOTTOMLEFT,
									  Face.BOTTOM, Location_in_face.TOPRIGHT,
									  Face.FRONT, Location_in_face.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotate_right_face("CW")

	def rotate_front_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only(Face.FRONT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.BOTTOM, Face.RIGHT, Location_in_face.LEFT, Face.BOTTOM,
									  Location_in_face.TOP, Face.LEFT, Location_in_face.RIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.BOTTOMLEFT, Face.RIGHT, Location_in_face.TOPLEFT, Face.BOTTOM,
									  Location_in_face.TOPRIGHT, Face.LEFT, Location_in_face.BOTTOMRIGHT)
			self.rotate_left_to_right(Face.TOP, Location_in_face.BOTTOMRIGHT, Face.RIGHT, Location_in_face.BOTTOMLEFT, Face.BOTTOM,
									  Location_in_face.TOPLEFT, Face.LEFT, Location_in_face.TOPRIGHT)
		else:
			for _ in range(0,3):
				self.rotate_front_face("CW")

	def rotate_left_to_right_face_only(self, face):
		self.rotate_left_to_right(face, Location_in_face.TOP, face, Location_in_face.RIGHT, face, Location_in_face.BOTTOM, face,
								  Location_in_face.LEFT)
		self.rotate_left_to_right(face, Location_in_face.BOTTOMLEFT, face, Location_in_face.TOPLEFT, face, Location_in_face.TOPRIGHT,
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
		print(self.get_color(face, Location_in_face.TOPLEFT) + " " +
			  self.get_color(face, Location_in_face.TOP) + " " + self.get_color(face, Location_in_face.TOPRIGHT) + "\n")
		print(self.get_color(face, Location_in_face.LEFT) + " " +
			  self.get_color(face, Location_in_face.RIGHT) + "\n")
		print(self.get_color(face, Location_in_face.BOTTOMLEFT) + " " +
			  self.get_color(face, Location_in_face.BOTTOM) + " " + self.get_color(face, Location_in_face.BOTTOMRIGHT) + "\n")
	
	#                TL T TR
	#                L TOP R 
	#                BL B BR

	#TL T TR TL T TR TL T TR TL T TR
	#LBACK R LLEFT R LFRONTR LRIGHTR 
	#BL B BR BL B BR BL B BR BL B BR

	#                TL T TR
	#                LBOTTOMR 
	#                BL B BR

	def rotate_left_to_right(self, firstFace, firstLocationInFace, secondFace,
							 secondLocationInFace, thirdFace, thirdLocationInFace, fourthFace,
							 fourthLocationInFace):
		temp = self.get_color(fourthFace, fourthLocationInFace)
		self.set_color(fourthFace, fourthLocationInFace, self.get_color(thirdFace, thirdLocationInFace))
		self.set_color(thirdFace, thirdLocationInFace, self.get_color(secondFace, secondLocationInFace))
		self.set_color(secondFace, secondLocationInFace, self.get_color(firstFace, firstLocationInFace))
		self.set_color(firstFace, firstLocationInFace, temp)

	def count_difference_second_floor(self, cube):
		counter = 0
		if (self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.LEFT) or
				self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.RIGHT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.LEFT) or
				self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.RIGHT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.LEFT) or
				self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.RIGHT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.LEFT) or
				self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.RIGHT)):
			counter+=1
		return counter

	def count_difference_first_floor(self, cube):
		counter = 0
		if (self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.BOTTOM) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.TOP)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.BOTTOM) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.LEFT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.BOTTOM) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.BOTTOM)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.BOTTOM) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.RIGHT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.BOTTOMLEFT) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.TOPLEFT) or
				self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.BOTTOMRIGHT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.BOTTOMRIGHT) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.TOPRIGHT) or
				self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.BOTTOMLEFT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.BOTTOMRIGHT) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.BOTTOMLEFT) or
				self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.BOTTOMLEFT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.BOTTOMLEFT) or
				self.color_in_face_not_equal(cube, Face.BOTTOM, Location_in_face.BOTTOMRIGHT) or
				self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.BOTTOMRIGHT)):
			counter+=1
		return counter

	def count_difference_third_floor(self, cube):
		counter = 0
		if (self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.TOP) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.BOTTOM)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.TOP) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.LEFT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.TOP) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.TOP)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.TOP) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.RIGHT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.TOPLEFT) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.BOTTOMLEFT) or
				self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.TOPRIGHT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.FRONT, Location_in_face.TOPRIGHT) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.BOTTOMRIGHT) or
				self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.TOPLEFT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.TOPRIGHT) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.TOPLEFT) or
				self.color_in_face_not_equal(cube, Face.LEFT, Location_in_face.TOPLEFT)):
			counter+=1
		if (self.color_in_face_not_equal(cube, Face.BACK, Location_in_face.TOPLEFT) or
				self.color_in_face_not_equal(cube, Face.TOP, Location_in_face.TOPRIGHT) or
				self.color_in_face_not_equal(cube, Face.RIGHT, Location_in_face.TOPRIGHT)):
			counter+=1
		return counter

	def color_in_face_not_equal(self, comparedCube, face, locationInFace):
		return self.get_color(face, locationInFace) != comparedCube.get_color(face, Location_in_face.BOTTOM)

	def count_all_differences(self, comparedCube):
		return (self.count_difference_third_floor(comparedCube) +
				self.count_difference_first_floor(comparedCube) +
				self.count_difference_second_floor(comparedCube))
	

	def get_copy(self):
		return Cube(self)
	


