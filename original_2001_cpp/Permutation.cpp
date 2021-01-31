/***************************************************************************
                          Permutation.cpp  -  description
                             -------------------
    begin                : Fri Apr 20 2001
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
#include "Permutation.h"




  void Permutation::addCubicleData(CubicleData p_cubicleData)
	{
		c_cubicles++;
		c_cubicleData[c_cubicles] = p_cubicleData;
	}

  int Permutation::isPartRubik(Rubik *p_rubik)
  {
  	int i;
  	for (i=0;i<c_cubicles;i++)
  		if ((p_rubik->getCubicleCubieLocation(c_cubicleData[i].getLocation())!=
           c_cubicleData[i].getCubieLocation()) ||
  				(p_rubik->getCubicleCubiePosition(c_cubicleData[i].getLocation())!=
           c_cubicleData[i].getCubiePosition()))
      	return 0;
    return 1;
  }
  int Permutation::getDifferece(Rubik *p_rubik)
  {
   	int i, l_counter=0;
  	for (i=0;i<c_cubicles;i++)
	  {
	  	Location l_perL, l_rubL;
	  	Position l_perP, l_rubP;
	  	l_perL = c_cubicleData[i].getCubieLocation();
	  	l_rubL = p_rubik->getCubicleCubieLocation(c_cubicleData[i].getLocation());
	  	l_perP = c_cubicleData[i].getCubiePosition();
	  	l_rubP = p_rubik->getCubicleCubiePosition(c_cubicleData[i].getLocation());

	  	if ((p_rubik->getCubicleCubieLocation(c_cubicleData[i].getLocation())!=
           c_cubicleData[i].getCubieLocation()) ||
  				(p_rubik->getCubicleCubiePosition(c_cubicleData[i].getLocation())!=
           c_cubicleData[i].getCubiePosition()))
      	l_counter++;
     }
     return l_counter;
  }

  void Permutation::print()
  {
  	int i;
  	printf("\nnumber of cubicles is %d\n",c_cubicles+1);
  	for (i=0;i<=c_cubicles;i++)
  	{
  		printf("Cubicle Location:");
  		c_cubicleData[i].getLocation().print();
			printf(" Cubie Location:");  		
  	  c_cubicleData[i].getCubieLocation().print();
  	  printf(" Cubie Position:");  		
  	  c_cubicleData[i].getCubiePosition().print();
  	  printf("\n");
    }
  }

  void Permutation::load(FILE *p_file)
  {
  // reading order is: 12 edges first, then 8 corners
  // reading order: cubicle, current cubie location, current cubie position
  int i;
 	Location l_cubicleLocation, l_currCubicleLocation;
 	Position l_position;
  for (i=0;i<12;i++)
  {
  	int l_cubicleFace0,l_cubicleFace1;
  	int l_currCubicleFace0,l_currCubicleFace1;
  	int l_up,l_front;

  	l_cubicleFace0 = getCharFace(fgetc(p_file));
  	l_cubicleFace1 = getCharFace(fgetc(p_file));
  	fgetc(p_file);
  	l_currCubicleFace0 = getCharFace(fgetc(p_file));
  	l_currCubicleFace1 = getCharFace(fgetc(p_file));
  	fgetc(p_file);
  	l_up = getCharFace(fgetc(p_file));
  	l_front = getCharFace(fgetc(p_file));
  	fgetc(p_file);
  	l_cubicleLocation = Location(l_cubicleFace0,l_cubicleFace1);
		l_currCubicleLocation = Location(l_currCubicleFace0,l_currCubicleFace1);
		l_position = Position(l_up,l_front);
		addCubicleData(CubicleData(l_cubicleLocation,l_currCubicleLocation,l_position));  	
  }
  for (i=0;i<8;i++)
  {
  	int l_cubicleFace0,l_cubicleFace1,l_cubicleFace2;
  	int l_currCubicleFace0,l_currCubicleFace1,l_currCubicleFace2;
  	int l_up,l_front;

  	l_cubicleFace0 = getCharFace(fgetc(p_file));
  	l_cubicleFace1 = getCharFace(fgetc(p_file));
  	l_cubicleFace2 = getCharFace(fgetc(p_file));  	
  	fgetc(p_file);
  	l_currCubicleFace0 = getCharFace(fgetc(p_file));
  	l_currCubicleFace1 = getCharFace(fgetc(p_file));
  	l_currCubicleFace2 = getCharFace(fgetc(p_file));  	
  	fgetc(p_file);
  	l_up = getCharFace(fgetc(p_file));
  	l_front = getCharFace(fgetc(p_file));
  	fgetc(p_file);
  	l_cubicleLocation = Location(l_cubicleFace0,l_cubicleFace1,l_cubicleFace2);
		l_currCubicleLocation = Location(l_currCubicleFace0,l_currCubicleFace1,l_currCubicleFace2);
		l_position = Position(l_up,l_front);
		addCubicleData(CubicleData(l_cubicleLocation,l_currCubicleLocation,l_position));  	
  }
 }
  	
 int Permutation::getValue(int p_onlyFirstFloor)
 {
 	int i,l_value=0;
 	for (i=0;i<20;i++)
 	{
 		Location l_currLocation = c_cubicleData[i].getLocation();
 		if ( !p_onlyFirstFloor ||
 				(l_currLocation == Location(D,L) ||
 				l_currLocation == Location(D,R) ||
 				l_currLocation == Location(D,B) ||
 				l_currLocation == Location(D,F) ||
 				l_currLocation == Location(D,F,R) ||
 				l_currLocation == Location(D,F,L) ||
 				l_currLocation == Location(D,B,R) ||
 				l_currLocation == Location(D,B,L)))
 		{		
 			if (c_cubicleData[i].getLocation()==c_cubicleData[i].getCubieLocation())
 			{
 				l_value++;
 			if (c_cubicleData[i].getCubiePosition() == Position(U,F))
 				l_value++;
 			}
 		}
 	}
 	return l_value;
 }

Permutation *Permutation::getCopy()
{
	Permutation *l_permutation = new Permutation();
	int i;
	for (i=0;i<20;i++)
		l_permutation->addCubicleData(getCubicleData(i));
	return l_permutation;
}
 	
int Permutation::operator ==(Permutation p_permutation)
{
	int i;
	for (i=0;i<20;i++)
		if (!(getCubicleData(i) == p_permutation.getCubicleData(i)))
			return 0;
	return 1;
}
