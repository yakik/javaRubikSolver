from production.utils.face import Face
from production.utils.rotation import Rotation
from production.cube.cubeStatus import CubeStatus
from production.cube.rubik_file_writer import Rubik_file_writer
from production.solver.rotation_sequence import Rotation_sequence
from production.cube.cube import Cube

class Good_rotations_builder:

		@staticmethod
		def findGoodRotationLinks(self,p_firstFloorFile
				,p_secondFloorFile,p_thirdFloorFile, p_levels):
			l_firstWriter = Rubik_file_writer(p_firstFloorFile)
			l_secondWriter = Rubik_file_writer(p_secondFloorFile)
			l_thirdWriter = Rubik_file_writer(p_thirdFloorFile)
			l_rubik = Cube()
			l_initialPermutation = Cube(l_rubik)
			l_rotationLinkedList = Rotation_sequence()
			Good_rotations_builder.BuildFilesForRotation(l_firstWriter, l_secondWriter, l_thirdWriter
														 , l_rubik, l_initialPermutation, l_rotationLinkedList, p_levels, "")
			l_firstWriter.close()
			l_secondWriter.close()
			l_thirdWriter.close()

		@staticmethod
		def BuildFilesForRotation(p_firstFloorFile, p_secondFloorFile, p_thirdFloorFile,p_rubik
				,p_initialPermutation,p_rotationLinkedList, p_level,p_progressString):

			if p_level == 0:
				 return
			if p_level > 5:
				 print(p_progressString)
			i = 0
			for face in Face:
				for direction in Direction:
					i+=1
					myProgressString = p_progressString + i
					newRotation = Rotation(face, direction)
					if p_rotationLinkedList.is_redundant(newRotation):
						continue
					p_rotationLinkedList.add_rotation(newRotation)
					p_rubik.rotate_face(newRotation.getFace(), newRotation.getDirection())
					if CubeStatus.isDifferentItemsInFirstFloorLessThanThree(p_rubik, p_initialPermutation):
						p_rotationLinkedList.write_to_file(p_firstFloorFile)
					if CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(p_rubik, p_initialPermutation):
						p_rotationLinkedList.write_to_file((p_secondFloorFile))
					if CubeStatus.changesOnlyInThirdFloor(p_rubik, p_initialPermutation):
						p_rotationLinkedList.write_to_file(p_thirdFloorFile)

					Good_rotations_builder.BuildFilesForRotation(p_firstFloorFile, p_secondFloorFile, p_thirdFloorFile,
																 p_rubik, p_initialPermutation, p_rotationLinkedList, p_level - 1, myProgressString)
					p_rotationLinkedList.remove_rotation()
					p_rubik.rotate_face(newRotation.getReverse().getFace(), newRotation.getReverse().getDirection())
				
	

	

