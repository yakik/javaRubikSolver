/***************************************************************************
                          Cubie.h  -  description
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
class Cubie;
#ifndef __Cubie_H
#define __Cubie_H

#include "Position.h"
#include "Cubicle.h"
#include "Rotation.h"


class Cubie
{
public:	
	Cubie(){}
	void rotate(Rotation p_rotation){c_position.rotate(p_rotation);}
	int getFace(int p_viewpoint){return c_position.getFace(p_viewpoint);}	
	Cubicle *getHomeCubicle();
	Cubicle *getCurrentCubicle();
	Position getPosition(){return c_position;}
	void setHomeCubicle(Cubicle *p_cubicle);
	void setCurrentCubicle(Cubicle *p_cubicle);
	void setPosition(Position p_position){c_position = p_position;}

private:
	Position c_position;
	Cubicle *c_homeCubicle;
	Cubicle *c_currentCubicle;

};

#endif
