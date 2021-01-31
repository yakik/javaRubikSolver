
/***************************************************************************
                          cube.cpp  -  description
                             -------------------
    begin                : Mon Apr 9 2001
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

Rubik::Rubik()
{
	int i;
	int j;
	int k;
//	Cube();
// initializing
  for (i=0;i<6;i++)
  	for (j=0;j<6;j++)
	  	for (k=0;k<6;k++)
		  	c_cornerCubicles[i][j][k] = NULL;
  for (i=0;i<6;i++)
  	for (j=0;j<6;j++)
	  	c_edgeCubicles[i][j] = NULL;

	resetData();
	buildCubiclesPerFace();


}

Rubik::~Rubik()
{
	int i;
	int j;
	int k;
//	Cube();
// initializing
  for (i=0;i<6;i++)
  	for (j=0;j<6;j++)
	  	for (k=0;k<6;k++)
		  	if (c_cornerCubicles[i][j][k] != NULL)
		  		delete  c_cornerCubicles[i][j][k];
  for (i=0;i<6;i++)
  	for (j=0;j<6;j++)
  		if (c_edgeCubicles[i][j] != NULL)
  			delete  c_edgeCubicles[i][j];


}

void Rubik::buildCubiclesPerFace()
{
	int i,j;
//build  edgeCubiclePerFace
  for (i=0;i<6;i++)
  	for (j=0;j<4;++j)
  		c_edgeCubiclePerFace[i][j] = getCubicle(Location(i,g_faceOrder[i][j]));
//build  cornerCubiclePerFace
  for (i=0;i<6;i++)
  	for (j=0;j<4;j++)
  		c_cornerCubiclePerFace[i][j] = getCubicle(Location(i,g_faceOrder[i][j],g_faceOrder[i][(j+1+4)%4]));
}

void Rubik::reset()
{

	int i;
	int j;
	int k;

	 for (i=0;i<6;i++)
  	for (j=0;j<6;j++)
	  	for (k=0;k<6;k++)
		  {
		  	Location l_location = Location(i,j,k);
		  	if (c_cornerCubicles[l_location.getFace0()][l_location.getFace1()][l_location.getFace2()]!=NULL)
		  	{
		  		delete c_cornerCubicles[l_location.getFace0()][l_location.getFace1()][l_location.getFace2()];
					c_cornerCubicles[l_location.getFace0()][l_location.getFace1()][l_location.getFace2()] = NULL;		  		
        }
       }

  for (i=0;i<6;i++)
  	for (j=0;j<6;j++)
		  {
		  	Location l_location = Location(i,j);
		  	if (c_edgeCubicles[l_location.getFace0()][l_location.getFace1()]!=NULL)
		  	{
		  		delete c_edgeCubicles[l_location.getFace0()][l_location.getFace1()];
					c_edgeCubicles[l_location.getFace0()][l_location.getFace1()] = NULL;		  		
        }
       }
	
	resetData();
	buildCubiclesPerFace();
}

void Rubik::resetData()
{
	int i;
	int j;

// build 		c_edgeCubicles[Face][Face];
  for (i=0;i<6;i++)
  {
  	c_edgeCubicles[i][i] = new Cubicle(Location(i,i));
  	for (j=0;j<4;j++)
  	{
	  	Location l_edgeLocation(i,g_faceOrder[i][j]);
  		if (c_edgeCubicles[l_edgeLocation.getFace0()][l_edgeLocation.getFace1()]==NULL)
  			c_edgeCubicles[l_edgeLocation.getFace0()][l_edgeLocation.getFace1()] = new Cubicle(l_edgeLocation);
  	}
  }

// build 		c_cornerCubicles[Face][Face];
  for (i=0;i<6;i++)
  	for (j=0;j<4;j++)
  	{
			Location l_cornerLocation(i,g_faceOrder[i][j],g_faceOrder[i][((j+1+4)%4)]);
			if (c_cornerCubicles[l_cornerLocation.getFace0()]
			                    [l_cornerLocation.getFace1()]
			                    [l_cornerLocation.getFace2()]==NULL)
			   c_cornerCubicles[l_cornerLocation.getFace0()]
			                    [l_cornerLocation.getFace1()]
			                    [l_cornerLocation.getFace2()]= new Cubicle(l_cornerLocation);
			l_cornerLocation = Location(i,g_faceOrder[i][j],g_faceOrder[i][((j-1+4)%4)]);
			if (c_cornerCubicles[l_cornerLocation.getFace0()]
			                    [l_cornerLocation.getFace1()]
			                    [l_cornerLocation.getFace2()]==NULL)
			   c_cornerCubicles[l_cornerLocation.getFace0()]
			                    [l_cornerLocation.getFace1()]
			                    [l_cornerLocation.getFace2()]= new Cubicle(l_cornerLocation);
		}

}

Cubicle *Rubik::getCubicle(Location p_location)
{
	if (p_location.isEdge())
	{
		if (c_edgeCubicles[p_location.getFace0()][p_location.getFace1()]==NULL)
			printf("null request:%c,%c\n",getFaceChar(p_location.getFace0()), getFaceChar(p_location.getFace1()));
		return c_edgeCubicles[p_location.getFace0()][p_location.getFace1()];
	}
	else
	{
		if (c_cornerCubicles[p_location.getFace0()][p_location.getFace1()][p_location.getFace2()]==NULL)
			printf("null request:%c,%c,%c\n",getFaceChar(p_location.getFace0()), getFaceChar(p_location.getFace1()), getFaceChar(p_location.getFace2()));
		return c_cornerCubicles[p_location.getFace0()][p_location.getFace1()][p_location.getFace2()];
	}
}


void Rubik::rotateFace(Rotation p_rotation)
{
  int i;
	Cubie *l_tmpCubic;
	int l_face = p_rotation.getFace();
	int l_direction = p_rotation.getDirection();
//rotate
	if (l_direction == CW)
//edges
	{
		l_tmpCubic = c_edgeCubiclePerFace[l_face][3]->getCurrentCubie();
		c_edgeCubiclePerFace[l_face][3]->	setCurrentCubie(c_edgeCubiclePerFace[l_face][2]->getCurrentCubie());
		c_edgeCubiclePerFace[l_face][2]->	setCurrentCubie(c_edgeCubiclePerFace[l_face][1]->getCurrentCubie());
		c_edgeCubiclePerFace[l_face][1]->	setCurrentCubie(c_edgeCubiclePerFace[l_face][0]->getCurrentCubie());
		c_edgeCubiclePerFace[l_face][0]->	setCurrentCubie(l_tmpCubic);
//corners
		l_tmpCubic = c_cornerCubiclePerFace[l_face][3]->getCurrentCubie();
		c_cornerCubiclePerFace[l_face][3]->	setCurrentCubie(c_cornerCubiclePerFace[l_face][2]->getCurrentCubie());
		c_cornerCubiclePerFace[l_face][2]->	setCurrentCubie(c_cornerCubiclePerFace[l_face][1]->getCurrentCubie());
		c_cornerCubiclePerFace[l_face][1]->	setCurrentCubie(c_cornerCubiclePerFace[l_face][0]->getCurrentCubie());
		c_cornerCubiclePerFace[l_face][0]->	setCurrentCubie(l_tmpCubic);
	}
  else
//edges
	{
		l_tmpCubic = c_edgeCubiclePerFace[l_face][0]->getCurrentCubie();
		c_edgeCubiclePerFace[l_face][0]->	setCurrentCubie(c_edgeCubiclePerFace[l_face][1]->getCurrentCubie());
		c_edgeCubiclePerFace[l_face][1]->	setCurrentCubie(c_edgeCubiclePerFace[l_face][2]->getCurrentCubie());
		c_edgeCubiclePerFace[l_face][2]->	setCurrentCubie(c_edgeCubiclePerFace[l_face][3]->getCurrentCubie());
		c_edgeCubiclePerFace[l_face][3]->	setCurrentCubie(l_tmpCubic);
//corners
		l_tmpCubic = c_cornerCubiclePerFace[l_face][0]->getCurrentCubie();
		c_cornerCubiclePerFace[l_face][0]->	setCurrentCubie(c_cornerCubiclePerFace[l_face][1]->getCurrentCubie());
		c_cornerCubiclePerFace[l_face][1]->	setCurrentCubie(c_cornerCubiclePerFace[l_face][2]->getCurrentCubie());
		c_cornerCubiclePerFace[l_face][2]->	setCurrentCubie(c_cornerCubiclePerFace[l_face][3]->getCurrentCubie());
		c_cornerCubiclePerFace[l_face][3]->	setCurrentCubie(l_tmpCubic);
	}
//rotate cubicles
//edges
	for (i=0;i<4;i++)
		c_edgeCubiclePerFace[l_face][i]->	getCurrentCubie()->rotate(p_rotation);
//corners
	for (i=0;i<4;i++)
		c_cornerCubiclePerFace[l_face][i]->	getCurrentCubie()->rotate(p_rotation);

}

int Rubik::set(Permutation *p_permutation)
{
	int i, l_returnValue;
	if (p_permutation->getCubicleCount()!=20)
		 l_returnValue = 0;
	else
	{
		for (i=0;i<20;i++)
		{
			CubicleData l_cubicleData = p_permutation->getCubicleData(i);
			Cubicle *l_cubicle = getCubicle(l_cubicleData.getLocation());
			Cubie *l_cubie = l_cubicle->getHomeCubie();
			getCubicle(l_cubicleData.getCubieLocation())->setCurrentCubie(l_cubie);
			l_cubie->setPosition(l_cubicleData.getCubiePosition());
		}
		l_returnValue = 1;
	}
	return l_returnValue;
}

Permutation *Rubik::getPermutation()
{
 	Location l_rubikLocation[20]={Location(F,U),
 	                              Location(F,R),
 	                              Location(F,L),
 	                              Location(F,D),
 	                              Location(B,U),
 	                              Location(B,R),
 	                              Location(B,L),
 	                              Location(B,D),
 	                              Location(U,R),
 	                              Location(U,L),
 	                              Location(D,R),
 	                              Location(D,L),
 	                              Location(F,U,R),
 	                              Location(F,U,L),
 	                              Location(F,D,R),
 	                              Location(F,D,L),
 	                              Location(B,U,R),
 	                              Location(B,U,L),
 	                              Location(B,D,R),
 	                              Location(B,D,L)};
 	int i;
 	Permutation *l_permutation = new Permutation;
 	for (i=0;i<20;i++)
 	 	l_permutation->addCubicleData(CubicleData(l_rubikLocation[i],
 														 	 		getCubicleCubieLocation(l_rubikLocation[i]),
 														 	 		getCubicleCubiePosition(l_rubikLocation[i])));
 	return l_permutation;
}

Location Rubik::getCubicleCubieLocation(Location p_cubicleLocation)
{
	return getCubicle(p_cubicleLocation)->getHomeCubie()->getCurrentCubicle()->
						getLocation();
}

Position Rubik::getCubicleCubiePosition(Location p_cubicleLocation)
{
	return getCubicle(p_cubicleLocation)->getHomeCubie()->getPosition();
}

char 		Rubik::getCubeFacelet(Location p_location, int p_face)
{
	return getFaceChar(getCubicle(p_location)->
					getCurrentCubie()->getFace(p_face));
}


void Rubik::printCube()
{
printf ("         %c %c %c\n",getCubeFacelet(Location(U,B,L),U),getCubeFacelet(Location(U,B),U),getCubeFacelet(Location(U,B,R),U));
printf ("         %c %c %c\n",getCubeFacelet(Location(U,L),U),getCubeFacelet(Location(U,U),U),getCubeFacelet(Location(U,R),U));
printf ("         %c %c %c\n\n",getCubeFacelet(Location(U,F,L),U),getCubeFacelet(Location(U,F),U),getCubeFacelet(Location(U,F,R),U));
printf (" %c %c %c",getCubeFacelet(Location(L,B,U),L),getCubeFacelet(Location(L,U),L),getCubeFacelet(Location(L,F,U),L));
printf ("   %c %c %c",getCubeFacelet(Location(F,U,L),F),getCubeFacelet(Location(F,U),F),getCubeFacelet(Location(F,U,R),F));
printf ("   %c %c %c\n",getCubeFacelet(Location(R,F,U),R),getCubeFacelet(Location(R,U),R),getCubeFacelet(Location(R,B,U),R));
printf (" %c %c %c",getCubeFacelet(Location(L,B),L),getCubeFacelet(Location(L,L),L),getCubeFacelet(Location(L,F),L));
printf ("   %c %c %c",getCubeFacelet(Location(F,L),F),getCubeFacelet(Location(F,F),F),getCubeFacelet(Location(F,R),F));
printf ("   %c %c %c\n",getCubeFacelet(Location(R,F),R),getCubeFacelet(Location(R,R),R),getCubeFacelet(Location(R,B),R));
printf (" %c %c %c",getCubeFacelet(Location(L,B,D),L),getCubeFacelet(Location(L,D),L),getCubeFacelet(Location(L,F,D),L));
printf ("   %c %c %c",getCubeFacelet(Location(F,D,L),F),getCubeFacelet(Location(F,D),F),getCubeFacelet(Location(F,D,R),F));
printf ("   %c %c %c\n\n",getCubeFacelet(Location(R,F,D),R),getCubeFacelet(Location(R,D),R),getCubeFacelet(Location(R,B,D),R));
printf ("         %c %c %c\n",getCubeFacelet(Location(D,F,L),D),getCubeFacelet(Location(D,F),D),getCubeFacelet(Location(D,F,R),D));
printf ("         %c %c %c\n",getCubeFacelet(Location(D,L),D),getCubeFacelet(Location(D,D),D),getCubeFacelet(Location(D,R),D));
printf ("         %c %c %c\n\n",getCubeFacelet(Location(D,B,L),D),getCubeFacelet(Location(D,B),D),getCubeFacelet(Location(D,B,R),D));
printf ("         %c %c %c\n",getCubeFacelet(Location(B,D,L),B),getCubeFacelet(Location(B,D),B),getCubeFacelet(Location(B,D,R),B));
printf ("         %c %c %c\n",getCubeFacelet(Location(B,L),B),getCubeFacelet(Location(B,B),B),getCubeFacelet(Location(B,R),B));
printf ("         %c %c %c\n",getCubeFacelet(Location(B,U,L),B),getCubeFacelet(Location(B,U),B),getCubeFacelet(Location(B,U,R),B));
}





