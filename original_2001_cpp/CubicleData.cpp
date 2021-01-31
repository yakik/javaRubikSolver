/***************************************************************************
                          CubicleData.cpp  -  description
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
#include "CubicleData.h"

	CubicleData::CubicleData(Location p_location, Location p_cubieLocation, Position p_cubiePosition)
	{
		c_location = p_location;
		c_cubieLocation = p_cubieLocation;
		c_cubiePosition = p_cubiePosition;
	}
	
	int CubicleData::operator ==(CubicleData p_cubicleData)
	{
		return (c_location == p_cubicleData.c_location &&
						c_cubieLocation == p_cubicleData.c_cubieLocation &&
						c_cubiePosition == p_cubicleData.c_cubiePosition);
	}
