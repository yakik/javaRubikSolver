/***************************************************************************
                          main.cpp  -  description
                             -------------------
    begin                : Tue Apr 10 2001
    copyright            : (C) 2001 by yaki koren
    email                : 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
  #include "Rubik.h"
  #include "Guesser.h"
  #include "RotationTree.h"
  #include "Solver.h"

/*  void testCube()
  {
  	Cube l_cube;
  	int l_inputFace;
  	Direction l_inputDirection;
  	while (1)
  	{
  	printf("\nenter Face and Direction (Clockwise/counterclockWise)\n");
  	l_inputFace = getCharFace(getchar());
  	l_inputDirection = getCharDirection(getchar());
  	getchar();
  	l_cube.rotate(l_inputFace, l_inputDirection);
  	printf("front cube = %c\n",getFaceChar(l_cube.getFace(F)));
  	}
  }*/


	void testRubik()
  {
  	Solver l_solver;
  	Rubik l_cube;
    char l_inputChar;
  	int l_inputFace;
  	int l_inputDirection;
  	Permutation *l_permutation;
  	l_cube.printCube();
  	while (1)
  	{
  	printf("\nenter [Face and Direction] or [LD - load] or [MD - shuffle] or [SL - solve]\n");
   	l_inputFace = getCharFace(l_inputChar = getchar());
  	l_inputDirection = getCharDirection(getchar());
  	getchar();
		if (l_inputChar == 'M') 	
 	{int i;
 	for (i=0;i<40;i++)
 	{
 	l_cube.rotateFace(Rotation(F,CW));
 	l_cube.rotateFace(Rotation(U,CW));
 	l_cube.rotateFace(Rotation(R,CW));
 	l_cube.rotateFace(Rotation(D,CW));
	l_cube.rotateFace(Rotation(L,CW));
 	l_cube.rotateFace(Rotation(B,CW));
 	l_cube.rotateFace(Rotation(L,CW));
 	l_cube.rotateFace(Rotation(D,CW));
 	l_cube.rotateFace(Rotation(R,CW));
 	l_cube.rotateFace(Rotation(D,CW));
	l_cube.rotateFace(Rotation(F,CW));
 	l_cube.rotateFace(Rotation(B,CW));

 	}
 	}
	if (l_inputChar == 'S') 	
 	 l_solver.solve(&l_cube);
  	else if (l_inputChar == 'Z')
  		l_cube.reset();
  		 	else if (l_inputChar == 'L')
  		 	{
   				FILE *l_file= fopen("myUnfinbishedCube.txt","r");
   				Permutation *l_perm = new Permutation();
   				l_perm->load(l_file);
  				fclose(l_file);  		 	
			    l_cube.set(l_perm);
			    l_cube.printCube();
  		 	}

  	else
  		if (l_inputChar == 'P')
  		{
  			l_permutation = l_cube.getPermutation();
  			l_permutation->print();
//  			delete l_permutation;	
  		}
  		else
  			if (l_inputChar== 'Q')
  			{
  				l_cube.set(l_permutation);
  				l_cube.printCube();
  			}
  			else
	 				{
	 					l_cube.rotateFace(Rotation(l_inputFace, l_inputDirection));
	 					l_cube.printCube();
	 				}
  	}
  }

/*  void testGuesser()
  {
  	Rubik l_rubik;
  	Guesser l_guesser;
  	Permutation l_permutation;
  	Process l_Process;
  	int l_counter;
  	
  	l_counter = l_guesser.depthFirstSearch(&l_permutation, &l_rubik, 5, &l_Process);
  	printf("%d\n",l_counter);
  }	

   void testGuesser2()
  {
  	Rubik l_rubik;
  	Guesser l_guesser;
  	Permutation l_permutation(&l_rubik);
  	Process l_Process;

  	
  	l_guesser.Search2(&l_permutation, &l_rubik, 8, &l_Process);
  	
  }	       */



/*void testSolve()
{
   	Rubik *l_cube = new Rubik();
   	Solver l_solver;
   	FILE *l_file;
   	l_file= fopen("myUnfinbishedCube2.txt","r");
   	Permutation *l_perm = new Permutation();
   	l_perm->load(l_file);
  	fclose(l_file);
    l_cube->set(l_perm);
    l_cube->printCube();
    getchar();
    l_solver.solve(l_cube);

} */

  int main()       	
  {
    testRubik();
   	//testSolve();

    return 1;
  }

