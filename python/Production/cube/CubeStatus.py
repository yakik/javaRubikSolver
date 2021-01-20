class CubeStatus:

	@staticmethod
	def changesOnlyInThirdFloor(cube,p_comparedPermutation):

		l_counter = 0

		#next line replaced previous code
		l_counter = cube.countDifferenceThirdFloor(p_comparedPermutation)

		if l_counter > 0):
			 return True
				else:
					 return False


            @ staticmethod
            def isDifferentItemsInFirstFloorLessThanThree(cube,p_comparedPermutation)

            l_counter=0

            l_counter=cube.countDifferenceFirstFloor(
        p_comparedPermutation)


            if l_counter < 3):
				 return True
            else:
				 return False


            @ staticmethod
            def isDifferentItemsOnlyInSecondFloorLessThanThree(cube,
                                                              p_comparedPermutation)

            l_counter=0

            l_counter=cube.countDifferenceSecondFloor( p_comparedPermutation)



            if l_counter < 3):
				 return True
            else:
				 return False


            @ staticmethod
            def isFirstFloor(p_location)

            return (p_location.containsFace(Face.BOTTOM))



            @ staticmethod
            def isThirdFloor(p_location)

            return (p_location.containsFace(Face.TOP))



            @ staticmethod
            def isSecondFloor(p_location)

            return (!(isFirstFloor(p_location) or isThirdFloor(p_location)))
