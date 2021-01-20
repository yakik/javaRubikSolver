class GoodRotationsBuilder :

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
		def BuildFilesForRotation(self, RubikFileWriter p_firstFloorFile, RubikFileWriter p_secondFloorFile, RubikFileWriter p_thirdFloorFile
												 ,p_rubik
				,p_initialPermutation,p_rotationLinkedList, p_level,p_progressString):

			if p_level == 0:
				 return
			if p_level > 5:
				 Console.WriteLine(p_progressString)
			i = 0
			
				for face in Enum.GetValues(typeof(Face)):
				for direction in Enum.GetValues(typeof(Direction)):
					i+=1
					String myProgressString = p_progressString + String.Format(".%d", i)
					Rotation newRotation = Rotation(face, direction)
					if p_rotationLinkedList.isRedundant(newRotation))
						continue
					p_rotationLinkedList.addRotation(newRotation)
					p_rubik.rotateFace(newRotation.getFace(), newRotation.getDirection())
					if CubeStatus.isDifferentItemsInFirstFloorLessThanThree(p_rubik, p_initialPermutation))
						p_rotationLinkedList.writeToFile(p_firstFloorFile)
					if CubeStatus.isDifferentItemsOnlyInSecondFloorLessThanThree(p_rubik, p_initialPermutation))
						p_rotationLinkedList.writeToFile((p_secondFloorFile))
					if CubeStatus.changesOnlyInThirdFloor(p_rubik, p_initialPermutation))
						p_rotationLinkedList.writeToFile(p_thirdFloorFile)

					BuildFilesForRotation(p_firstFloorFile, p_secondFloorFile, p_thirdFloorFile,
						   p_rubik, p_initialPermutation, p_rotationLinkedList, p_level - 1, myProgressString)
					p_rotationLinkedList.removeRotation()
					p_rubik.rotateFace(newRotation.getReverse().getFace(), newRotation.getReverse().getDirection())
				
		

	

