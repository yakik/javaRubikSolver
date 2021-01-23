from production.utils.face import Face
from production.utils.direction import Direction
from production.utils.rotation import Rotation
from production.cube.cubeStatus import CubeStatus
from production.cube.rubikFileWriter import RubikFileWriter
from production.solver.rotationSequence import RotationSequence
from production.cube.cube import Cube

class GoodRotationsBuilder:

		@staticmethod
		def findGoodRotationLinks(self,p_firstFloorFile
				,p_secondFloorFile,p_thirdFloorFile, p_levels):
			l_firstWriter = RubikFileWriter(p_firstFloorFile)
			l_secondWriter = RubikFileWriter(p_secondFloorFile)
			l_thirdWriter = RubikFileWriter(p_thirdFloorFile)
			l_rubik = Cube()
			l_initialPermutation = Cube(l_rubik)
			l_rotationLinkedList = RotationSequence()
			GoodRotationsBuilder.BuildFilesForRotation(l_firstWriter, l_secondWriter, l_thirdWriter
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
					if p_rotationLinkedList.isRedundant(newRotation):
						continue
					p_rotationLinkedList.addRotation(newRotation)
					p_rubik.rotateFace(newRotation.getFace(), newRotation.getDirection())
					if CubeStatus.isDifferentItemsInFirstFloorLessThanThree(p_rubik, p_initialPermutation):
						p_rotationLinkedList.writeToFile(p_firstFloorFile)
					if CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(p_rubik, p_initialPermutation):
						p_rotationLinkedList.writeToFile((p_secondFloorFile))
					if CubeStatus.changesOnlyInThirdFloor(p_rubik, p_initialPermutation):
						p_rotationLinkedList.writeToFile(p_thirdFloorFile)

					GoodRotationsBuilder.BuildFilesForRotation(p_firstFloorFile, p_secondFloorFile, p_thirdFloorFile,
							p_rubik, p_initialPermutation, p_rotationLinkedList, p_level - 1, myProgressString)
					p_rotationLinkedList.removeRotation()
					p_rubik.rotateFace(newRotation.getReverse().getFace(), newRotation.getReverse().getDirection())
				
	

	

