

/***************************************************************************
                          Cuibicle.h  -  description
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

class Cubicle;
#ifndef __Cubicle_H
#define __Cubicle_H

#include "Location.h"
#include "Cubie.h"


class Cubicle
{
public:
	Cubicle(Location p_location);
	Cubie *getHomeCubie();
	Cubie *getCurrentCubie();
	Location getLocation();
	void setHomeCubie(Cubie *p_cubie);
	void setCurrentCubie(Cubie *p_cubie);
	~Cubicle();

private:
	Cubie *c_homeCubie;
	Cubie *c_currentCubie;
	Location c_location;

};

#endif
