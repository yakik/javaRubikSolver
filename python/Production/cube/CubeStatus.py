class CubeStatus:

	@staticmethod
	def changesOnlyInThirdFloor(Cube cube,p_comparedPermutation):

		l_counter = 0

		#next line replaced previous code
		l_counter = cube.countDifferenceThirdFloor(p_comparedPermutation)

		if l_counter > 0) return True
				else return False


            @ staticmethod
            def isDifferentItemsInFirstFloorLessThanThree(Cube cube,Cube p_comparedPermutation)

            l_counter=0

            l_counter=cube.countDifferenceFirstFloor(
        p_comparedPermutation)


            if l_counter < 3) return True
            else return False


            @ staticmethod
            def isDifferentItemsOnlyInSecondFloorLessThanThree(Cube cube,
                                                              p_comparedPermutation)

            l_counter=0

            l_counter=cube.countDifferenceSecondFloor(
                                                      p_comparedPermutation)



            if l_counter < 3) return True
            else return False


            @ staticmethod
            def isFirstFloor(Location p_location)

            return (p_location.containsFace(Face.BOTTOM))



            @ staticmethod
            def isThirdFloor(Location p_location)

            return (p_location.containsFace(Face.TOP))



            @ staticmethod
            def isSecondFloor(Location p_location)

            return (!(isFirstFloor(p_location) or isThirdFloor(p_location)))
