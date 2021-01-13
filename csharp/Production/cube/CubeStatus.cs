using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using utils;

namespace cube
{

	public class CubeStatus
	{

		public static Boolean changesOnlyInThirdFloor(Cube cube, Cube p_comparedPermutation)
		{
			int l_counter = 0;



			//next line replaced previous code
			l_counter = cube.countDifferenceThirdFloor(p_comparedPermutation);

			if (l_counter > 0) return true;
			else return false;
		}

		public static Boolean isDifferentItemsInFirstFloorLessThanThree(Cube cube,
				Cube p_comparedPermutation)
		{
			int l_counter = 0;

			l_counter = cube.countDifferenceFirstFloor(p_comparedPermutation);


			if (l_counter < 3) return true;
			else return false;
		}

		public static Boolean isDifferentItemsOnlyInSecondFloorLessThanThree(Cube cube,
				Cube p_comparedPermutation)
		{
			int l_counter = 0;

			l_counter = cube.countDifferenceSecondFloor(p_comparedPermutation);



			if (l_counter < 3) return true;
			else return false;
		}

		static public Boolean isFirstFloor(Location p_location)
		{
			return (p_location.containsFace(Face.BOTTOM));

		}

		static public Boolean isThirdFloor(Location p_location)
		{
			return (p_location.containsFace(Face.TOP));

		}

		static public Boolean isSecondFloor(Location p_location)
		{
			return (!(isFirstFloor(p_location) || isThirdFloor(p_location)));

		}

	}
}
