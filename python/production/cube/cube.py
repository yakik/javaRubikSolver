from production.utils.location_in_face_handler import Location_in_face_handler
from production.utils.face_handler import Face_handler
import copy
#import numpy as np

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
		self.colors[Face_handler.getIntFaceValue(face)][Location_in_face_handler.GetLocationInFaceInt(locationInFace)]=color

	def get_color(self, face, locationInFace):
		return self.colors[Face_handler.getIntFaceValue(face)][Location_in_face_handler.GetLocationInFaceInt(locationInFace)]


	def __init__(self,source=None):
		if source == None:
			self.colors = [["TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR","TOPCOLOR"],
							["BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR","BOTTOMCOLOR"],
							["RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR","RIGHTCOLOR"],
							["LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR","LEFTCOLOR"],
							["FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR","FRONTCOLOR"],
							["BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR","BACKCOLOR"]]
		else:
			self.colors = copy.deepcopy(source.colors)


	def rotate_face(self, face, direction):
		if face=="FRONT":
			self.rotate_front_face(direction)
			return
		if face == "RIGHT":
			self.rotate_right_face(direction)
			return
		if face == "LEFT":
			self.rotate_left_face(direction)
			return
		if face == "BACK":
			self.rotate_back_face(direction)
			return
		if face == "TOP":
			self.rotate_top_Face(direction)
			return
		if face == "BOTTOM":
			self.rotate_bottom_face(direction)
			return

		#switcher={"FRONT":self.rotateFrontFace,
		#		"RIGHT":self.rotateRightFace,
		#		"LEFT":self.rotateLeftFace,
		#		"BACK":self.rotateBackFace,
		#		"TOP":self.rotateTopFace,
		#		"BOTTOM":self.rotateBottomFace}
		#switcher.get(face)(direction)

	def rotate_bottom_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only("BOTTOM")

			self.rotate_left_to_right("BACK", "LIF_BOTTOM", "LEFT", "LIF_BOTTOM", "FRONT",
									  "LIF_BOTTOM", "RIGHT", "LIF_BOTTOM")
			self.rotate_left_to_right("BACK", "LIF_BOTTOMLEFT", "LEFT", "LIF_BOTTOMLEFT", "FRONT",
									  "LIF_BOTTOMLEFT", "RIGHT", "LIF_BOTTOMLEFT")
			self.rotate_left_to_right("BACK", "LIF_BOTTOMRIGHT", "LEFT", "LIF_BOTTOMRIGHT", "FRONT",
									  "LIF_BOTTOMRIGHT", "RIGHT", "LIF_BOTTOMRIGHT")
		else:
			self.rotate_right_to_left_face_only("BOTTOM")

			self.rotate_right_to_left("BACK", "LIF_BOTTOM", "LEFT", "LIF_BOTTOM", "FRONT",
									  "LIF_BOTTOM", "RIGHT", "LIF_BOTTOM")
			self.rotate_right_to_left("BACK", "LIF_BOTTOMLEFT", "LEFT", "LIF_BOTTOMLEFT", "FRONT",
									  "LIF_BOTTOMLEFT", "RIGHT", "LIF_BOTTOMLEFT")
			self.rotate_right_to_left("BACK", "LIF_BOTTOMRIGHT", "LEFT", "LIF_BOTTOMRIGHT", "FRONT",
									  "LIF_BOTTOMRIGHT", "RIGHT", "LIF_BOTTOMRIGHT")

	def rotate_top_Face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only("TOP")
			self.rotate_left_to_right("BACK", "LIF_TOP", "RIGHT", "LIF_TOP", "FRONT",
									  "LIF_TOP", "LEFT", "LIF_TOP")
			self.rotate_left_to_right("BACK", "LIF_TOPLEFT", "RIGHT", "LIF_TOPLEFT", "FRONT",
									  "LIF_TOPLEFT", "LEFT", "LIF_TOPLEFT")
			self.rotate_left_to_right("BACK", "LIF_TOPRIGHT", "RIGHT", "LIF_TOPRIGHT", "FRONT",
									  "LIF_TOPRIGHT", "LEFT", "LIF_TOPRIGHT")
		else:
			self.rotate_right_to_left_face_only("TOP")
			self.rotate_right_to_left("BACK", "LIF_TOP", "RIGHT", "LIF_TOP", "FRONT",
									  "LIF_TOP", "LEFT", "LIF_TOP")
			self.rotate_right_to_left("BACK", "LIF_TOPLEFT", "RIGHT", "LIF_TOPLEFT", "FRONT",
									  "LIF_TOPLEFT", "LEFT", "LIF_TOPLEFT")
			self.rotate_right_to_left("BACK", "LIF_TOPRIGHT", "RIGHT", "LIF_TOPRIGHT", "FRONT",
									  "LIF_TOPRIGHT", "LEFT", "LIF_TOPRIGHT")

	def rotate_back_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only("BACK")
			self.rotate_left_to_right("TOP", "LIF_TOP", "LEFT", "LIF_LEFT", "BOTTOM",
									  "LIF_BOTTOM", "RIGHT", "LIF_RIGHT")
			self.rotate_left_to_right("TOP", "LIF_TOPLEFT", "LEFT", "LIF_BOTTOMLEFT", "BOTTOM",
									  "LIF_BOTTOMRIGHT", "RIGHT", "LIF_TOPRIGHT")
			self.rotate_left_to_right("TOP", "LIF_TOPRIGHT", "LEFT", "LIF_TOPLEFT", "BOTTOM",
									  "LIF_BOTTOMLEFT", "RIGHT", "LIF_BOTTOMRIGHT")
		else:
			self.rotate_right_to_left_face_only("BACK")
			self.rotate_right_to_left("TOP", "LIF_TOP", "LEFT", "LIF_LEFT", "BOTTOM",
									  "LIF_BOTTOM", "RIGHT", "LIF_RIGHT")
			self.rotate_right_to_left("TOP", "LIF_TOPLEFT", "LEFT", "LIF_BOTTOMLEFT", "BOTTOM",
									  "LIF_BOTTOMRIGHT", "RIGHT", "LIF_TOPRIGHT")
			self.rotate_right_to_left("TOP", "LIF_TOPRIGHT", "LEFT", "LIF_TOPLEFT", "BOTTOM",
									  "LIF_BOTTOMLEFT", "RIGHT", "LIF_BOTTOMRIGHT")

	def rotate_left_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only("LEFT")
			self.rotate_left_to_right("TOP", "LIF_LEFT",
									  "FRONT", "LIF_LEFT",
									  "BOTTOM", "LIF_LEFT",
									  "BACK", "LIF_RIGHT")
			self.rotate_left_to_right("TOP", "LIF_BOTTOMLEFT",
									  "FRONT", "LIF_BOTTOMLEFT",
									  "BOTTOM", "LIF_BOTTOMLEFT",
									  "BACK", "LIF_TOPRIGHT")
			self.rotate_left_to_right("TOP", "LIF_TOPLEFT",
									  "FRONT", "LIF_TOPLEFT",
									  "BOTTOM", "LIF_TOPLEFT",
									  "BACK", "LIF_BOTTOMRIGHT")
		else:
			self.rotate_right_to_left_face_only("LEFT")
			self.rotate_right_to_left("TOP", "LIF_LEFT",
									  "FRONT", "LIF_LEFT",
									  "BOTTOM", "LIF_LEFT",
									  "BACK", "LIF_RIGHT")
			self.rotate_right_to_left("TOP", "LIF_BOTTOMLEFT",
									  "FRONT", "LIF_BOTTOMLEFT",
									  "BOTTOM", "LIF_BOTTOMLEFT",
									  "BACK", "LIF_TOPRIGHT")
			self.rotate_right_to_left("TOP", "LIF_TOPLEFT",
									  "FRONT", "LIF_TOPLEFT",
									  "BOTTOM", "LIF_TOPLEFT",
									  "BACK", "LIF_BOTTOMRIGHT")

	def rotate_right_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only("RIGHT")

			self.rotate_left_to_right("TOP", "LIF_RIGHT",
									  "BACK", "LIF_LEFT",
									  "BOTTOM", "LIF_RIGHT",
									  "FRONT", "LIF_RIGHT")
			self.rotate_left_to_right("TOP", "LIF_BOTTOMRIGHT",
									  "BACK", "LIF_TOPLEFT",
									  "BOTTOM", "LIF_BOTTOMRIGHT",
									  "FRONT", "LIF_BOTTOMRIGHT")
			self.rotate_left_to_right("TOP", "LIF_TOPRIGHT",
									  "BACK", "LIF_BOTTOMLEFT",
									  "BOTTOM", "LIF_TOPRIGHT",
									  "FRONT", "LIF_TOPRIGHT")
		else:
			self.rotate_right_to_left_face_only("RIGHT")

			self.rotate_right_to_left("TOP", "LIF_RIGHT",
									  "BACK", "LIF_LEFT",
									  "BOTTOM", "LIF_RIGHT",
									  "FRONT", "LIF_RIGHT")
			self.rotate_right_to_left("TOP", "LIF_BOTTOMRIGHT",
									  "BACK", "LIF_TOPLEFT",
									  "BOTTOM", "LIF_BOTTOMRIGHT",
									  "FRONT", "LIF_BOTTOMRIGHT")
			self.rotate_right_to_left("TOP", "LIF_TOPRIGHT",
									  "BACK", "LIF_BOTTOMLEFT",
									  "BOTTOM", "LIF_TOPRIGHT",
									  "FRONT", "LIF_TOPRIGHT")

	def rotate_front_face(self, direction):
		if direction == "CW":
			self.rotate_left_to_right_face_only("FRONT")
			self.rotate_left_to_right("TOP", "LIF_BOTTOM", "RIGHT", "LIF_LEFT", "BOTTOM",
									  "LIF_TOP", "LEFT", "LIF_RIGHT")
			self.rotate_left_to_right("TOP", "LIF_BOTTOMLEFT", "RIGHT", "LIF_TOPLEFT", "BOTTOM",
									  "LIF_TOPRIGHT", "LEFT", "LIF_BOTTOMRIGHT")
			self.rotate_left_to_right("TOP", "LIF_BOTTOMRIGHT", "RIGHT", "LIF_BOTTOMLEFT", "BOTTOM",
									  "LIF_TOPLEFT", "LEFT", "LIF_TOPRIGHT")
		else:
			self.rotate_right_to_left_face_only("FRONT")
			self.rotate_right_to_left("TOP", "LIF_BOTTOM", "RIGHT", "LIF_LEFT", "BOTTOM",
									  "LIF_TOP", "LEFT", "LIF_RIGHT")
			self.rotate_right_to_left("TOP", "LIF_BOTTOMLEFT", "RIGHT", "LIF_TOPLEFT", "BOTTOM",
									  "LIF_TOPRIGHT", "LEFT", "LIF_BOTTOMRIGHT")
			self.rotate_right_to_left("TOP", "LIF_BOTTOMRIGHT", "RIGHT", "LIF_BOTTOMLEFT", "BOTTOM",
									  "LIF_TOPLEFT", "LEFT", "LIF_TOPRIGHT")

	def rotate_left_to_right_face_only(self, face):
		self.rotate_left_to_right(face, "LIF_TOP", face, "LIF_RIGHT", face, "LIF_BOTTOM", face,
								  "LIF_LEFT")
		self.rotate_left_to_right(face, "LIF_BOTTOMLEFT", face, "LIF_TOPLEFT", face, "LIF_TOPRIGHT",
								  face, "LIF_BOTTOMRIGHT")

	def rotate_right_to_left_face_only(self, face):
		self.rotate_right_to_left(face, "LIF_TOP", face, "LIF_RIGHT", face, "LIF_BOTTOM", face,
								  "LIF_LEFT")
		self.rotate_right_to_left(face, "LIF_BOTTOMLEFT", face, "LIF_TOPLEFT", face, "LIF_TOPRIGHT",
								  face, "LIF_BOTTOMRIGHT")

	def print(self):
		self.printFace("TOP")
		self.printFace("BOTTOM")
		self.printFace("FRONT")
		self.printFace("BACK")
		self.printFace("LEFT")
		self.printFace("RIGHT")

	def printFace(self,face):
		print ("\n" + Face_handler.getCharValue(face) + "\n\n")
		print(self.get_color(face, "LIF_TOPLEFT") + " " +
			  self.get_color(face, "LIF_TOP") + " " + self.get_color(face, "LIF_TOPRIGHT") + "\n")
		print(self.get_color(face, "LIF_LEFT") + " " +
			  self.get_color(face, "LIF_RIGHT") + "\n")
		print(self.get_color(face, "LIF_BOTTOMLEFT") + " " +
			  self.get_color(face, "LIF_BOTTOM") + " " + self.get_color(face, "LIF_BOTTOMRIGHT") + "\n")
	
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

	def rotate_right_to_left(self, firstFace, firstLocationInFace, secondFace,
							 secondLocationInFace, thirdFace, thirdLocationInFace, fourthFace,
							 fourthLocationInFace):
		temp = self.get_color(firstFace, firstLocationInFace)
		self.set_color(firstFace, firstLocationInFace, self.get_color(secondFace, secondLocationInFace))
		self.set_color(secondFace, secondLocationInFace, self.get_color(thirdFace, thirdLocationInFace))
		self.set_color(thirdFace, thirdLocationInFace, self.get_color(fourthFace, fourthLocationInFace))
		self.set_color(fourthFace, fourthLocationInFace, temp)


	def count_difference_second_floor(self, cube):
		counter = 0
		if (self.color_in_face_not_equal(cube, "FRONT", "LIF_LEFT") or
				self.color_in_face_not_equal(cube, "LEFT", "LIF_RIGHT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "LEFT", "LIF_LEFT") or
				self.color_in_face_not_equal(cube, "BACK", "LIF_RIGHT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "BACK", "LIF_LEFT") or
				self.color_in_face_not_equal(cube, "RIGHT", "LIF_RIGHT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "RIGHT", "LIF_LEFT") or
				self.color_in_face_not_equal(cube, "FRONT", "LIF_RIGHT")):
			counter+=1
		return counter

	def count_difference_first_floor(self, cube):
		counter = 0
		if (self.color_in_face_not_equal(cube, "FRONT", "LIF_BOTTOM") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_TOP")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "LEFT", "LIF_BOTTOM") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_LEFT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "BACK", "LIF_BOTTOM") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_BOTTOM")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "RIGHT", "LIF_BOTTOM") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_RIGHT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "FRONT", "LIF_BOTTOMLEFT") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_TOPLEFT") or
				self.color_in_face_not_equal(cube, "LEFT", "LIF_BOTTOMRIGHT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "FRONT", "LIF_BOTTOMRIGHT") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_TOPRIGHT") or
				self.color_in_face_not_equal(cube, "RIGHT", "LIF_BOTTOMLEFT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "BACK", "LIF_BOTTOMRIGHT") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_BOTTOMLEFT") or
				self.color_in_face_not_equal(cube, "LEFT", "LIF_BOTTOMLEFT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "BACK", "LIF_BOTTOMLEFT") or
				self.color_in_face_not_equal(cube, "BOTTOM", "LIF_BOTTOMRIGHT") or
				self.color_in_face_not_equal(cube, "RIGHT", "LIF_BOTTOMRIGHT")):
			counter+=1
		return counter

	def count_difference_third_floor(self, cube):
		counter = 0
		if (self.color_in_face_not_equal(cube, "FRONT", "LIF_TOP") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_BOTTOM")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "LEFT", "LIF_TOP") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_LEFT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "BACK", "LIF_TOP") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_TOP")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "RIGHT", "LIF_TOP") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_RIGHT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "FRONT", "LIF_TOPLEFT") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_BOTTOMLEFT") or
				self.color_in_face_not_equal(cube, "LEFT", "LIF_TOPRIGHT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "FRONT", "LIF_TOPRIGHT") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_BOTTOMRIGHT") or
				self.color_in_face_not_equal(cube, "RIGHT", "LIF_TOPLEFT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "BACK", "LIF_TOPRIGHT") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_TOPLEFT") or
				self.color_in_face_not_equal(cube, "LEFT", "LIF_TOPLEFT")):
			counter+=1
		if (self.color_in_face_not_equal(cube, "BACK", "LIF_TOPLEFT") or
				self.color_in_face_not_equal(cube, "TOP", "LIF_TOPRIGHT") or
				self.color_in_face_not_equal(cube, "RIGHT", "LIF_TOPRIGHT")):
			counter+=1
		return counter

	def color_in_face_not_equal(self, comparedCube, face, locationInFace):
		return self.get_color(face, locationInFace) != comparedCube.get_color(face, "LIF_BOTTOM")

	def count_all_differences(self, comparedCube):
		return (self.count_difference_third_floor(comparedCube) +
				self.count_difference_first_floor(comparedCube) +
				self.count_difference_second_floor(comparedCube))
	

	def get_copy(self):
		return Cube(self)
	


