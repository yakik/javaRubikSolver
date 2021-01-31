/***************************************************************************
                          Cubicle.cpp  -  description
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
#include "Cubicle.h"

	Cubicle::Cubicle(Location p_location)
	{
		Cubie *l_cubie;
		c_location = p_location;
		l_cubie = new Cubie();
		(*l_cubie).setHomeCubicle(this);
		(*l_cubie).setCurrentCubicle(this);
		setHomeCubie(l_cubie);
		setCurrentCubie(l_cubie);
	}

	Location Cubicle::getLocation()
	{
		return c_location;
	}				

	Cubie *Cubicle::getHomeCubie()
	{
		return c_homeCubie;
	}

	Cubie *Cubicle::getCurrentCubie()
	{
		return c_currentCubie;
	}

	Cubicle::~Cubicle()
	{
		if (c_homeCubie != NULL)
		{
			delete c_homeCubie;
			c_homeCubie = NULL;
		}
	}	
	
	void Cubicle::setHomeCubie(Cubie *p_cubie)
	{
		c_homeCubie = p_cubie;
	}
	
	void Cubicle::setCurrentCubie(Cubie *p_cubie)
	{
		c_currentCubie = p_cubie;
		p_cubie ->setCurrentCubicle(this);
	}


