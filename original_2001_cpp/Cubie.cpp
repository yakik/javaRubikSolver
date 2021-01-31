/***************************************************************************
                          Cubie.cpp  -  description
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
#include "Cubie.h"

	Cubicle *Cubie::getHomeCubicle()
	{
		return c_homeCubicle;
	}

	Cubicle *Cubie::getCurrentCubicle()
	{
		return c_currentCubicle;
	}

	void Cubie::setHomeCubicle(Cubicle *p_cubicle)
	{
		c_homeCubicle = p_cubicle;
	}
	
	void Cubie::setCurrentCubicle(Cubicle *p_cubicle)
	{
		c_currentCubicle = p_cubicle;
	}


