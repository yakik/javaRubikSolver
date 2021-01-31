
/***************************************************************************
                          cube.h  -  description
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

class Permutation;

#ifndef __Rubik_H
#define __Rubik_H

#include <stdio.h>
#include "Location.h"
#include "Rotation.h"
#include "Position.h"
#include "Cubicle.h"
#include "Cubie.h"
#include "Permutation.h"





class Rubik
{
public:

		Rubik(void);
		~Rubik();	
		void rotateFace(Rotation p_rotation);
		Location getCubicleCubieLocation(Location p_cubicleLocation);
		Position getCubicleCubiePosition(Location p_cubicleLocation);
		void printCube();
		char 		getCubeFacelet(Location p_location, int p_face);
		void reset();
		int set(Permutation *p_permutation);
		Permutation *getPermutation();

private:

		Cubicle *c_edgeCubicles[6][6];
		Cubicle *c_cornerCubicles[6][6][6];
		Cubicle *getCubicle(Location p_location);
		Cubicle *c_edgeCubiclePerFace [6][4];
		Cubicle *c_cornerCubiclePerFace [6][4];
		void initCorner(Location p_location);
		void resetData();
		void buildCubiclesPerFace();


};

#endif
